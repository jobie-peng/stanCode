"""
File: Bouncing Ball
Name: Monica Peng
-------------------------
This program simulates the process of a bouncing ball.
If the bouncing ball falls out of the screen, the ball returns to its start position.
After 3 tries, the ball does not move anymore.
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40

window = GWindow(800, 500, title='bouncing_ball.py')
ball = GOval(SIZE, SIZE)
replay = True

# Global variable
num_tries = 3


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    # display the ball on the window
    ball.filled = True
    ball.fill_color = 'turquoise'
    ball.color = 'turquoise'
    window.add(ball, START_X, START_Y)

    onmouseclicked(balldrop)


def balldrop(event):
    global num_tries, replay

    """
    On mouse clicks, it plays the animation of bouncing ball.
    However, it only plays the animation if both conditions are satisfied:
    1. Number of tries > 0.
    2. The ball is at its original starting position.
    """

    if num_tries > 0 and window.get_object_at(START_X, START_Y) is not None:
        # replay = not replay  # set the replay to false as soon as the ball starts dropping
        num_tries -= 1  # Reduce number of tries by 1

        vy = 1  # Set the initial velocity

        while True:
            ball.move(VX, vy)
            vy += GRAVITY  # Increase the velocity by gravity for each loop
            if ball.y + SIZE >= window.height:  # if the ball hits the ground
                vy = -vy * REDUCE  # Set the bounce
            if ball.x + SIZE >= window.width + SIZE:  # if the ball falls out of screen
                window.add(ball, START_X, START_Y)  # return ball to original position
                replay = not replay  # reset the replay value to true for the next iteration
                break
            pause(DELAY)


if __name__ == "__main__":
    main()
