from p2p import p2pNode, p2pConnection
from window import Window
from constants import *
from color import *


def getDefaultHost():
    strDefaultHost = input(
        "\nИграть на разных устройствах в локальной сети? ({:s}y{:s} or {:s}N{:s}): "
            .format(PURPLE_TERMINAL, BASE_COLOR_TERMINAL, PURPLE_TERMINAL, BASE_COLOR_TERMINAL))

    if strDefaultHost == "y":
        defaultHost = False
    else:
        defaultHost = True

    return defaultHost


def getP2PNode(defaultHost: bool):
    colorUser = input(
        "Выберете цвет ({:s}w{:s} or {:s}b{:s}): "
            .format(PURPLE_TERMINAL, BASE_COLOR_TERMINAL, PURPLE_TERMINAL, BASE_COLOR_TERMINAL))

    if colorUser == "w":
        node = p2pNode(whiteСolor=True, defaultHost=defaultHost)
    elif colorUser == "b":
        node = p2pNode(whiteСolor=False, defaultHost=defaultHost)
    else:
        print("\n{:s}Ошибка!{:s} Ожидался ввод 'w' или 'b'.\n"
            .format(RED_TERMINAL, BASE_COLOR_TERMINAL))
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
