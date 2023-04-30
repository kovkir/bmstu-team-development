from tkinter import Canvas, CENTER
from color import *

from chessPieces.chessPiece import ChessPiece


class Elephant(ChessPiece):
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
        self.drawElephant(self.xLeftChessBoard + self.xCell * self.sizeCell,
                          self.yTopChessBoard  + self.yCell * self.sizeCell)
                          

    def drawElephant(self, x, y):
        # верхняя часть слона
        self.canvas.create_oval(
            x + self.sizeCell * 0.33, y + self.sizeCell * 0.22,
            x + self.sizeCell * 0.67, y + self.sizeCell * 0.72,
            outline = self.colorBorder, fill = self.color, width = 2
        )

        # наконечник слона
        self.canvas.create_oval(
            x + self.sizeCell * 0.42, y + self.sizeCell * 0.08,
            x + self.sizeCell * 0.58, y + self.sizeCell * 0.24,
            outline = self.colorBorder, fill = self.color, width = 2
        )

        # тело слона
        self.canvas.create_polygon(
            [x + self.sizeCell * 0.4, y + self.sizeCell * 0.67,
             x + self.sizeCell * 0.6, y + self.sizeCell * 0.67,
             x + self.sizeCell * 0.7, y + self.sizeCell * 0.75,
             x + self.sizeCell * 0.3, y + self.sizeCell * 0.75
            ],
            outline = self.colorBorder, fill = self.color, width = 2
        )

        # подставка слона
        self.canvas.create_rectangle(
            x + self.sizeCell * 0.2, y + self.sizeCell * 0.75,
            x + self.sizeCell * 0.8, y + self.sizeCell * 0.87,
            outline = self.colorBorder, fill = self.color, width = 2
        )
        
     # нахождение списка всех возможных ходов слона
    def calculateMovement(self, mainWhiteСolor: bool, isColorWhite: bool,
                          wChessBool: list, bChessBool: list):
        self.movement.clear()

        if isColorWhite:
            myChessBool = wChessBool
            anotherChessBool = bChessBool
        else:
            myChessBool = bChessBool
            anotherChessBool = wChessBool    

        # добавление ходов вверх налево по диагонали
        x = self.xCell - 1
        y = self.yCell - 1

        while x >= 0 and y >= 0:
            # путь перегораживает своя фигура
            if myChessBool[y][x]:
                break

            self.movement.append([x, y])

            # путь перегораживает фигура соперника
            if anotherChessBool[y][x]:
                break

            x -= 1
            y -= 1

        # добавление ходов вверх направо по диагонали
        x = self.xCell + 1
        y = self.yCell - 1

        while x <= 7 and y >= 0:
            # путь перегораживает своя фигура
            if myChessBool[y][x]:
                break

            self.movement.append([x, y])

            # путь перегораживает фигура соперника
            if anotherChessBool[y][x]:
                break

            x += 1
            y -= 1

        # добавление ходов вниз налево по диагонали
        x = self.xCell - 1
        y = self.yCell + 1
        
        while x >= 0 and y <= 7:
            # путь перегораживает своя фигура
            if myChessBool[y][x]:
                break

            self.movement.append([x, y])

            # путь перегораживает фигура соперника
            if anotherChessBool[y][x]:
                break

            x -= 1
            y += 1

        # добавление ходов вниз направо по диагонали
        x = self.xCell + 1
        y = self.yCell + 1

        while x <= 7 and y <= 7:
            # путь перегораживает своя фигура
            if myChessBool[y][x]:
                break

            self.movement.append([x, y])

            # путь перегораживает фигура соперника
            if anotherChessBool[y][x]:
                break

            x += 1
            y += 1

        return self.movement
    