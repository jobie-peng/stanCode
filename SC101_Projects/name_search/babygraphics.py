"""
File: babygraphics.py
Name: 
--------------------------------
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950,
         1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['#59c7eb', '#ffb8ac', '#09a398', '#eca0b2', '#b8bcc1']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index where the current year is in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                            with the current year.
    """
    return GRAPH_MARGIN_SIZE + year_index * ((width - GRAPH_MARGIN_SIZE * 2) // len(YEARS))


def draw_fixed_lines(canvas):
    """
    Draws the fixed background lines on the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # ----- Write your code below this line ----- #

    # Create a top and bottom line
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE,
                       CANVAS_WIDTH - GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE)

    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE,
                       CANVAS_WIDTH - GRAPH_MARGIN_SIZE, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE)

    # Create each vertical line for each year and put the year text at the bottom
    for i in range(len(YEARS)):
        x_pos = get_x_coordinate(CANVAS_WIDTH, i)
        canvas.create_line(x_pos, 0, x_pos, CANVAS_HEIGHT)
        canvas.create_text(x_pos + TEXT_DX, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, text=YEARS[i], anchor=tkinter.NW)


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid

    # ----- Write your code below this line ----- #

    draw_area = CANVAS_HEIGHT - 2 * GRAPH_MARGIN_SIZE

    for i in range(len(lookup_names)):
        line_color = COLORS[i % len(COLORS)]         # Define the line color
        name = lookup_names[i]

        for j in range(len(YEARS)):
            # Retrieve the first set of (x, y)
            year1 = str(YEARS[j])
            x0 = get_x_coordinate(CANVAS_WIDTH, j)
            if year1 not in name_data[name] or int(name_data[name][year1]) > MAX_RANK:
                y0 = MAX_RANK / MAX_RANK * draw_area + GRAPH_MARGIN_SIZE
                rank = '*'
            else:
                y0 = int(name_data[name][year1]) / MAX_RANK * draw_area + GRAPH_MARGIN_SIZE
                rank = name_data[name][year1]

            # Retrieve the second set of (x, y) only if we are not in the last year of the list
            if j < len(YEARS) - 1:
                x1 = get_x_coordinate(CANVAS_WIDTH, j+1)
                year2 = str(YEARS[j+1])
                if year2 not in name_data[name] or int(name_data[name][year2]) > MAX_RANK:
                    y1 = MAX_RANK / MAX_RANK * draw_area + GRAPH_MARGIN_SIZE
                else:
                    y1 = int(name_data[name][year2]) / MAX_RANK * draw_area + GRAPH_MARGIN_SIZE

                canvas.create_line(x0, y0, x1, y1, width=LINE_WIDTH, fill=line_color)
            canvas.create_text(x0 + TEXT_DX, y0, text=name + " " + rank, anchor=tkinter.SW, fill=line_color)


# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names Ranking by Year')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
