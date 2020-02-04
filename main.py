import curses
import random

screen = curses.initscr()
screen.nodelay(1)

board_width = 40 * 2
board_height = 20
char = " "

game_exit = False


class Player:
    def __init__(self, player_id):
        self.height = 4
        self.char = "|"

        if player_id == 1:
            self.x = 3
        elif player_id == 2:
            self.x = board_width - 3 - 1
        self.y = board_height // 2 - self.height // 2

    def draw(self):
        for i in range(self.height):
            screen.addstr(self.y + i, self.x, self.char)

    def check_input(self, player_id, input_key):
        # ASCII table reference: https://www.ascii-code.com/
        if player_id == 1:
            if input_key == ord("w"):
                if self.y > 1:
                    self.y -= 1
            if input_key == ord("s"):
                if self.y < board_height - self.height - 1:
                    self.y += 1

        if player_id == 2:
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

        self.speed_x = random.choice([-0.02, 0.02])
        self.speed_y = random.uniform(-0.04, 0.04)

    def draw(self):
        self.x += self.speed_x
        self.y += self.speed_y
        screen.addstr(int(self.y), int(self.x), "o")

    def check_collision(self):
        pass


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

    screen.refresh()

curses.endwin()
