"""
File: Draw Line
Name: Monica Peng
-------------------------
This program creates a straight line between two mouse clicks.
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

# Constant determines the size of the circle in first click
SIZE = 5

# Global variable
first_click = True
start_x = 0
start_y = 0

window = GWindow(title='Draw line')
circle = GOval(SIZE, SIZE)


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(draw)


def draw(mouse_click):
    global first_click, start_x, start_y

    if first_click:  # if it's first click, create the circle and record the x, y of mouse click
        window.add(circle, mouse_click.x - SIZE/2, mouse_click.y - SIZE/2)
        start_x = mouse_click.x
        start_y = mouse_click.y
    else:  # if it's second click, remove the circle and draw the line
        window.remove(circle)
        end_x = mouse_click.x
        end_y = mouse_click.y
        line = GLine(start_x, start_y, end_x, end_y)
        window.add(line)

    # flip the first click into second click and vice versa
    first_click = not first_click


if __name__ == "__main__":
    main()
