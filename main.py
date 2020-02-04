import curses

screen = curses.initscr()
screen.nodelay(1)

# ASCII table reference: https://www.ascii-code.com/

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

    def check_input(self, player_id, key):
        if player_id == 1:
            if key == ord("w"):
                if self.y > 1:
                    self.y -= 1
            if key == ord("s"):
                if self.y < board_height - self.height - 1:
                    self.y += 1

        elif player_id == 2:
            if key == ord("i"):
                if self.y > 1:
                    self.y -= 1
            if key == ord("k"):
                if self.y < board_height - self.height - 1:
                    self.y += 1


class Ball:
    pass


player1 = Player(1)
player2 = Player(2)

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

    key = screen.getch()
    if key == 27:
        game_exit = True
    player1.check_input(1, key)
    player2.check_input(2, key)

    screen.refresh()

curses.endwin()
