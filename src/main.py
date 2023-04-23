from window import Window
from p2p import p2pNode, p2pConnection


WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 740

CANVAS_WIDTH = WINDOW_WIDTH - 300
CANVAS_HEIGHT = WINDOW_HEIGHT


def main(): 
    colorUser = input("Выберете цвет (w or b): ")

    if colorUser == "w":
        node = p2pNode(True)
    elif colorUser == "b":
        node = p2pNode(False)
    else:
        print("Ожидался ввод 'w' или 'b'")

    node.start()
    p2pConnection(node)

    window = Window(WINDOW_WIDTH, WINDOW_HEIGHT, CANVAS_WIDTH, CANVAS_HEIGHT, node)
    window.run()

    node.stop()


if __name__ == "__main__":
    main()
