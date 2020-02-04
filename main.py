import curses

screen = curses.initscr()
screen.nodelay(1)

# ASCII table reference: https://www.ascii-code.com/

board_width = 40 * 2
board_height = 20
char = " "

game_exit = False

player_height = 4
player_char = "|"

player1_x = 2
player1_y = board_height // 2 - player_height // 2

player2_x = board_width - 2 * 2
player2_y = board_height // 2 - player_height // 2

while not game_exit:
    screen.clear()
    for y in range(board_height):
        for x in range(board_width):
            if x == 0 or y == 0 or x == board_width - 1 or y == board_height - 1 or x == board_width // 2:
                screen.addstr(y, x, "#")
            else:
                screen.addstr(y, x, char)

    for i in range(player_height):
        screen.addstr(player1_y + i, player1_x, player_char)
        screen.addstr(player2_y + i, player2_x, player_char)

    screen.refresh()

    key = screen.getch()
    if key == 27:
        game_exit = True
    if key == ord("w"):
        if player1_y > 0:
            player1_y -= 1
    if key == ord("s"):
        if player1_y < board_height - player_height:
            player1_y += 1

curses.endwin()
