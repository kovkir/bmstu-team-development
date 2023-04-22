from tkinter import Canvas, messagebox, CENTER

from chessPieces.chessPiece import ChessPiece
from chessPieces.queen import Queen
from chessPieces.king import King
from chessPieces.pawn import Pawn
from chessPieces.rook import Rook
from chessPieces.horse import Horse
from chessPieces.elephant import Elephant
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
        self.deletedPieces = self.createDeletedPiecesDict()
        self.calculateMovement()

    
    def createChessPieces(self, color: str):
        '''
        Получение списка шахматных фигур заданного цвета 
        '''
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
            pawn = Pawn(self.canvas, self.sizeCell, self.xLeftChessBoard, self.yTopChessBoard, 
                "Pawn", color, i, indStrPawns)
            chessPieces.append(pawn)

        # создание ладей
        chessPieces.append(Rook(self.canvas, self.sizeCell, self.xLeftChessBoard, self.yTopChessBoard, 
            "Rook", color, 0, indStrOtherPieces))
        chessPieces.append(Rook(self.canvas, self.sizeCell, self.xLeftChessBoard, self.yTopChessBoard, 
            "Rook", color, 7, indStrOtherPieces))

        # создание коней
        chessPieces.append(Horse(self.canvas, self.sizeCell, self.xLeftChessBoard, self.yTopChessBoard, 
            "Horse", color, 1, indStrOtherPieces))
        chessPieces.append(Horse(self.canvas, self.sizeCell, self.xLeftChessBoard, self.yTopChessBoard, 
            "Horse", color, 6, indStrOtherPieces))

        # создание слонов
        chessPieces.append(Elephant(self.canvas, self.sizeCell, self.xLeftChessBoard, self.yTopChessBoard, 
            "Elephant", color, 2, indStrOtherPieces))
        chessPieces.append(Elephant(self.canvas, self.sizeCell, self.xLeftChessBoard, self.yTopChessBoard, 
            "Elephant", color, 5, indStrOtherPieces))

        # создание ферзя
        chessPieces.append(Queen(self.canvas, self.sizeCell, self.xLeftChessBoard, self.yTopChessBoard, 
            "Queen", color, 3, indStrOtherPieces))
        
        # создание короля
        chessPieces.append(King(self.canvas, self.sizeCell, self.xLeftChessBoard, self.yTopChessBoard, 
            "King", color, 4, indStrOtherPieces))
        
        return chessPieces
    
    
    def createDeletedPiecesDict(self):
        '''
        Создание словаря съеденных фигур
        '''
        keys = ["wPawn", "wHorse", "wElephant", "wRook", "wQueen",
                "bPawn", "bHorse", "bElephant", "bRook", "bQueen"]

        deletedPieces = dict()
        deletedPieces = dict.fromkeys(keys, 0)

        return deletedPieces


    def drawChessPieces(self):
        '''
        Отображение фигур на шахматной доске
        '''
        for piece in self.wChessPieces:
            piece.drawPiece()

        for piece in self.bChessPieces:
            piece.drawPiece()


    def drawChessBoard(self):
        '''
        Отображение шахматной доски
        '''
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
        '''
        Перевернуть шаматную доску
        '''
        self.mainWhiteСolor = mainWhiteСolor
        self.cancelChooseCell()

        for piece in self.wChessPieces:
            piece.yCell = 7 - piece.yCell

        for piece in self.bChessPieces:
            piece.yCell = 7 - piece.yCell

        self.calculateMovement()
    

    def searchNewСell(self, xEvent: int, yEvent: int):
        '''
        Нахождение координат выбранной клетки
        '''
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
    

    def cellIsNotEmpty(self, xСell: int, yСell: int, isColorWhite: bool):
        '''
        Проверка, что нажали на фигуру ходящего игрока
        '''
        if isColorWhite:
            for piece in self.wChessPieces:
                if piece.isMy(xСell, yСell):
                    return True
        else:
            for piece in self.bChessPieces:
                if piece.isMy(xСell, yСell):
                    return True
        
        return False
    

    def getCurСell(self):
        '''
        Нахождение координат для вывода в окне "Выбранная фигура"
        '''
        if self.xCurСell >= 0 and \
           self.yCurСell >= 0:
            # нажали на фигуру ходящего игрока
            xCell = self.alphabet[self.xCurСell]
            yCell = str(8 - self.yCurСell)
            
        elif self.xCurСell == EMPTY or \
             self.yCurСell == EMPTY:
            # игрок тыкнул вне доски
            xCell = EMPTY
            yCell = EMPTY
        else:
            # игрок сделал ход
            xCell = MOVE_DONE
            yCell = MOVE_DONE

        return xCell, yCell
    

    def getPiece(self, xСell: int, yСell: int, isColorWhite: bool):
        '''
        Возвращает фигуру, которая делает ход
        '''
        if isColorWhite:
            for piece in self.wChessPieces:
                if piece.isMy(xСell, yСell):
                    return piece
        else:
            for piece in self.bChessPieces:
                if piece.isMy(xСell, yСell):
                    return piece
    

    def checkMovement(self, currPiece: ChessPiece, xNewCell: int, yNewCell: int):
        '''
        Проверяем xNewCell, yNewCell на присутствие в списке 
        возможных ходов. Далее для каждой фигуры вызывается соответствующая 
        ей функция, которая делает уникальные проверки
        '''
        if currPiece.name == "Pawn":
            currPiece.firstTurn = False

        print(currPiece.name, currPiece.movement, "\n")

        if [xNewCell, yNewCell] in currPiece.movement:
            print("Находится в списке ходов")
            return True
        else:
            print("Не находится в списке ходов")
            return False
        
    
    def deletePiece(self, piece: ChessPiece, isColorWhite: bool):
        '''
        Удаление фигуры из списка белых\черных фигур
        '''
        if isColorWhite:
            self.wChessPieces.remove(piece)
        else:
            self.bChessPieces.remove(piece)
        
    
    def eatPiece(self, eatenPiece: ChessPiece):
        '''
        Обновление словаря удаленных фигур
        '''
        key = ("w" if self.activeWhitePlayer else "b") + eatenPiece.name
        self.deletedPieces.update({key : self.deletedPieces[key] + 1}) 
        self.deletePiece(eatenPiece, not self.activeWhitePlayer)
        

    def movePiece(self, xNewСell: int, yNewСell: int):
        '''
        Игрок делает ход
        '''
        # фигура, которая делает ход
        currPiece = self.getPiece(self.xCurСell, self.yCurСell, self.activeWhitePlayer)

        if self.checkMovement(currPiece, xNewСell, yNewСell):
            # если пытаемся съесть фигуру соперника
            if self.cellIsNotEmpty(xNewСell, yNewСell, not self.activeWhitePlayer):
                eatenPiece = self.getPiece(xNewСell, yNewСell, not self.activeWhitePlayer)

                if eatenPiece.name == "King":
                    messagebox.showwarning("Ошибка", "Нельзя ходить на короля")
                    return

                self.eatPiece(eatenPiece)

            # перемещение фигуры
            currPiece.setCell(xNewСell, yNewСell)
            # ход переходит к следующему игроку
            self.activeWhitePlayer = not self.activeWhitePlayer
        else:
            messagebox.showinfo("Ошибка",
                "Выбранная фигура не может ходить в эту клетку.")
            

    def chooseСell(self, xEvent: int, yEvent: int):
        '''
        Игрок пытается выбрать клетку шахматной доски
        '''
        if xEvent < self.xLeftChessBoard or xEvent > self.xRightChessBoard or \
           yEvent < self.yTopChessBoard  or yEvent > self.yBottomChessBoard:
            # игрок тыкнул вне доски
            self.xCurСell = EMPTY
            self.yCurСell = EMPTY
        else:
            # координаты выбранной клетки
            xNewСell, yNewСell = self.searchNewСell(xEvent, yEvent)

            if self.cellIsNotEmpty(xNewСell, yNewСell, self.activeWhitePlayer):
                # нажали на фигуру ходящего игрока
                self.xCurСell = xNewСell 
                self.yCurСell = yNewСell

            elif self.xCurСell != EMPTY and self.yCurСell != EMPTY:
                # игрок делает ход
                self.movePiece(xNewСell, yNewСell)

                self.xCurСell = MOVE_DONE
                self.yCurСell = MOVE_DONE

        return self.getCurСell()


    def cancelChooseCell(self):
        '''
        Игрок отменяет прошлый выбор клетки шахматной доски
        '''
        self.xCurСell = EMPTY
        self.yCurСell = EMPTY


    def calculateMovement(self):
        '''
        Нахождение списка всех возможных ходов для каждой фигуры 
        (без учета расположения других фигур)
        '''
        for piece in self.wChessPieces:
            piece.calculateMovement(self.mainWhiteСolor, self.activeWhitePlayer)

        for piece in self.bChessPieces:
            piece.calculateMovement(self.mainWhiteСolor, self.activeWhitePlayer)


    def isMyMove(self):
        '''
        Проверка, что сейчас ход игрока, чьи фигуры отображены 
        внизу шахматной доски (ходить может только такой игрок)
        '''
        return self.mainWhiteСolor == self.activeWhitePlayer
