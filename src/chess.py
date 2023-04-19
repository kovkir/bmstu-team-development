from tkinter import Canvas, messagebox, CENTER

from color import *


EMPTY     = -1
MOVE_DONE = -2


class Chess:
    canvas: Canvas
    canvasWidth: int
    canvasHeight: int

    sizeChessBoard: int
    sizeCell: int

    xLeftChessBoard: int
    xRightChessBoard: int
    yTopChessBoard: int
    yBottomChessBoard: int

    xCurСell: int
    yCurСell: int

    mainWhiteСolor: bool
    activeWhitePlayer: bool

    alphabet: list
    wChessPieces: list
    bChessPieces: list
    deletedPieces: dict()


    def __init__(self, canvas: Canvas, canvasWidth: int, canvasHeight: int, mainWhiteСolor: bool):
        self.canvas = canvas
        self.canvasWidth = canvasWidth
        self.canvasHeight = canvasHeight

        self.mainWhiteСolor = mainWhiteСolor
        self.activeWhitePlayer = True

        self.sizeChessBoard = (canvasWidth if canvasWidth <= canvasHeight else canvasHeight) * 5 / 6
        self.sizeCell = self.sizeChessBoard / 8

        self.xLeftChessBoard = (self.canvasWidth - self.sizeChessBoard) / 2
        self.xRightChessBoard = self.xLeftChessBoard + self.sizeChessBoard
        self.yTopChessBoard = (self.canvasHeight - self.sizeChessBoard) / 2
        self.yBottomChessBoard = self.yTopChessBoard + self.sizeChessBoard

        self.xCurСell = EMPTY
        self.yCurСell = EMPTY

        self.alphabet = ["A", "B", "C", "D", "E", "F", "G", "H"]
        self.wChessPieces = self.createChessPieces(WHITE_CHESS_PIECE)
        self.bChessPieces = self.createChessPieces(BLACK_CHESS_PIECE)
    
    
    def createChessPieces(self, color: str):
        chessPieces = list()

        return chessPieces


    def drawChessBoard(self):
        x = self.xLeftChessBoard
        y = self.yTopChessBoard

        for i in range(8):
            # нумерация полей слева от доски
            self.canvas.create_text(
                x - 15, y + self.sizeCell / 2, text = str(8 - i),
                justify = CENTER, font = ("Arial", 20))

            for j in range(8):
                # темная клетка
                if (i + j) % 2 == self.mainWhiteСolor:
                    self.canvas.create_rectangle(
                        x, y, x + self.sizeCell, y + self.sizeCell, 
                        outline = PURPLE_DARK, fill = PURPLE)
                #светлая клетка
                else:
                    self.canvas.create_rectangle(
                        x, y, x + self.sizeCell, y + self.sizeCell, 
                        outline = PURPLE_DARK, fill = PURPLE_LIGHT)

                if i == 7:
                    # подпись полей под доской
                    self.canvas.create_text(
                        x + self.sizeCell / 2, y + self.sizeCell + 15, text = self.alphabet[j],
                        justify = CENTER, font = ("Arial", 20))

                x += self.sizeCell 

            x = self.xLeftChessBoard
            y += self.sizeCell
    
    
    def isMyMove(self):
        return self.mainWhiteСolor == self.activeWhitePlayer
