"""
File: sierpinski.py
Name: Monica Peng
---------------------------
This file recursively prints the Sierpinski triangle on GWindow.
The Sierpinski triangle is a fractal described in 1915 by Waclaw Sierpinski.
It is a self similar structure that occurs at different levels of iterations.
"""

from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GLine
from campy.gui.events.timer import pause

# Constants
ORDER = 6  # Controls the order of Sierpinski Triangle
LENGTH = 600  # The length of order 1 Sierpinski Triangle
UPPER_LEFT_X = 150  # The upper left x coordinate of order 1 Sierpinski Triangle
UPPER_LEFT_Y = 100  # The upper left y coordinate of order 1 Sierpinski Triangle
WINDOW_WIDTH = 950  # The width of the GWindow
WINDOW_HEIGHT = 700  # The height of the GWindow

# Global Variable
window = GWindow(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)  # The canvas to draw Sierpinski Triangle


def main():
    """
	This program calls a recursive function that draws a number of Sierpinski Triangle
	based on the ORDER constant set above.
	"""
    sierpinski_triangle(ORDER, LENGTH, UPPER_LEFT_X, UPPER_LEFT_Y)


def sierpinski_triangle(order, length, upper_left_x, upper_left_y):
    """
	:param order: int, the order of the Sierpinski Triangle
	:param length: int, the length of the Sierpinski Triangle
	:param upper_left_x: int, the upper left x coordinate of Sierpinski Triangle
	:param upper_left_y: int, the upper left y coordinate of Sierpinski Triangle
	:return: draws the Sierpinski Triangle based on the parameters above on the canvas
	"""
    if order == 0:
        pass
    else:
        # The list contains three set of x, y coordinates for the Triangle
        tri_l = [(upper_left_x, upper_left_y),
                 (upper_left_x + length * 0.5, upper_left_y + length * 0.866),
                 (upper_left_x + length, upper_left_y)]

        # Draws three lines to form a triangle based on the coordinates above
        for i in range(3):
            line = GLine(tri_l[i][0], tri_l[i][1],
                         tri_l[(i + 1) % 3][0], tri_l[(i + 1) % 3][1])
            window.add(line)

        # The following is recursion of the triangles
        # Left
        sierpinski_triangle(order - 1, length / 2, upper_left_x, upper_left_y)
        # Right
        sierpinski_triangle(order - 1, length / 2, upper_left_x + length / 2, upper_left_y)
        # Bottom
        sierpinski_triangle(order - 1, length / 2, upper_left_x + length / 2 * 0.5, upper_left_y + length / 2 * 0.866)


if __name__ == '__main__':
    main()
