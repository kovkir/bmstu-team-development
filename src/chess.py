from tkinter import Canvas, messagebox, CENTER

from chessPieces.chessPiece import ChessPiece
from chessPieces.queen import Queen
from chessPieces.king import King
from chessPieces.pawn import Pawn
from chessPieces.rook import Rook
from chessPieces.horse import Horse
from chessPieces.elephant import Elephant
from color import *
from constants import *


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
    wChessBool: list
    bChessBool: list

    check: bool
    checkmate: bool


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

        self.check     = False
        self.checkmate = False

        self.alphabet = ["A", "B", "C", "D", "E", "F", "G", "H"]
        self.wChessPieces = self.createChessPieces(WHITE_CHESS_PIECE)
        self.bChessPieces = self.createChessPieces(BLACK_CHESS_PIECE)
        self.deletedPieces = self.createDeletedPiecesDict()
        self.wChessBool = self.createChessBool(mainWhiteСolor)
        self.bChessBool = self.createChessBool(not mainWhiteСolor)
        self.calculateMovement()

    
    def createChessBool(self, mainWhiteСolor: str):
        '''
        Получение булевой матрицы размера доски, каждый элемент которой 
        отвечает за присутствие фигуры в данной клетке 
        '''
        chessBool = []

        if mainWhiteСolor:
            chessBool.append([False for _ in range(8)])
            chessBool.append([False for _ in range(8)])
        else:
            chessBool.append([True for _ in range(8)])
            chessBool.append([True for _ in range(8)])

        for _ in range(4):
            chessBool.append([False for _ in range(8)])

        if mainWhiteСolor:
            chessBool.append([True for _ in range(8)])
            chessBool.append([True for _ in range(8)])
        else:
            chessBool.append([False for _ in range(8)])
            chessBool.append([False for _ in range(8)])

        return chessBool
    

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

        self.wChessBool.reverse()
        self.bChessBool.reverse()
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
            return self.wChessBool[yСell][xСell]
        else:
            return self.bChessBool[yСell][xСell]


    def getCurСell(self):
        '''
        Нахождение координат для вывода в окне "Выбранная фигура"
        '''
        xCell = self.alphabet[self.xCurСell]
        yCell = str(8 - self.yCurСell)
            
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
        Проверяем xNewCell, yNewCell на присутствие в списке возможных ходов.
        '''
        print("\nСписок возможных ходов для {:s}{:s}{:s}: {}"
            .format(PURPLE_TERMINAL, currPiece.name, BASE_COLOR_TERMINAL, currPiece.movement))
        print("Игрок походил: {:s}{}{:s}"
            .format(PURPLE_TERMINAL, [xNewCell, yNewCell], BASE_COLOR_TERMINAL))

        if self.checkmate:
            print("Игра окончена, вы не можите больше ходить")
            return False
            
        if [xNewCell, yNewCell] in currPiece.movement:
            print("Находится в списке ходов")

            if self.check and currPiece.name != "King":
                print("Недоступный ход, вам был поставлен шах")
                return False
            else:
                self.check = False

            if currPiece.name == "Pawn":
                print("Пешка больше не может ходить на 2 клетки")
                currPiece.firstTurn = False

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
            self.wChessBool[piece.yCell][piece.xCell] = False
        else:
            self.bChessPieces.remove(piece)
            self.bChessBool[piece.yCell][piece.xCell] = False
        
    
    def eatPiece(self, eatenPiece: ChessPiece):
        '''
        Обновление словаря удаленных фигур
        '''
        key = ("w" if self.activeWhitePlayer else "b") + eatenPiece.name
        self.deletedPieces.update({key : self.deletedPieces[key] + 1}) 
        self.deletePiece(eatenPiece, not self.activeWhitePlayer)
        

    def movePiece(self, currPiece: ChessPiece, xNewСell: int, yNewСell: int):
        '''
        Перемещение фигуры
        '''
        currPiece.setCell(xNewСell, yNewСell)

        if self.activeWhitePlayer == True:
            self.wChessBool[self.yCurСell][self.xCurСell] = False
            self.wChessBool[yNewСell][xNewСell] = True
        else:
            self.bChessBool[self.yCurСell][self.xCurСell] = False
            self.bChessBool[yNewСell][xNewСell] = True

    
    def findKing(self, isColorWhite: bool):
        '''
        Поиск короля нужного цвета
        '''
        if isColorWhite:
            for piece in self.wChessPieces:
                if piece.name == "King":
                    return piece
        else:
            for piece in self.bChessPieces:
                if piece.name == "King":
                    return piece
    

    def checkmateCheck(self, isColorWhite: bool):
        '''
        Проверка, что игроку поставили шах или мат
        '''
        king = self.findKing(isColorWhite)      
        check, checkmate = king.checkCheckmate(isColorWhite, self.wChessPieces, self.bChessPieces)

        return check, checkmate


    def playerMakesMove(self, xNewСell: int, yNewСell: int):
        '''
        Игрок делает ход
        '''
        # фигура, которая делает ход
        currPiece = self.getPiece(self.xCurСell, self.yCurСell, self.activeWhitePlayer)

        if self.checkMovement(currPiece, xNewСell, yNewСell):
            # если пытаемся съесть фигуру соперника
            if self.cellIsNotEmpty(xNewСell, yNewСell, not self.activeWhitePlayer):
                eatenPiece = self.getPiece(xNewСell, yNewСell, not self.activeWhitePlayer)
                self.eatPiece(eatenPiece)

            # перемещение фигуры
            self.movePiece(currPiece, xNewСell, yNewСell)   
            self.printChessBools()
            # ход переходит к следующему игроку
            self.activeWhitePlayer = not self.activeWhitePlayer
            self.calculateMovement()
            # проверка, что игрок поставил шах или мат
            self.check, self.checkmate = self.checkmateCheck(self.activeWhitePlayer)
        else:
            if self.activeWhitePlayer == self.mainWhiteСolor:
                messagebox.showinfo("Ошибка",
                    "Выбранная фигура не может ходить в эту клетку.")
            return False
        
        return True
            

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
                successfulMove = self.playerMakesMove(xNewСell, yNewСell)

                # не удалось походить
                if successfulMove == False:
                    self.xCurСell = EMPTY
                    self.yCurСell = EMPTY
                # игрок поставил мат
                elif self.checkmate:
                    self.xCurСell = CHECKMATE
                    self.yCurСell = CHECKMATE
                # игрок поставил шах
                elif self.check:
                    self.xCurСell = CHECK
                    self.yCurСell = CHECK
                # обычный успешных ход
                else:
                    self.xCurСell = MOVE_DONE
                    self.yCurСell = MOVE_DONE

        if self.xCurСell >= 0 and self.yCurСell >= 0:
            return self.getCurСell()
        else: 
            return [self.xCurСell, self.yCurСell]


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
            piece.calculateMovement(self.mainWhiteСolor, True,
                                    self.wChessBool, self.bChessBool)

        for piece in self.bChessPieces:
            piece.calculateMovement(self.mainWhiteСolor, False,
                                    self.wChessBool, self.bChessBool)


    def isMyMove(self):
        '''
        Проверка, что сейчас ход игрока, чьи фигуры отображены 
        внизу шахматной доски (ходить может только такой игрок)
        '''
        return self.mainWhiteСolor == self.activeWhitePlayer
    

    def printChessBools(self):
        '''
        Вывод булевых матриц расположения фигур на шахматной доске
        '''
        print("\n{:s}--- White ChessBool ---\n".format(BLUE_TERMINAL)) 
        for row in self.wChessBool:
            for elem in row:
                if elem == True:
                    print("{:s}{:6s}".format(GREEN_TERMINAL, str(elem)), end='')
                else:
                    print("{:s}{:6s}".format(RED_TERMINAL, str(elem)), end='')
            print("{:s}".format(BASE_COLOR_TERMINAL))
        
        print("\n{:s}--- Black ChessBool ---\n".format(BLUE_TERMINAL)) 
        for row in self.bChessBool:
            for elem in row:
                if elem == True:
                    print("{:s}{:6s}".format(GREEN_TERMINAL, str(elem)), end='')
                else:
                    print("{:s}{:6s}".format(RED_TERMINAL, str(elem)), end='')
            print("{:s}".format(BASE_COLOR_TERMINAL))
        print()
