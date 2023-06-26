"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

This program controls all the graphics and mechanism of the breakout game.
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
from campy.gui.events.timer import pause
from campy.graphics.gimage import GImage
import keyboard
import winsound
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Width of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10        # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75     # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball
FRAME_RATE = 60       # Control the flash of the starting prompt
SPEED_UP_THRESHOLD = BRICK_COLS * BRICK_ROWS // 3     # Control when the game is sped up


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        # Define the variables
        # Setting variables
        self.paddle_offset = paddle_offset
        self.brick_rows = brick_rows
        self.brick_cols = brick_cols
        self.brick_width = brick_width
        self.brick_height = brick_height
        self.brick_offset = brick_offset
        self.brick_spacing = brick_spacing

        # Speed variables
        self.__dx = 0
        self.__dy = 0
        # Number of bricks used in game
        self.num_bricks = brick_cols * brick_rows

        # Define colors used in game here
        self.brick_color = ['#92dad9', '#dcebeb', '#f7e2e1', '#eca4a4', '#ac6869']
        self.ball_n_paddle_color = 'dark grey'
        self.orange_title_color = '#f3b46c'
        self.brick_count_color = '#da949c'
        self.win_bg_color = '#d3e1e1'

        # Define sound related path and switches
        self.sound_play_flag = winsound.SND_ASYNC
        self.sound_paddle_bounce = 'sounds/paddle_bounce.wav'
        self.sound_wall_bounce = 'sounds/wall_bounce.wav'
        self.sound_brick_bounce = 'sounds/brick_bounce.wav'
        self.sound_ball_die = 'sounds/ball_die.wav'
        self.sound_game_start = 'sounds/game_start.wav'
        self.sound_game_over = 'sounds/game_over.wav'
        self.sound_gameover_screen = 'sounds/game_over_screen.wav'
        self.sound_game_win = 'sounds/game_win.wav'
        self.sound_game_win_screen = 'sounds/game_win_screen.wav'
        self.sound_hurry_up = 'sounds/hurry_up.wav'

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create necessary objects for the main game
        self.paddle = GRect(paddle_width, paddle_height)
        self.ball = GOval(ball_radius * 2, ball_radius * 2)
        self.brick = GRect(self.brick_width, self.brick_height)

        # Define boolean switches
        self.replay = False
        self.game_over = False
        self.game_win = False
        self.brick_left_toggle = False

        # Create a starting screen that covers the play section first
        self.background = GRect(self.window.width, self.window.height)
        self.game_title = GLabel('BREAKOUT')
        self.game_subtitle = GLabel('S I M P L E .  B U T  A D D I C T I V E .')
        self.op_brick1 = GRect(BRICK_WIDTH * 2, BRICK_HEIGHT * 2)
        self.op_brick2 = GRect(BRICK_WIDTH * 2, BRICK_HEIGHT * 2)
        self.op_brick3 = GRect(BRICK_WIDTH * 2, BRICK_HEIGHT * 2)
        self.op_brick4 = GRect(BRICK_WIDTH * 2, BRICK_HEIGHT * 2)
        self.op_brick5 = GRect(BRICK_WIDTH * 2, BRICK_HEIGHT * 2)
        self.op_brick6 = GRect(BRICK_WIDTH * 2, BRICK_HEIGHT * 2)
        self.op_ball = GOval(BALL_RADIUS * 2 * 2, BALL_RADIUS * 2 * 2)
        self.op_paddle = GRect(PADDLE_WIDTH * 1.5, PADDLE_HEIGHT / 1.5)
        self.op_prompt = GLabel('P R E S S  S P A C E  T O  S T A R T')

        # Create a starting screen
        self.starting_screen()
        # Loop over to flash the label and break the loop when user press space
        while True:
            # If space is pressed, start the game by breaking the loop
            if keyboard.is_pressed('space'):
                break
            pause(FRAME_RATE)
            self.op_prompt.color = 'white'
            pause(FRAME_RATE)
            self.op_prompt.color = 'black'

        # Remove starting screen
        self.window.clear()
        winsound.PlaySound(self.sound_game_start, self.sound_play_flag)

        # Game End screen items
        self.gameover_title = GLabel('')
        self.gameover_pic = GImage('pics/lose.jpg')
        self.gameover_quote = GLabel('')
        self.gameover_prompt = GLabel('P R E S S  S P A C E  T O  R E T R Y')
        self.game_win_pic = GImage('pics/win.jpg')

        # Define other items
        self.heart_offset = 5  # Space offset for hearts display

        self.brick_left_display = GLabel('Bricks Left: ')
        self.brick_left_display.font = 'Corbel-14'
        self.brick_left_count = GLabel('')

        self.speed_up = GLabel('SPEED UP!')

        # Initialize our mouse listeners
        onmousemoved(self.mouse_move)
        onmouseclicked(self.mouse_click)

        # Display main game area
        self.main_game()

    def main_game(self):
        # Create the main game area
        # Reset the boolean switches and bricks number
        self.game_over = False
        self.brick_left_toggle = False
        self.num_bricks = self.brick_rows * self.brick_cols

        # Display the main game items
        # Display a paddle
        self.paddle.filled = True
        self.paddle.color = self.ball_n_paddle_color
        self.paddle.fill_color = self.ball_n_paddle_color
        self.window.add(self.paddle, x=(self.window.width - self.paddle.width)/2,
                        y=self.window.height - self.paddle.height - self.paddle_offset)

        # Center a filled ball in the graphical window
        self.ball.filled = True
        self.ball.color = self.ball_n_paddle_color
        self.ball.fill_color = self.ball_n_paddle_color
        self.ball_reset()

        # Default initial velocity for the ball
        self.ball_initialise()

        # Add other items
        self.brick_left_count.text = self.num_bricks
        self.brick_left_count.font = 'Arial Rounded MT Bold-18'
        self.brick_left_count.color = 'black'
        self.window.add(self.brick_left_display, 5, self.window.height-5)
        self.window.add(self.brick_left_count, self.brick_left_display.x + self.brick_left_display.width,
                        self.brick_left_display.y)

        # Draw bricks
        for i in range(self.brick_rows):
            for j in range(self.brick_cols):
                self.brick = GRect(self.brick_width, self.brick_height)
                self.brick.filled = True
                self.brick.fill_color = self.brick_color[i // 2]
                self.brick.color = self.brick_color[i // 2]
                self.window.add(self.brick, x=j * (self.brick_width + self.brick_spacing),
                                y=self.brick_offset + i * (self.brick_height + self.brick_spacing))

    def starting_screen(self):
        # Create the starting screen
        # Background
        self.background.filled = True
        self.background.color = 'white'
        self.background.fill_color = 'white'
        self.window.add(self.background)

        # Title
        self.game_title.font = 'Arial Rounded MT Bold-40'
        self.window.add(self.game_title, (self.window.width - self.game_title.width)/2,
                        self.window.height/2 + self.game_title.height + 50)

        # Subtitle
        self.game_subtitle.font = 'Corbel-14'
        self.window.add(self.game_subtitle, (self.window.width - self.game_subtitle.width)/2,
                        self.game_title.y + self.game_subtitle.height)

        # Bricks
        three_bricks_width = self.op_brick1.width * 3 + BRICK_SPACING * 2
        self.op_brick1.filled = True
        self.op_brick2.filled = True
        self.op_brick3.filled = True
        self.op_brick4.filled = True
        self.op_brick5.filled = True
        self.op_brick6.filled = True

        self.window.add(self.op_brick1, (self.window.width - three_bricks_width)/2, 150)
        self.window.add(self.op_brick2, self.op_brick1.x + self.op_brick1.width + BRICK_SPACING,
                        self.op_brick1.y)
        self.window.add(self.op_brick3, self.op_brick2.x + self.op_brick2.width + BRICK_SPACING,
                        self.op_brick1.y)
        self.window.add(self.op_brick4, self.op_brick1.x,
                        self.op_brick1.y + self.op_brick1.height + BRICK_SPACING)
        self.window.add(self.op_brick5, self.op_brick2.x,
                        self.op_brick2.y + self.op_brick2.height + BRICK_SPACING)
        self.window.add(self.op_brick6, self.op_brick3.x,
                        self.op_brick3.y + self.op_brick3.height + BRICK_SPACING)

        # Ball & Paddle
        self.op_ball.filled = True
        self.window.add(self.op_ball, (self.window.width - self.op_ball.width)/2,
                        self.op_brick4.y + 75)

        self.op_paddle.filled = True
        self.window.add(self.op_paddle, (self.window.width - self.op_paddle.width)/2,
                        self.op_ball.y + self.op_ball.height)

        # Start prompt
        self.op_prompt.font = 'Corbel-12'
        self.window.add(self.op_prompt, (self.window.width - self.op_prompt.width)/2,
                        self.game_subtitle.y + 50 + self.op_prompt.height)

    def ball_initialise(self):
        # Randomise and set the ball initial speed
        self.__dx = random.randint(1, MAX_X_SPEED)
        self.__dy = INITIAL_Y_SPEED
        if random.random() > 0.5:
            self.set_dx()

    def game_win_screen(self):
        # Create the game win screen
        # Set the game over toggle to True
        self.game_over = True

        # Title over the screen
        self.gameover_title.text = 'YOU WIN'
        self.gameover_title.color = self.orange_title_color
        self.gameover_title.font = 'Arial Rounded MT Bold-40'
        self.window.add(self.gameover_title, (self.window.width - self.gameover_title.width) / 2,
                        (self.window.height - self.gameover_title.height) / 2 + self.gameover_title.height)
        winsound.PlaySound(self.sound_game_win, self.sound_play_flag)
        pause(1000)

        # Remove title
        self.window.remove(self.gameover_title)

        # Background
        self.background.color = self.win_bg_color
        self.background.fill_color = self.win_bg_color
        self.window.add(self.background)
        self.window.add(self.game_win_pic, (self.window.width - self.game_win_pic.width) / 2,
                        (self.window.height - self.game_win_pic.height) / 5)
        winsound.PlaySound(self.sound_game_win_screen, self.sound_play_flag)

        # Win game quote
        self.gameover_quote.text = 'You\'ve wasted enough time on this. Now go pat your dog!'
        self.gameover_quote.font = 'Gabriola-15'
        self.gameover_quote.color = 'dark grey'
        self.window.add(self.gameover_quote, (self.window.width - self.gameover_quote.width) / 2,
                        self.game_win_pic.y + self.game_win_pic.height + 20)

    def game_over_screen(self):
        # Create the gameover screen
        # Set the game over toggle to True
        self.game_over = True

        # Title over the screen
        self.gameover_title.text = 'GAME OVER'
        self.gameover_title.color = 'black'
        self.gameover_title.font = 'Arial Rounded MT Bold-40'
        self.window.add(self.gameover_title, (self.window.width - self.gameover_title.width)/2,
                        (self.window.height - self.gameover_title.height)/2+self.gameover_title.height)
        winsound.PlaySound(self.sound_game_over, self.sound_play_flag)
        pause(1000)

        # Remove title
        self.window.remove(self.gameover_title)

        # Background
        self.background.color = 'white'
        self.background.fill_color = 'white'
        self.window.add(self.background)
        self.window.add(self.gameover_pic, (self.window.width-self.gameover_pic.width)/2,
                        (self.window.height-self.gameover_pic.height)/5)
        winsound.PlaySound(self.sound_gameover_screen, self.sound_play_flag)

        # Quote list stores all the game over quotes
        quote_list = ['\"Those who don\'t learn from past levels will be forced to repeat them.\"',
                      '\"I pray for you, oh Lord, but you are not good at video games.\"',
                      '\"One who cannot dance must not blame the song.\"',
                      '\"To quit is to fail - as long as you are still in the game you are succeeding!\"',
                      '\"The game itself is bigger than the winning.\"',
                      '\"Since you\'re born, life is just a Suicide Game.\"',
                      '\"You\'re old, you\'re predictable, and you never stood a chance.\"',
                      '\"THIS is justice. THIS is what you deserve.\"',
                      '\"Your death was inevitable, I\'m afraid. A statistical certainty.\"']

        # Game over quote, randomise the quote from the list above
        self.gameover_quote.text = random.choice(quote_list)
        self.gameover_quote.font = 'Gabriola-13'
        self.gameover_quote.color = 'black'
        self.window.add(self.gameover_quote, (self.window.width-self.gameover_quote.width)/2,
                        self.gameover_pic.y + self.gameover_pic.height - 40)

        # Prompt for user to start over the game again
        self.gameover_prompt.font = 'Corbel-12'
        self.window.add(self.gameover_prompt, (self.window.width-self.gameover_prompt.width)/2,
                        self.gameover_quote.y + 50 + self.gameover_prompt.height)

        # Loop over to flash the label and break the loop when user press space
        while True:
            # If space is pressed, clear the window by breaking the loop
            if keyboard.is_pressed('space'):
                break
            pause(FRAME_RATE)
            self.gameover_prompt.color = 'white'
            pause(FRAME_RATE)
            self.gameover_prompt.color = 'black'

        # Clear the window for the next game
        self.window.clear()
        winsound.PlaySound(self.sound_game_start, self.sound_play_flag)

    def get_dx(self):
        return self.__dx

    def get_dy(self):
        return self.__dy

    def set_dx(self):
        self.__dx = -self.__dx

    def set_dy(self):
        self.__dy = -self.__dy

    def mouse_click(self, event):
        # While still in game (ie. not Game Over or You Win), then set the replay toggle to True
        if not self.game_over:
            self.replay = True

    def ball_reset(self):
        # Reset the ball to its original position
        self.window.add(self.ball, x=(self.window.width - self.ball.width) / 2,
                        y=(self.window.height - self.ball.height) / 2)

    def mouse_move(self, event):
        # Set the paddle to move together with the mouse
        if self.paddle.width/2 <= event.x <= self.window.width - self.paddle.width/2:
            self.paddle.x = event.x - self.paddle.width / 2

        # if mouse move to the left of the screen, paddle stays end of left screen
        elif event.x < self.paddle.width/2:
            self.paddle.x = 0
        # if mouse move to the right of the screen, paddle stays end of right screen
        elif event.x > self.window.width - self.paddle.width/2:
            self.paddle.x = self.window.width - self.paddle.width

    def display_lives(self, full_lives, lives_left):
        """
        :param full_lives: int, max lives available in the game.
        :param lives_left: int, current lives in the game.
        :return: display the heart pictures accordingly.
        """
        # If maximum lives then show every life as full heart
        if lives_left == full_lives:
            for i in range(1, full_lives+1):
                heart_full = GImage('pics/heart_full.jpg')
                self.window.add(heart_full, self.window.width - i * (self.heart_offset + heart_full.width),
                                self.window.height - (self.heart_offset + heart_full.height))
        # If not maximum lives then remove the relevant full heart, and replace with empty heart
        else:
            heart_full = GImage('pics/heart_full.jpg')
            heart_empty = GImage('pics/heart_empty.jpg')
            pos_x = self.window.width - (lives_left+1) * (self.heart_offset + heart_full.width)
            pos_y = self.window.height - (self.heart_offset + heart_full.height)

            obj = self.window.get_object_at(pos_x, pos_y)
            self.window.remove(obj)
            self.window.add(heart_empty, pos_x, pos_y)

    def check_collision(self):
        # This function checks the collision of ball with objects on screen
        left_x = self.ball.x
        right_x = self.ball.x + self.ball.width
        upper_y = self.ball.y
        lower_y = self.ball.y + self.ball.height
        obj = self.window.get_object_at(0, 0)

        # When ball is below half screen, it most likely will hit bottom first
        # When ball is above half screen, it most likely will hit top first
        if self.ball.y >= self.window.height/2:
            # Check the hit corner from bottom to top
            if self.window.get_object_at(left_x, lower_y) is not None:
                obj = self.window.get_object_at(left_x, lower_y)
            elif self.window.get_object_at(right_x, lower_y) is not None:
                obj = self.window.get_object_at(right_x, lower_y)
            elif self.window.get_object_at(left_x, upper_y) is not None:
                obj = self.window.get_object_at(left_x, upper_y)
            elif self.window.get_object_at(right_x, upper_y) is not None:
                obj = self.window.get_object_at(right_x, upper_y)
        else:
            # Reverse the order, check hit corner from top to bottom
            if self.window.get_object_at(left_x, upper_y) is not None:
                obj = self.window.get_object_at(left_x, upper_y)
            elif self.window.get_object_at(right_x, upper_y) is not None:
                obj = self.window.get_object_at(right_x, upper_y)
            elif self.window.get_object_at(left_x, lower_y) is not None:
                obj = self.window.get_object_at(left_x, lower_y)
            elif self.window.get_object_at(right_x, lower_y) is not None:
                obj = self.window.get_object_at(right_x, lower_y)

        # If ball hits something, check if object hit is a paddle first
        if obj is not None:
            # If the object hit is the paddle
            if obj is self.paddle:
                self.set_dy()
                winsound.PlaySound(self.sound_paddle_bounce, self.sound_play_flag)
            # If it's not paddle, stuff others than bricks should be excluded
            # Bricks can only be above paddle, hence only check items above paddle
            elif (self.ball.y+self.ball.height) <= self.paddle.y:
                self.set_dy()
                self.num_bricks -= 1
                # Update the display to the new number
                self.brick_left_count.text = self.num_bricks
                winsound.PlaySound(self.sound_brick_bounce, self.sound_play_flag)
                self.window.remove(obj)
            # If the ball hits object, move the ball once again to avoid being caught in the loop
            self.ball.move(self.__dx, self.__dy)

    def bricks_left(self):
        # This function checks if bricks left is less than the SPEED_UP_THRESHOLD
        # If true then speed up the ball by dy+3 and dx+1
        if not self.brick_left_toggle and self.num_bricks < SPEED_UP_THRESHOLD:
            # Display speed up cue
            self.speed_up.color = self.orange_title_color
            self.speed_up.font = 'Arial Rounded MT Bold-40'
            self.window.add(self.speed_up, (self.window.width - self.speed_up.width) / 2,
                            (self.window.height - self.speed_up.height) / 2 + self.speed_up.height)
            winsound.PlaySound(self.sound_hurry_up, winsound.SND_NOWAIT)
            self.window.remove(self.speed_up)

            # Change the brick count color to dark pastel red
            self.brick_left_count.font = 'Arial Rounded MT Bold-22'
            self.brick_left_count.color = self.brick_count_color

            # Speed up the XY axis speed depending on its sign
            if self.__dy > 0:
                self.__dy += 3
            else:
                self.__dy -= 3

            if self.__dx > 0:
                self.__dx += 1
            else:
                self.__dx -= 1

            # Set the toggle to true so this section is not repeated
            self.brick_left_toggle = True

        # If bricks are all gone user wins
        if self.num_bricks == 0:
            self.game_win = True
