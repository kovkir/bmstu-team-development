from p2pnetwork.node import Node
import time


HOST = 'localhost'
PORT_FOR_WHITE = 8000
PORT_FOR_BLACK = 9000


def p2pNode(whiteСolor: bool):
    if whiteСolor:
        port = PORT_FOR_WHITE
    else:
        port = PORT_FOR_BLACK

    try:
        node = MyOwnPeer2PeerNode(HOST, port, mainWhiteСolor=whiteСolor)
    except:
        print("\n{} цвет уже занят, вам придется играть за {} :)\n".format(
            "Белый"  if whiteСolor else "Черный",
            "Черных" if whiteСolor else "Белых"
        ))
        node = p2pNode(not whiteСolor)

    return node


def p2pConnection(node: Node):
    print("Ожидание соперника...")
    if node.mainWhiteСolor:
        while node.connect_with_node(HOST, PORT_FOR_BLACK) == False:
            time.sleep(1)
    

class MyOwnPeer2PeerNode (Node):
    mainWhiteСolor: bool
    namePlayer: str

    def __init__(self, host, port, id = None, callback = None, 
                       max_connections = 0, mainWhiteСolor = True):

        super(MyOwnPeer2PeerNode, self).__init__(host, port, id, callback, max_connections)

        self.mainWhiteСolor = mainWhiteСolor

        if mainWhiteСolor:
            self.namePlayer = "First Player"
        else:
            self.namePlayer = "Second Player"


    def node_message(self, connected_node, data):
        print("node_message from " + self.namePlayer)
        print("x = {}, y = {}".format(data['xEvent'], data['yEvent']))

        self.window.chooseCell(data['xEvent'], data['yEvent'])


    def myInit(self, window):
        self.window = window


    def sendXYEvent(self, x, y):
        data = {'xEvent': x, 'yEvent': y}
        self.send_to_nodes(data)
