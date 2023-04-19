from window import Window


WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 740

CANVAS_WIDTH = WINDOW_WIDTH - 300
CANVAS_HEIGHT = WINDOW_HEIGHT


def main(): 
    window = Window(WINDOW_WIDTH, WINDOW_HEIGHT, CANVAS_WIDTH, CANVAS_HEIGHT)
    window.run()


if __name__ == "__main__":
    main()
