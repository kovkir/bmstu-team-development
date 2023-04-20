from tkinter import Canvas, CENTER
from color import *

from chessPieces.chessPiece import ChessPiece


class Pawn(ChessPiece):
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
    firstTurn: bool


    def __init__(self, canvas: Canvas, sizeCell: int, xLeftChessBoard: int, yTopChessBoard: int,
                 name: str, color: str, xCell: int, yCell: int):
        super().__init__(canvas, sizeCell, xLeftChessBoard, yTopChessBoard,
                 name, color, xCell, yCell)
        self.movement = list()
        self.firstTurn = True


    def drawPiece(self):
        self.drawPawn(self.xLeftChessBoard + self.xCell * self.sizeCell,
                      self.yTopChessBoard  + self.yCell * self.sizeCell)
                          

    def drawPawn(self, x, y):
        # голова пешки
        self.canvas.create_oval(
            x + self.sizeCell * 0.37, y + self.sizeCell * 0.17,
            x + self.sizeCell * 0.63, y + self.sizeCell * 0.43,
            outline = self.colorBorder, fill = self.color, width = 2
        )

        # тело пешки
        self.canvas.create_arc(
            x + self.sizeCell * 0.28, y + self.sizeCell * 0.5,
            x + self.sizeCell * 0.72, y + self.sizeCell * 1.2,
            start = 0, extent = 180, outline = self.colorBorder, fill = self.color, width = 2
        )

    
    # нахождение списка всех возможных ходов пешки без учета расположения других фигур
    def calculateMovement(self, mainWhiteСolor: bool, activeWhitePlayer: bool):
        self.movement.clear()

        step = -1 if mainWhiteСolor == activeWhitePlayer else 1

        # добавление ходов вперед
        for i in range(-1, 2, 1):
            self.movement.append([self.xCell + i, self.yCell + step])

        # при первом ходе пешка может ходить на 2 клетки вперед
        if self.firstTurn:
            self.movement.append([self.xCell, self.yCell + (step * 2)])
