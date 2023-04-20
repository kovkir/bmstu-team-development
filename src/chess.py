from tkinter import Canvas, messagebox, CENTER

from chessPieces.chessPiece import ChessPiece
from chessPieces.queen import Queen
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

         # номера строк доски для расположения фигур
        if self.mainWhiteСolor:
            indStrPawns = 6 if color == WHITE_CHESS_PIECE else 1
            indStrOtherPieces = 7 if color == WHITE_CHESS_PIECE else 0
        else:
            indStrPawns = 6 if color == BLACK_CHESS_PIECE else 1
            indStrOtherPieces = 7 if color == BLACK_CHESS_PIECE else 0

        # создание пешек
        for i in range(8):
            pawn = ChessPiece(self.canvas, self.sizeCell, self.xLeftChessBoard, self.yTopChessBoard, 
                "Pawn", color, i, indStrPawns)
            chessPieces.append(pawn)

        # создание ладей
        chessPieces.append(ChessPiece(self.canvas, self.sizeCell, self.xLeftChessBoard, self.yTopChessBoard, 
            "Rook", color, 0, indStrOtherPieces))
        chessPieces.append(ChessPiece(self.canvas, self.sizeCell, self.xLeftChessBoard, self.yTopChessBoard, 
            "Rook", color, 7, indStrOtherPieces))

        # создание коней
        chessPieces.append(ChessPiece(self.canvas, self.sizeCell, self.xLeftChessBoard, self.yTopChessBoard, 
            "Horse", color, 1, indStrOtherPieces))
        chessPieces.append(ChessPiece(self.canvas, self.sizeCell, self.xLeftChessBoard, self.yTopChessBoard, 
            "Horse", color, 6, indStrOtherPieces))

        # создание слонов
        chessPieces.append(ChessPiece(self.canvas, self.sizeCell, self.xLeftChessBoard, self.yTopChessBoard, 
            "Elephant", color, 2, indStrOtherPieces))
        chessPieces.append(ChessPiece(self.canvas, self.sizeCell, self.xLeftChessBoard, self.yTopChessBoard, 
            "Elephant", color, 5, indStrOtherPieces))

        # создание ферзя
        chessPieces.append(Queen(self.canvas, self.sizeCell, self.xLeftChessBoard, self.yTopChessBoard, 
            "Queen", color, 3, indStrOtherPieces))
        
        # создание короля
        chessPieces.append(ChessPiece(self.canvas, self.sizeCell, self.xLeftChessBoard, self.yTopChessBoard, 
            "King", color, 4, indStrOtherPieces))
        
        return chessPieces


    def drawChessPieces(self):
        for piece in self.wChessPieces:
            piece.drawPiece()

        for piece in self.bChessPieces:
            piece.drawPiece()


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

    
    def flipChessBoard(self, mainWhiteСolor: bool):
        self.mainWhiteСolor = mainWhiteСolor
        self.cancelChooseCell()

        for piece in self.wChessPieces:
            piece.yCell = 7 - piece.yCell

        for piece in self.bChessPieces:
            piece.yCell = 7 - piece.yCell
    

    def searchNewСell(self, xEvent: int, yEvent: int):
        xNewСell = EMPTY
        yNewСell = EMPTY

        for i in range(1, 9):
            if xEvent <= i * self.sizeCell + self.xLeftChessBoard:
                xNewСell = i - 1
                break
        
        for j in range(1, 9):
            if yEvent <= j * self.sizeCell + self.yTopChessBoard:
                yNewСell = j - 1
                break
        
        return xNewСell, yNewСell
    

    def getCurСell(self):
        if self.xCurСell >= 0 and \
           self.yCurСell >= 0:

            xCell = self.alphabet[self.xCurСell]
            yCell = str(8 - self.yCurСell)
        else:
            xCell = EMPTY
            yCell = EMPTY

        return xCell, yCell
    

    def chooseСell(self, xEvent: int, yEvent: int):
        if xEvent < self.xLeftChessBoard or xEvent > self.xRightChessBoard or \
           yEvent < self.yTopChessBoard  or yEvent > self.yBottomChessBoard:
            
            self.xCurСell = EMPTY
            self.yCurСell = EMPTY
        else:
            xNewСell, yNewСell = self.searchNewСell(xEvent, yEvent)

            self.xCurСell = xNewСell 
            self.yCurСell = yNewСell

        return self.getCurСell()


    def cancelChooseCell(self):
        self.xCurСell = EMPTY
        self.yCurСell = EMPTY


    def isMyMove(self):
        return self.mainWhiteСolor == self.activeWhitePlayer
