"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

Breakout is a game using the paddle to bounce off the ball to hit the bricks.
The aim is the clear all the bricks in the game.
BEWARE it gets harder in the end if you are too good.
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics
import winsound

FRAME_RATE = 10         # 100 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    graphics = BreakoutGraphics()
    lives = NUM_LIVES
    graphics.display_lives(NUM_LIVES, lives)

    # Add the animation loop here!
    while True:
        if graphics.replay:
            graphics.ball.move(graphics.get_dx(), graphics.get_dy())
            # Bounce off side walls
            if graphics.ball.x <= 0 or (graphics.ball.x + graphics.ball.width) >= graphics.window.width:
                graphics.set_dx()
                winsound.PlaySound(graphics.sound_wall_bounce, graphics.sound_play_flag)
            # Bounce off ceiling
            if graphics.ball.y <= 0:
                graphics.set_dy()
                winsound.PlaySound(graphics.sound_wall_bounce, graphics.sound_play_flag)
            # If ball falls below then minus one life
            if graphics.ball.y >= graphics.window.height:
                lives -= 1
                graphics.display_lives(NUM_LIVES, lives)
                winsound.PlaySound(graphics.sound_ball_die, graphics.sound_play_flag)
                # If there are still lives left reset the ball
                if lives > 0:
                    graphics.ball_reset()
                    graphics.ball_initialise()
                else:
                    graphics.game_over_screen()
                    # If user exit the gameover loop means restart the whole game
                    # Reset the lives back to maximum
                    lives = NUM_LIVES
                    graphics.display_lives(NUM_LIVES, lives)
                    graphics.main_game()

                graphics.replay = False

            graphics.check_collision()
            graphics.bricks_left()

            if graphics.game_win:
                graphics.game_win_screen()
                break
        pause(FRAME_RATE)


if __name__ == '__main__':
    main()
