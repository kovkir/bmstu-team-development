from tkinter import Tk, Canvas, Label, Entry, Button, Radiobutton, \
    messagebox, BooleanVar, DISABLED, NORMAL, END

from chess import Chess, EMPTY, MOVE_DONE
from color import *


class Window():
    window: Tk
    canvas: Canvas
    canvasWidth: int
    canvasHeight: int

    xEntry: Entry
    yEntry: Entry

    wPawnEntry: Entry
    wHorseEntry: Entry
    wElephantEntry: Entry
    wRookEntry: Entry
    wQueenEntry: Entry

    bPawnEntry: Entry
    bHorseEntry: Entry
    bElephantEntry: Entry
    bRookEntry: Entry
    bQueenEntry: Entry

    colorVar: BooleanVar

    chess: Chess


    def __init__(self, windowWidth: int, windowHeight: int, 
                       canvasWidth: int, canvasHeight: int):
        self.window = self.createWindow(windowWidth, windowHeight)
        self.canvas = self.createCanvas(canvasWidth, canvasHeight)
        self.canvasWidth = canvasWidth
        self.canvasHeight = canvasHeight

        self.createInterface(canvasWidth, True)
        self.chess = Chess(self.canvas, canvasWidth, canvasHeight, True)
        self.fillEntries()


    def createWindow(self, windowWidth: int, windowHeight: int):
        window = Tk()
        window.title("Пиринговое приложение для игры в шахматы")
        window.geometry("{0}x{1}".format(windowWidth, windowHeight))
        window.resizable(False, False)
        window["bg"] = PURPLE_LIGHT

        return window


    def createCanvas(self, canvasWidth: int, canvasHeight: int):
        canvas = Canvas(self.window, width = canvasWidth, height = canvasHeight, bg = "white")
        canvas.place(x = 0, y = 0)

        return canvas


    def aboutProgram(self):
        messagebox.showinfo("О программе",
            "Пиринговое приложение для игры в шахматы.\n\n"
            "Разработчики:\n"
            "   1) Волков Михаил  ИУ7-83Б;\n"
            "   2) Кишов Гаджи    ИУ7-83Б;\n"
            "   3) Ковалец Кирилл ИУ7-83Б;\n"
            "   4) Криков Антон   ИУ7-83Б."
        )


    def createInterface(self, canvasWidth: int, mainWhiteСolor: bool):
        Label(text = "ВЫБРАННАЯ ФИГУРА", font = ("Arial", 16, "bold"), bg = PURPLE_DARK,
            fg = "white").place(width = 295, height = 30, x = canvasWidth + 6 , y = 0)

        Label(text = "X\t\tY", font = ("Arial", 16), bg = PURPLE_LIGHT,
            fg = PURPLE_SUPER_DARK).place(width = 250, height = 20, x = canvasWidth + 30, y = 40)

        self.xEntry = Entry(font = ("Arial", 17), state = DISABLED)
        self.xEntry.place(width = 125, height = 30, x = canvasWidth + 30, y = 70)
        
        self.yEntry = Entry(font = ("Arial", 17), state = DISABLED)
        self.yEntry.place(width = 125, height = 30, x = canvasWidth + 155, y = 70)


        Label(text = "БЕЛЫЕ", font = ("Arial", 16, "bold"), bg = PURPLE_DARK,
            fg = "white").place(width = 295, height = 30, x = canvasWidth + 6, y = 110)

        Label(text = "Пешка - ", font = ("Arial", 16), bg = PURPLE_LIGHT,
            fg = PURPLE_SUPER_DARK).place(width = 150, height = 30, x = canvasWidth + 6, y = 150)

        self.wPawnEntry = Entry(font = ("Arial", 17))
        self.wPawnEntry.place(width = 125, height = 30, x = canvasWidth + 155, y = 150)

        Label(text = "Конь - ", font = ("Arial", 16), bg = PURPLE_LIGHT,
            fg = PURPLE_SUPER_DARK).place(width = 150, height = 30, x = canvasWidth + 6, y = 180)

        self.wHorseEntry = Entry(font = ("Arial", 17))
        self.wHorseEntry.place(width = 125, height = 30, x = canvasWidth + 155, y = 180)

        Label(text = "Слон - ", font = ("Arial", 16), bg = PURPLE_LIGHT,
            fg = PURPLE_SUPER_DARK).place(width = 150, height = 30, x = canvasWidth + 6, y = 210)

        self.wElephantEntry = Entry(font = ("Arial", 17))
        self.wElephantEntry.place(width = 125, height = 30, x = canvasWidth + 155, y = 210)

        Label(text = "Ладья - ", font = ("Arial", 16), bg = PURPLE_LIGHT,
            fg = PURPLE_SUPER_DARK).place(width = 150, height = 30, x = canvasWidth + 6, y = 240)

        self.wRookEntry = Entry(font = ("Arial", 17))
        self.wRookEntry.place(width = 125, height = 30, x = canvasWidth + 155, y = 240)

        Label(text = "Ферзь - ", font = ("Arial", 16), bg = PURPLE_LIGHT,
            fg = PURPLE_SUPER_DARK).place(width = 150, height = 30, x = canvasWidth + 6, y = 270)

        self.wQueenEntry = Entry(font = ("Arial", 17))
        self.wQueenEntry.place(width = 125, height = 30, x = canvasWidth + 155, y = 270)



        Label(text = "ЧЕРНЫЕ", font = ("Arial", 16, "bold"), bg = PURPLE_DARK,
            fg = "white").place(width = 295, height = 30, x = canvasWidth + 6 , y = 340)

        Label(text = "Пешка - ", font = ("Arial", 16), bg = PURPLE_LIGHT,
            fg = PURPLE_SUPER_DARK).place(width = 150, height = 30, x = canvasWidth + 6, y = 380)

        self.bPawnEntry = Entry(font = ("Arial", 17))
        self.bPawnEntry.place(width = 125, height = 30, x = canvasWidth + 155, y = 380)

        Label(text = "Конь - ", font = ("Arial", 16), bg = PURPLE_LIGHT,
            fg = PURPLE_SUPER_DARK).place(width = 150, height = 30, x = canvasWidth + 6, y = 410)

        self.bHorseEntry = Entry(font = ("Arial", 17))
        self.bHorseEntry.place(width = 125, height = 30, x = canvasWidth + 155, y = 410)

        Label(text = "Слон - ", font = ("Arial", 16), bg = PURPLE_LIGHT,
            fg = PURPLE_SUPER_DARK).place(width = 150, height = 30, x = canvasWidth + 6, y = 440)

        self.bElephantEntry = Entry(font = ("Arial", 17))
        self.bElephantEntry.place(width = 125, height = 30, x = canvasWidth + 155, y = 440)

        Label(text = "Ладья - ", font = ("Arial", 16), bg = PURPLE_LIGHT,
            fg = PURPLE_SUPER_DARK).place(width = 150, height = 30, x = canvasWidth + 6, y = 470)

        self.bRookEntry = Entry(font = ("Arial", 17))
        self.bRookEntry.place(width = 125, height = 30, x = canvasWidth + 155, y = 470)

        Label(text = "Ферзь - ", font = ("Arial", 16), bg = PURPLE_LIGHT,
            fg = PURPLE_SUPER_DARK).place(width = 150, height = 30, x = canvasWidth + 6, y = 500)

        self.bQueenEntry = Entry(font = ("Arial", 17))
        self.bQueenEntry.place(width = 125, height = 30, x = canvasWidth + 155, y = 500)



        Label(text = "ВЫБОР ЦВЕТА", font = ("Arial", 16, "bold"), bg = PURPLE_DARK,
            fg = "white").place(width = 295, height = 30, x = canvasWidth + 6 , y = 570)

        self.colorVar = BooleanVar()
        self.colorVar.set(mainWhiteСolor)

        colorRadiobutton = Radiobutton(
            text = "Белый", 
            variable = self.colorVar, value = True,
            font = ("Arial", 16), bg = PURPLE_LIGHT, fg = PURPLE_SUPER_DARK, anchor = "w",
            command = lambda : self.changeСolorСhessPieces())
        colorRadiobutton.place(width = 150, height = 30, x = canvasWidth + 30, y = 610)

        colorRadiobutton = Radiobutton(
            text = "Черный", 
            variable = self.colorVar, value = False,
            font = ("Arial", 16), bg = PURPLE_LIGHT, fg = PURPLE_SUPER_DARK, anchor = "w",
            command = lambda : self.changeСolorСhessPieces())
        colorRadiobutton.place(width = 150, height = 30, x = canvasWidth + 155, y = 610)



        Label(text = "О ПРОГРАММЕ", font = ("Arial", 16, "bold"), bg = PURPLE_DARK,
            fg = "white").place(width = 295, height = 30, x = canvasWidth + 6 , y = 650)

        # Эта кнопка имитирует границы кнопки infoButton
        Button(highlightbackground = PURPLE_DARK, highlightthickness = 30, state = DISABLED).\
            place(width = 250, height = 30,  x = canvasWidth + 30, y = 695)

        infoButton = Button(
            text = "Информация о программе", font = ("Arial", 16), 
            highlightbackground = PURPLE, highlightthickness = 30, fg = PURPLE_SUPER_DARK,
            command = lambda: self.aboutProgram())
        infoButton.place(width = 246, height = 26,  x = canvasWidth + 32, y = 697)



    def blockEntriesFigures(self, status):
        self.wPawnEntry.config(state = status)
        self.wHorseEntry.config(state = status)
        self.wElephantEntry.config(state = status)
        self.wRookEntry.config(state = status)
        self.wQueenEntry.config(state = status)

        self.bPawnEntry.config(state = status)
        self.bHorseEntry.config(state = status)
        self.bElephantEntry.config(state = status)
        self.bRookEntry.config(state = status)
        self.bQueenEntry.config(state = status)


    def clearEntries(self):
        self.wPawnEntry.delete(0, END)
        self.wHorseEntry.delete(0, END)
        self.wElephantEntry.delete(0, END)
        self.wRookEntry.delete(0, END)
        self.wQueenEntry.delete(0, END)

        self.bPawnEntry.delete(0, END)
        self.bHorseEntry.delete(0, END)
        self.bElephantEntry.delete(0, END)
        self.bRookEntry.delete(0, END)
        self.bQueenEntry.delete(0, END)


    def fillEntries(self):
        self.blockEntriesFigures(NORMAL)
        self.clearEntries()

        self.wPawnEntry.insert(    0, self.chess.deletedPieces["wPawn"])
        self.wHorseEntry.insert(   0, self.chess.deletedPieces["wHorse"])
        self.wElephantEntry.insert(0, self.chess.deletedPieces["wElephant"])
        self.wRookEntry.insert(    0, self.chess.deletedPieces["wRook"])
        self.wQueenEntry.insert(   0, self.chess.deletedPieces["wQueen"])

        self.bPawnEntry.insert(    0, self.chess.deletedPieces["bPawn"])
        self.bHorseEntry.insert(   0, self.chess.deletedPieces["bHorse"])
        self.bElephantEntry.insert(0, self.chess.deletedPieces["bElephant"])
        self.bRookEntry.insert(    0, self.chess.deletedPieces["bRook"])
        self.bQueenEntry.insert(   0, self.chess.deletedPieces["bQueen"])

        self.blockEntriesFigures(DISABLED)

    
    def clearXYEntry(self):
        self.xEntry.config(state = NORMAL)
        self.yEntry.config(state = NORMAL)

        self.xEntry.delete(0, END)
        self.yEntry.delete(0, END)

        self.xEntry.config(state = DISABLED)
        self.yEntry.config(state = DISABLED)


    def fillXYEntry(self, x, y):
        self.xEntry.config(state = NORMAL)
        self.yEntry.config(state = NORMAL)

        self.xEntry.insert(0, x)
        self.yEntry.insert(0, y)

        self.xEntry.config(state = DISABLED)
        self.yEntry.config(state = DISABLED)


    def chooseCell(self, xEvent, yEvent):
        xCell, yCell = self.chess.chooseСell(xEvent, yEvent)

        if xCell == EMPTY:
            # игрок тыкнул вне доски
            self.cancelChooseCell()
        elif xCell == MOVE_DONE:
            # игрок сделал ход
            self.cancelChooseCell()
            self.chess.drawChessBoard()
            self.chess.drawChessPieces()
            self.fillEntries()
        else:
            # нажали на фигуру ходящего игрока
            self.clearXYEntry()
            self.fillXYEntry(xCell, yCell)


    def cancelChooseCell(self):
        self.chess.cancelChooseCell()
        self.clearXYEntry()


    def chooseCellEvent(self, event):
        if self.chess.isMyMove():
            x = event.x
            y = event.y

            self.chooseCell(x, y)


    def cancelChooseCellEvent(self):
        if self.chess.isMyMove():
            self.cancelChooseCell()


    def changeСolorСhessPieces(self):
        self.clearXYEntry()

        self.chess.flipChessBoard(self.colorVar.get())
        self.chess.drawChessBoard()
        self.chess.drawChessPieces()


    def run(self):
        self.chess.drawChessBoard()
        self.chess.drawChessPieces()

        self.canvas.bind('<1>', # левая кнопка мыши
            lambda event: self.chooseCellEvent(event))

        self.canvas.bind('<2>', # правая кнопка мыши 
            lambda event: self.cancelChooseCellEvent())
        
        self.window.mainloop()
