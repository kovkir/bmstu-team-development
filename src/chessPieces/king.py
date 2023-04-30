from tkinter import Canvas, CENTER
import numpy as np
from math import pi, sin, cos
from copy import deepcopy
from color import *

from chessPieces.chessPiece import ChessPiece


POINTS_COUNT = 100


class King(ChessPiece):
    canvas: Canvas
    sizeCell: int
    xLeftChessBoard: int
    yTopChessBoard: int

    name: str
    color: str
    colorBorder: str
    xCell: int
    yCell: int

    movement: list


    def __init__(self, canvas: Canvas, sizeCell: int, xLeftChessBoard: int, yTopChessBoard: int,
                 name: str, color: str, xCell: int, yCell: int):
        super().__init__(canvas, sizeCell, xLeftChessBoard, yTopChessBoard,
                 name, color, xCell, yCell)
        self.movement = list()


    def drawPiece(self):
        self.drawKing(self.xLeftChessBoard + self.xCell * self.sizeCell,
                      self.yTopChessBoard  + self.yCell * self.sizeCell)

    
    def rotation(self, dots, angleRot, xCenter, yCenter):
        angleRot = angleRot * pi / 180
        M_rot = np.array([[cos(angleRot) , -sin(angleRot)], [sin(angleRot), cos(angleRot)]])

        for i in range(len(dots)):
            dots[i][0] -= xCenter
            dots[i][1] -= yCenter

            dots[i] = np.dot(M_rot, dots[i])

            dots[i][0] += xCenter
            dots[i][1] += yCenter

        return dots
                          

    def drawKing(self, x, y):
        # основа для построения левой и правой частей короны короля
        angleRotArr = np.linspace(0, 2 * pi, POINTS_COUNT)
        # [[x1, x2], [y1, y2]]
        PartCrownArr = np.array([x + self.sizeCell * 0.5 + self.sizeCell * 0.2 * np.cos(angleRotArr), 
                                 y + self.sizeCell * 0.5 + self.sizeCell * 0.25 * np.sin(angleRotArr)])

        # [[x1, y1], [x2, y2]]
        PartCrown = list()
        for i in range(len(PartCrownArr[0])):
            PartCrown.append([PartCrownArr[0][i], PartCrownArr[1][i]])

        # левая часть короны короля
        leftPartCrown = self.rotation(deepcopy(PartCrown), -30, x + self.sizeCell * 0.5, y + self.sizeCell * 0.75)

        # [x1, y1, x2, y2]
        leftPartCrownPolygon = list()
        for i in range(len(leftPartCrown)):
            leftPartCrownPolygon.append(leftPartCrown[i][0])
            leftPartCrownPolygon.append(leftPartCrown[i][1])

        self.canvas.create_polygon(
            leftPartCrownPolygon, outline = self.colorBorder, fill = self.color, width = 2
        )

        # правая часть короны короля
        rightPartCrown = self.rotation(deepcopy(PartCrown), 30, x + self.sizeCell * 0.5, y + self.sizeCell * 0.75)

        # [x1, y1, x2, y2]
        rightPartCrownPolygon = list()
        for i in range(len(rightPartCrown)):
            rightPartCrownPolygon.append(rightPartCrown[i][0])
            rightPartCrownPolygon.append(rightPartCrown[i][1])

        self.canvas.create_polygon(
            rightPartCrownPolygon, outline = self.colorBorder, fill = self.color, width = 2
        )

        # наконечник короны короля
        self.canvas.create_polygon(
            [x + self.sizeCell * 0.43, y + self.sizeCell * 0.19,
             x + self.sizeCell * 0.5,  y + self.sizeCell * 0.1,
             x + self.sizeCell * 0.57, y + self.sizeCell * 0.19,
             x + self.sizeCell * 0.5,  y + self.sizeCell * 0.32],
            outline = self.colorBorder, fill = self.color, width = 2
        )

        # середина короны короля
        self.canvas.create_oval(
            x + self.sizeCell * 0.36, y + self.sizeCell * 0.25,
            x + self.sizeCell * 0.64, y + self.sizeCell * 0.75,
            outline = self.colorBorder, fill = self.color, width = 2
        )

        # подставка короля
        self.canvas.create_rectangle(
            x + self.sizeCell * 0.2, y + self.sizeCell * 0.75,
            x + self.sizeCell * 0.8, y + self.sizeCell * 0.87,
            outline = self.colorBorder, fill = self.color, width = 2
        )


    # нахождение списка всех возможных ходов короля
    def calculateMovement(self, mainWhiteСolor: bool, activeWhitePlayer: bool,
                          wChessBool: list, bChessBool: list):
        self.movement.clear()

        if activeWhitePlayer:
            myChessBool = wChessBool
        else:
            myChessBool = bChessBool 

        # добавление ходов вверх и вниз
        for i in range(-1, 2, 1):
            # добавление ходов вверх
            x = self.xCell + i
            y = self.yCell + 1

            if x >= 0 and x <= 7 and y <= 7 and myChessBool[y][x] == False:
                self.movement.append([x, y])
            
            # добавление ходов вниз
            x = self.xCell + i
            y = self.yCell - 1

            if x >= 0 and x <= 7 and y >= 0 and myChessBool[y][x] == False:
                self.movement.append([x, y])

        # добавление ходов влево
        x = self.xCell - 1
        y = self.yCell

        if x >= 0 and myChessBool[y][x] == False:
            self.movement.append([x, y])

        # добавление ходов направо
        x = self.xCell + 1
        y = self.yCell

        if x <= 7 and myChessBool[y][x] == False:
            self.movement.append([x, y])

        return self.movement
    

    def checkCheckmate(self, activeWhitePlayer: bool, wChessPieces: list, bChessPieces: list): 
        #wChessBool: list, bChessBool: list):
        # enemyPieces -- массив вражеских фигур
        if activeWhitePlayer:
            #myChessBool = wChessBool
            enemyPieces = bChessPieces
        else:
            #myChessBool = bChessBool
            enemyPieces = wChessPieces

        check = False
        checkmate = False


        # Идея -- 
        # 1) проверить ходы каждой фигуры соперника на наличие клетки с королем 
        # 2) если клетка с королем находится в каком-либо из массивов ходов фигур соперника, то это шах -> переход к пункту 3, иначе игра продолжается как обычно
        # 3) проверить каждую клетку из возможных ходов короля как в пункте 1, если в каждой клетке стоит шах, то это мат, иначе надо обрезать массив доступных ходов короля до значений, в которых не получается шах -> игрок обязан походить в одну из доступных клеток

        # реализация 1 пункта
        for enemyChessPiece in enemyPieces:
            for move in enemyChessPiece.movement:
                if self.xCell == move[0] and self.yCell == move[1]:
                    # если позиция короля совпала с каким-либо из ходов, то ставится флаг шаха
                    check = True
                    break


        # если был поставлен шах, то надо проверить возможность мата
        if check == True:
            # реализация 3 пункта
            for kingMove in self.movement:
                futureCheck = False
                for enemyChessPiece in enemyPieces:
                    print("King moves", self.movement)
                    print("Enemy piece moves", enemyChessPiece.movement)
                    for move in enemyChessPiece.movement:
                        # если возможный ход короля также попадает на какую-либо из клеток хода вражеской фигуры, то этот ход удаляется у Короля, поскольку если он туда пойдет, то там также будет шах, а следовательно, мат
                        if kingMove == move:
                            futureCheck = True
                            print("King move", kingMove)
                            self.movement.remove(kingMove)
                            break
                    if futureCheck == True:
                        break

            # если список ходов короля пустой, то ему поставили мат
            if len(self.movement) == 0:
                checkmate = True

        # по итогу циклов выше, будет либо определен мат, либо у Короля останутся только те ходы, где ему повторно сразу не поставят шах

        return check, checkmate


        
    