import curses
screen = curses.initscr()
screen.nodelay(1)

width = 30 * 2
height = 15
char = "-"

game_exit = False

player_x = 0
player_y = 0
player_height = 5
player_char = "@"

while not game_exit:
    screen.clear()
    for y in range(height):
        for x in range(width):
            if x % 2 == 0:
                screen.addstr(y, x, char)
            else:
                screen.addstr(y, x, " ")

    for i in range(player_height):
        screen.addstr(player_y + i, player_x, player_char)
    screen.refresh()

    key = screen.getch()
    if key == ord("q"):
        game_exit = True

curses.endwin()
