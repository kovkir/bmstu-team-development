from p2p import p2pNode, p2pConnection
from window import Window
from constants import *


def getDefaultHost():
    strDefaultHost = input("\nИграть на разных устройствах в локальной сети? (y or N): ")

    if strDefaultHost == "y":
        defaultHost = False
    else:
        defaultHost = True

    return defaultHost


def getP2PNode(defaultHost: bool):
    colorUser = input("Выберете цвет (w or b): ")

    if colorUser == "w":
        node = p2pNode(whiteСolor=True, defaultHost=defaultHost)
    elif colorUser == "b":
        node = p2pNode(whiteСolor=False, defaultHost=defaultHost)
    else:
        print("\nОшибка! Ожидался ввод 'w' или 'b'.\n")
        node = None

    return node


def main(): 
    defaultHost = getDefaultHost()
    node = getP2PNode(defaultHost)
    if node == None:
        return
    
    node.start()
    status = p2pConnection(node, defaultHost)
    if status == False:
        node.stop()
        return

    window = Window(WINDOW_WIDTH, WINDOW_HEIGHT, CANVAS_WIDTH, CANVAS_HEIGHT, node)
    window.run()

    node.stop()


if __name__ == "__main__":
    main()
