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

    
    # нахождение списка всех возможных ходов пешки
    def calculateMovement(self, mainWhiteСolor: bool, activeWhitePlayer: bool,
                          wChessBool: list, bChessBool: list):
        self.movement.clear()

        if activeWhitePlayer:
            myChessBool = wChessBool
            anotherChessBool = bChessBool
        else:
            myChessBool = bChessBool
            anotherChessBool = wChessBool    

        step = -1 if mainWhiteСolor == activeWhitePlayer else 1

        # добавление ходов вперед
        x = self.xCell - 1
        y = self.yCell + step
        if x >= 0 and y >= 0 and y <= 7 and anotherChessBool[y][x]:
            self.movement.append([x, y])

        x = self.xCell + 1
        y = self.yCell + step
        if x <= 7 and y >= 0 and y <= 7 and anotherChessBool[y][x]:
            self.movement.append([x, y])

        x = self.xCell
        y = self.yCell + step
        if y >= 0 and y <= 7 and anotherChessBool[y][x] == False:
            self.movement.append([x, y])

        # при первом ходе пешка может ходить на 2 клетки вперед
        x = self.xCell
        y = self.yCell + (step * 2)
        if self.firstTurn \
            and y >= 0 and y <= 7 \
            and myChessBool[y - step][x] == False \
            and anotherChessBool[y - step][x] == False \
            and anotherChessBool[y][x] == False:

            self.movement.append([self.xCell, self.yCell + (step * 2)])

        return self.movement
    