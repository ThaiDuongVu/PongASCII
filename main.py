import curses
import sys

from ball import Ball
from player import Player

screen = curses.initscr()
screen.nodelay(1)

board_width = 40 * 2
board_height = 20
char = " "

ball_max_speed_x = 0.05
ball_max_speed_y = 0.02

max_score = 5


def add_text():
    screen.addstr(board_height, 0, "Player 1 control: up: W, down: S")
    screen.addstr(board_height + 1, 0, "Player 2 control: up: I, down: K")
    screen.addstr(board_height + 2, 0, "Press ESC to exit")
    screen.addstr(board_height + 3, 0, "Press B to pause")


def win(player_id):
    screen.addstr(board_height // 2 - 1, board_width // 2 - 6, "Player " + player_id + " wins", )
    screen.addstr(board_height // 2, board_width // 2 - 10, "Press Space to start")


def draw_screen():
    for y in range(board_height):
        for x in range(board_width):
            if x == 0 or y == 0 or x == board_width - 1 or y == board_height - 1 or x == board_width // 2:
                screen.addstr(y, x, "#")
            else:
                screen.addstr(y, x, char)


def player_win(player1, player2, ball):
    if player1.score >= max_score and player2.score <= max_score - 2:
        ball.speed_x = 0
        ball.speed_y = 0

        screen.addstr(board_height // 2 - 1, board_width // 2 - 6, "Player 1 wins", )
        screen.addstr(board_height // 2, board_width // 2 - 10, "Press Space to start")

        screen.refresh()
        return True


def main_loop():
    game_exit = False
    pause = False
    start = False

    game_over = False

    player1 = Player(1, board_width, board_height)
    player2 = Player(2, board_width, board_height)
    ball = Ball(board_width, board_height, ball_max_speed_x, ball_max_speed_y)

    while not game_exit:
        screen.clear()
        draw_screen()

        player1.draw(screen, board_width)
        player2.draw(screen, board_width)

        ball.draw(pause, start, screen)
        if not start:
            screen.addstr(board_height // 2 - 1, board_width // 2 - 10, "Press Space to start")
        add_text()

        curses.curs_set(False)

        key = screen.getch()
        if key == 27:
            game_exit = True
            curses.endwin()
            quit()

        if key == ord("b"):
            if pause:
                pause = False
            else:
                pause = True
        if key == 32:
            if not start:
                start = True
                ball.__init__(board_width, board_height, ball_max_speed_x, ball_max_speed_y)
            if game_over:
                main_loop()

        if not pause and start and not game_over:
            player1.check_input(key, board_height)
            player2.check_input(key, board_height)

            ball.check_collision_wall(player1, player2, board_width, board_height, ball_max_speed_x, ball_max_speed_y)
            ball.check_collision_player(player1, ball_max_speed_x, ball_max_speed_y)
            ball.check_collision_player(player2, ball_max_speed_x, ball_max_speed_y)
        if pause:
            screen.addstr(board_height // 2 - 1, board_width // 2 - 2, "PAUSE")

        if player_win(player1, player2, ball):
            game_over = True
        elif player_win(player2, player1, ball):
            game_over = True

        if not start and not game_over or pause:
            screen.refresh()

    curses.endwin()
    quit()
    sys.exit()


main_loop()
