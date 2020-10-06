import tkinter

class SevenSegment:

    TOP = ((10, 0), (40, 0), (40, 10), (10, 10))
    MIDDLE = ((10, 40), (40, 40), (40, 50), (10, 50))
    BOTTOM = ((10, 80), (40, 80), (40, 90), (10, 90))
    LEFT_TOP = ((0, 10), (10, 10), (10, 40), (0, 40))
    LEFT_BOTTOM = ((0, 50), (10, 50), (10, 80), (0, 80))
    RIGHT_TOP = ((40, 10), (50, 10), (50, 40), (40, 40))
    RIGHT_BOTTOM = ((40, 50), (50, 50), (50, 80), (40, 80))

    def __init__(self, tk, x_offset = 0, y_offset = 0, scale = 1):
        self.root = tk



    def display(self):
        canvas = tkinter.Canvas(self.root, width=500, height=500)
        canvas.create_polygon(self.TOP, fill="#000000")
        canvas.create_polygon(self.MIDDLE, fill="#000000")
        canvas.create_polygon(self.BOTTOM, fill="#000000")
        canvas.create_polygon(self.LEFT_TOP, fill="#000000")
        canvas.create_polygon(self.LEFT_BOTTOM, fill="#000000")
        canvas.create_polygon(self.RIGHT_TOP, fill="#000000")
        canvas.create_polygon(sel