from tkinter import Canvas, CENTER
from color import *

from chessPieces.chessPiece import ChessPiece


class Rook(ChessPiece):
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
        self.drawRook(self.xLeftChessBoard + self.xCell * self.sizeCell,
                          self.yTopChessBoard  + self.yCell * self.sizeCell)
                          

    def drawRook(self, x, y):
        # крышка ладьи
        self.canvas.create_polygon(
            [x + self.sizeCell * 0.2,  y + self.sizeCell * 0.3,
             x + self.sizeCell * 0.2,  y + self.sizeCell * 0.14,
             x + self.sizeCell * 0.32, y + self.sizeCell * 0.14,
             x + self.sizeCell * 0.32, y + self.sizeCell * 0.25,
             x + self.sizeCell * 0.44, y + self.sizeCell * 0.25,
             x + self.sizeCell * 0.44, y + self.sizeCell * 0.14,
             x + self.sizeCell * 0.56, y + self.sizeCell * 0.14,
             x + self.sizeCell * 0.56, y + self.sizeCell * 0.25,
             x + self.sizeCell * 0.68, y + self.sizeCell * 0.25,
             x + self.sizeCell * 0.68, y + self.sizeCell * 0.14,
             x + self.sizeCell * 0.8,  y + self.sizeCell * 0.14,
             x + self.sizeCell * 0.8,  y + self.sizeCell * 0.3,

             x + self.sizeCell * 0.65, y + self.sizeCell * 0.43,
             x + self.sizeCell * 0.35, y + self.sizeCell * 0.43
            ],
            outline = self.colorBorder, fill = self.color, width = 2
        )

        # тело ладьи
        self.canvas.create_polygon(
            [x + self.sizeCell * 0.35, y + self.sizeCell * 0.43,
             x + self.sizeCell * 0.65, y + self.sizeCell * 0.43,
             x + self.sizeCell * 0.7,  y + self.sizeCell * 0.75,
             x + self.sizeCell * 0.3,  y + self.sizeCell * 0.75
            ],
            outline = self.colorBorder, fill = self.color, width = 2
        )

        # подставка ладьи
        self.canvas.create_rectangle(
            x + self.sizeCell * 0.2, y + self.sizeCell * 0.75,
            x + self.sizeCell * 0.8, y + self.sizeCell * 0.87,
            outline = self.colorBorder, fill = self.color, width = 2
        )

    # нахождение списка всех возможных ходов ладьи без учета расположения других фигур
    def calculateMovement(self, mainWhiteСolor: bool, activeWhitePlayer: bool):
        self.movement.clear()

        for i in range(8):
            # добавление ходов вверх и вниз
            if self.yCell != i:
                self.movement.append([self.xCell, i])
            
            # добавление ходов влево и направо
            if self.xCell != i:
                self.movement.append([i, self.yCell])