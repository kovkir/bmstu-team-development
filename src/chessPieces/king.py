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


    # нахождение списка всех возможных ходов короля без учета расположения других фигур
    def calculateMovement(self, mainWhiteСolor: bool, activeWhitePlayer: bool):
        self.movement.clear()

        # добавление ходов вверх и вниз
        for i in range(-1, 2, 1):
            self.movement.append([self.xCell + i, self.yCell + 1])
            self.movement.append([self.xCell + i, self.yCell - 1])

        # добавление ходов влево и направо
        self.movement.append([self.xCell + 1, self.yCell])
        self.movement.append([self.xCell - 1, self.yCell])
        