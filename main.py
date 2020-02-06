import curses
import random

screen = curses.initscr()
screen.nodelay(1)

board_width = 40 * 2
board_height = 20
char = " "

ball_max_speed_x = 0.05
ball_max_speed_y = 0.02


def add_text():
    screen.addstr(board_height, 0, "Player 1 control: up: W, down: S")
    screen.addstr(board_height + 1, 0, "Player 2 control: up: I, down: K")
    screen.addstr(board_height + 2, 0, "Press ESC to exit")
    screen.addstr(board_height + 3, 0, "Press B to pause")


def win(player_id):
    pass


class Player:
    def __init__(self, player_id):
        self.id = player_id
        self.score = 0

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

        if self.id == 1:
            screen.addstr(3, (board_width // 4), str(self.score))
        elif self.id == 2:
            screen.addstr(3, (board_width // 4) * 3, str(self.score))

    def check_input(self, input_key):
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

    def check_win(self):
        if self.score >= 11:
            win(self.id)


class Ball:
    def __init__(self):
        self.x = board_width // 2
        self.y = board_height // 2 - 1

        self.speed_x = random.choice([-ball_max_speed_x, ball_max_speed_x])
        self.speed_y = random.uniform(-ball_max_speed_y, ball_max_speed_y)

    def draw(self, pause, start):
        if not pause and start:
            self.x += self.speed_x
            self.y += self.speed_y
        screen.addstr(int(self.y), int(self.x), "o")

    def reset(self, side):
        self.x = board_width // 2
        self.y = board_height // 2

        self.speed_y = random.uniform(-ball_max_speed_y, ball_max_speed_y)

        if side == "left":
            self.speed_x = ball_max_speed_x
        elif side == "right":
            self.speed_x = -ball_max_speed_x

    def check_collision_wall(self, player1, player2):
        if self.y <= 1:
            self.speed_y = random.uniform(0, ball_max_speed_y)
        if self.y >= board_height - 1:
            self.speed_y = random.uniform(-ball_max_speed_y, 0)

        if self.x <= 0:
            player2.score += 1
            self.reset("left")

        if self.x >= board_width:
            player1.score += 1
            self.reset("right")

    def check_collision_player(self, player):
        if player.id == 1:
            if self.x <= player.x + 1:
                if player.y <= self.y <= player.y + player.height:
                    self.speed_x = ball_max_speed_x
                    self.speed_y = random.uniform(-ball_max_speed_y, ball_max_speed_y)

        elif player.id == 2:
            if self.x >= player.x - 1:
                if player.y <= self.y <= player.y + player.height:
                    self.speed_x = -ball_max_speed_x
                    self.speed_y = random.uniform(-ball_max_speed_y, ball_max_speed_y)


def main_loop():
    game_exit = False
    pause = False
    start = False

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

        ball.draw(pause, start)
        if not start:
            screen.addstr(board_height // 2 - 1, board_width // 2 - 10, "Press Space to start")
        add_text()

        curses.curs_set(False)

        key = screen.getch()
        if key == 27:
            game_exit = True

        if key == ord("b"):
            if pause:
                pause = False
            else:
                pause = True
        if key == 32:
            start = True

        if not pause and start:
            player1.check_input(key)
            player2.check_input(key)

            ball.check_collision_wall(player1, player2)
            ball.check_collision_player(player1)
            ball.check_collision_player(player2)
        if pause:
            screen.addstr(board_height // 2 - 1, board_width // 2 - 2, "PAUSE")

        screen.refresh()

    curses.endwin()

main_loop()
