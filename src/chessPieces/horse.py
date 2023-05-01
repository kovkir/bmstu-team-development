from tkinter import Canvas
from chessPieces.chessPiece import ChessPiece


class Horse(ChessPiece):
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

    def __init__(self, canvas: Canvas,
                 sizeCell: int, xLeftChessBoard: int, yTopChessBoard: int,
                 name: str, color: str, xCell: int, yCell: int):
        super().__init__(canvas, sizeCell, xLeftChessBoard, yTopChessBoard,
                         name, color, xCell, yCell)
        self.movement = list()

    def drawPiece(self):
        self.drawHorse(self.xLeftChessBoard + self.xCell * self.sizeCell,
                       self.yTopChessBoard + self.yCell * self.sizeCell)

    def drawHorse(self, x, y):
        # подставка коня
        self.canvas.create_rectangle(
            x + self.sizeCell * 0.2, y + self.sizeCell * 0.75,
            x + self.sizeCell * 0.8, y + self.sizeCell * 0.87,
            outline=self.colorBorder, fill=self.color, width=2
        )

        # тело коня
        self.canvas.create_polygon(
            [x + self.sizeCell * 0.3,  y + self.sizeCell * 0.75,
             x + self.sizeCell * 0.32, y + self.sizeCell * 0.6,
             x + self.sizeCell * 0.43, y + self.sizeCell * 0.53,
             x + self.sizeCell * 0.46, y + self.sizeCell * 0.42,
             x + self.sizeCell * 0.2,  y + self.sizeCell * 0.5,
             x + self.sizeCell * 0.15, y + self.sizeCell * 0.38,
             x + self.sizeCell * 0.4,  y + self.sizeCell * 0.18,
             x + self.sizeCell * 0.47, y + self.sizeCell * 0.1,
             x + self.sizeCell * 0.6,  y + self.sizeCell * 0.15,
             x + self.sizeCell * 0.75, y + self.sizeCell * 0.19,
             x + self.sizeCell * 0.8,  y + self.sizeCell * 0.3,
             x + self.sizeCell * 0.82, y + self.sizeCell * 0.5,
             x + self.sizeCell * 0.7,  y + self.sizeCell * 0.6,
             x + self.sizeCell * 0.7,  y + self.sizeCell * 0.75
             ],
            outline=self.colorBorder, fill=self.color, width=2
        )

        # глаз коня
        self.canvas.create_line(
            x + self.sizeCell * 0.43, y + self.sizeCell * 0.28,
            x + self.sizeCell * 0.5,  y + self.sizeCell * 0.26,
            fill=self.colorBorder, width=2
        )

    # нахождение списка всех возможных ходов коня
    def calculateMovement(self, mainWhiteСolor: bool, isColorWhite: bool,
                          wChessBool: list, bChessBool: list):
        self.movement.clear()

        if isColorWhite:
            myChessBool = wChessBool
        else:
            myChessBool = bChessBool

        # добавление ходов вверх (i = -1) или вниз (i = 1)
        for i in range(-1, 2, 2):
            # вертикальная буква Г (повернута направо)
            y = self.yCell + 2 * i
            x = self.xCell + 1

            if y >= 0 and y <= 7 and x <= 7 and not myChessBool[y][x]:
                self.movement.append([x, y])

            # вертикальная буква Г (повернута налево)
            y = self.yCell + 2 * i
            x = self.xCell - 1

            if y >= 0 and y <= 7 and x >= 0 and not myChessBool[y][x]:
                self.movement.append([x, y])

            # горизонтальная буква Г (повернута направо)
            y = self.yCell + i
            x = self.xCell + 2

            if y >= 0 and y <= 7 and x <= 7 and not myChessBool[y][x]:
                self.movement.append([x, y])

            # горизонтальная буква Г (повернута налево)
            y = self.yCell + i
            x = self.xCell - 2

            if y >= 0 and y <= 7 and x >= 0 and not myChessBool[y][x]:
                self.movement.append([x, y])

        return self.movement
