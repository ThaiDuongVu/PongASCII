import curses
import random

screen = curses.initscr()
screen.nodelay(1)

board_width = 40 * 2
board_height = 20
char = " "

game_exit = False

ball_max_speed_x = 0.015
ball_max_speed_y = 0.03


class Player:
    def __init__(self, player_id):
        self.id = player_id
        self.height = 4
        self.char = "|"

        if self.id == 1:
            self.x = 3
        elif self.id == 2:
            self.x = board_width - 3 - 1
        self.y = board_height // 2 - self.height // 2

    def draw(self):
        for i in range(self.height):
            screen.addstr(self.y + i, self.x, self.char)

    def check_input(self, player_id, input_key):
        # ASCII table reference: https://www.ascii-code.com/
        if self.id == 1:
            if input_key == ord("w"):
                if self.y > 1:
                    self.y -= 1
            if input_key == ord("s"):
                if self.y < board_height - self.height - 1:
                    self.y += 1

        if self.id == 2:
            if input_key == ord("i"):
                if self.y > 1:
                    self.y -= 1
            if input_key == ord("k"):
                if self.y < board_height - self.height - 1:
                    self.y += 1


class Ball:
    def __init__(self):
        self.x = board_width // 2
        self.y = board_height // 2

        self.speed_x = random.choice([-ball_max_speed_x, ball_max_speed_x])
        self.speed_y = random.uniform(-ball_max_speed_y, ball_max_speed_y)

    def draw(self):
        self.x += self.speed_x
        self.y += self.speed_y
        screen.addstr(int(self.y), int(self.x), "o")

    def check_collision_wall(self):
        if self.y <= 1:
            self.speed_y = random.uniform(0, ball_max_speed_y)
        if self.y >= board_height - 1:
            self.speed_y = random.uniform(-ball_max_speed_y, 0)

        if self.x <= 0 or self.x >= board_width:
            self.__init__()

    def check_collision_player(self, player):
        if player.id == 1:
            if self.x <= player.x:
                if player.y >= self.y >= player.y + player.height:
                    self.speed_x = ball_max_speed_x

        elif player.id == 2:
            if self.x >= player.x:
                if player.y >= self.y >= player.y + player.height:
                    self.speed_x = -ball_max_speed_x


player1 = Player(1)
player2 = Player(2)
ball = Ball()

while not game_exit:
    screen.clear()
    for y in range(board_height):
        for x in range(board_width):
            if x == 0 or y == 0 or x == board_width - 1 or y == board_height - 1 or x == board_width // 2:
                screen.addstr(y, x, "#")
            else:
                screen.addstr(y, x, char)

    player1.draw()
    player2.draw()
    ball.draw()

    curses.curs_set(False)

    key = screen.getch()
    if key == 27:
        game_exit = True
    player1.check_input(1, key)
    player2.check_input(2, key)

    ball.check_collision_wall()
    ball.check_collision_player(player1)
    ball.check_collision_player(player2)

    screen.refresh()

curses.endwin()
