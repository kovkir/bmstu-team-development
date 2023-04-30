from tkinter import Canvas, CENTER
from color import *


class ChessPiece:
    canvas: Canvas
    sizeCell: int
    xLeftChessBoard: int
    yTopChessBoard: int

    name: str
    color: str
    colorBorder: str
    xCell: int
    yCell: int


    def __init__(self, canvas: Canvas, sizeCell: int, xLeftChessBoard: int, yTopChessBoard: int,
                 name: str, color: str, xCell: int, yCell: int):
        self.canvas = canvas
        self.sizeCell = sizeCell
        self.xLeftChessBoard = xLeftChessBoard
        self.yTopChessBoard = yTopChessBoard
        
        self.name = name
        self.color = color
        self.colorBorder = WHITE_CHESS_PIECE_BOERDER if color == WHITE_CHESS_PIECE else BLACK_CHESS_PIECE_BOERDER
        self.xCell = xCell
        self.yCell = yCell


    def drawPiece(self):
        self.drawPlug(self.xLeftChessBoard + self.xCell * self.sizeCell,
                      self.yTopChessBoard  + self.yCell * self.sizeCell)
    

    def drawPlug(self, x, y):
        # Заглушка c именем фигуры
        self.canvas.create_text(
            x + self.sizeCell / 2, y + self.sizeCell / 2,
            text = self.name, justify = CENTER, 
            font = ("Arial", 20, "bold"), fill = self.color
        )


    def calculateMovement(self, mainWhiteСolor: bool, isColorWhite: bool,
                          wChessBool: list, bChessBool: list):
        print("Попытка нахождение списка всех возможных ходов несуществующей фигуры")


    def isMy(self, xNewСell: int, yNewСell: int):
        return self.xCell == xNewСell and \
               self.yCell == yNewСell
    

    def setCell(self, xNewСell: int, yNewСell: int):
        self.xCell = xNewСell
        self.yCell = yNewСell
