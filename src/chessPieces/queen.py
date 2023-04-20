from tkinter import Canvas, CENTER
from color import *

from chessPieces.chessPiece import ChessPiece


class Queen(ChessPiece):
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
        self.drawQueen(self.xLeftChessBoard + self.xCell * self.sizeCell,
                          self.yTopChessBoard  + self.yCell * self.sizeCell)
                          

    def drawQueen(self, x, y):
        # тело ферзя
        self.canvas.create_polygon(
            [x + self.sizeCell * 0.3, y + self.sizeCell * 0.75,
             x + self.sizeCell * 0.125, y + self.sizeCell * 0.32,
             x + self.sizeCell * 0.29,  y + self.sizeCell * 0.47,
             x + self.sizeCell * 0.375, y + self.sizeCell * 0.25,
             x + self.sizeCell * 0.5,   y + self.sizeCell * 0.47,
             x + self.sizeCell * 0.625, y + self.sizeCell * 0.25,
             x + self.sizeCell * 0.71,  y + self.sizeCell * 0.47,
             x + self.sizeCell * 0.875, y + self.sizeCell * 0.32,
             x + self.sizeCell * 0.7,   y + self.sizeCell * 0.75],
            outline = self.colorBorder, fill = self.color, width = 2
        )

        # кружки на короне ферзя слева направо
        self.canvas.create_oval(
            x + self.sizeCell * 0.07, y + self.sizeCell * 0.255,
            x + self.sizeCell * 0.2, y + self.sizeCell * 0.375,
            outline = self.colorBorder, fill = self.color, width = 2
        )

        self.canvas.create_oval(
            x + self.sizeCell * 0.31, y + self.sizeCell * 0.185,
            x + self.sizeCell * 0.43, y + self.sizeCell * 0.305,
            outline = self.colorBorder, fill = self.color, width = 2
        )

        self.canvas.create_oval(
            x + self.sizeCell * 0.56,  y + self.sizeCell * 0.185,
            x + self.sizeCell * 0.69,  y + self.sizeCell * 0.305,
            outline = self.colorBorder, fill = self.color, width = 2
        )

        self.canvas.create_oval(
            x + self.sizeCell * 0.80,  y + self.sizeCell * 0.255,
            x + self.sizeCell * 0.93,  y + self.sizeCell * 0.375,
            outline = self.colorBorder, fill = self.color, width = 2
        )

        # подставка ферзя
        self.canvas.create_rectangle(
            x + self.sizeCell * 0.2, y + self.sizeCell * 0.75,
            x + self.sizeCell * 0.8, y + self.sizeCell * 0.87,
            outline = self.colorBorder, fill = self.color, width = 2
        )


    