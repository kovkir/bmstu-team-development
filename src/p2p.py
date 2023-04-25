import time
import subprocess
from p2pnetwork.node import Node

from constants import *


def getHost(defaultHost: bool):
    if defaultHost:
        host = HOST_DEFAULT
    else:
        cmd = open('../getIPcmd.txt', 'r').read()
        host = subprocess.getoutput(cmd)

    print("Ваш IP: {}\n".format(host))
    return host


def getPort(whiteСolor: bool):
    if whiteСolor:
        port = PORT_FOR_WHITE
    else:
        port = PORT_FOR_BLACK

    return port


def p2pNode(whiteСolor: bool, defaultHost: bool, reconnecting=False):
    host = getHost(defaultHost)
    port = getPort(whiteСolor)

    try:
        node = MyOwnPeer2PeerNode(host, port, mainWhiteСolor=whiteСolor)
    except:
        if reconnecting == False:
            print("\nОшибка!\nПохоже {} цвет уже занят, вам придется играть за {} :)".format(
                "белый"  if whiteСolor else "черный",
                "черных" if whiteСolor else "белых"
            ))
            node = p2pNode(not whiteСolor, defaultHost, reconnecting=True)
        else:
            print("\nПовторная ошибка! :(\n")
            return None

    return node


def p2pConnection(node: Node, defaultHost: bool):
    print("Ожидание соперника...\n")
    status = True

    if node.mainWhiteСolor:
        if defaultHost:
            while node.connect_with_node(HOST_DEFAULT, PORT_FOR_BLACK) == False:
                time.sleep(1)
        else:
            host = input("Введите IP вашего соперника: ")
            status = node.connect_with_node(host, PORT_FOR_BLACK)
            if status == False:
                print("Ошибка подключения!\n")

    return status


class MyOwnPeer2PeerNode (Node):
    mainWhiteСolor: bool
    namePlayer: str

    def __init__(self, host, port, id = None, callback = None, 
                       max_connections = 0, mainWhiteСolor = True):

        super(MyOwnPeer2PeerNode, self).__init__(host, port, id, callback, max_connections)

        self.mainWhiteСolor = mainWhiteСolor

        if mainWhiteСolor:
            self.namePlayer = "White Player"
        else:
            self.namePlayer = "Black Player"


    def node_message(self, connected_node, data):
        print("node_message from " + self.namePlayer)
        print("x = {}, y = {}".format(data['xEvent'], data['yEvent']))

        self.window.chooseCell(data['xEvent'], data['yEvent'])


    def myInit(self, window):
        self.window = window


    def sendXYEvent(self, x, y):
        data = {'xEvent': x, 'yEvent': y}
        self.send_to_nodes(data)
