class Player:
    def __init__(self, player_id, board_width, board_height):
        self.id = player_id
        self.score = 0

        self.height = 4
        self.char = "|"

        if self.id == 1:
            self.x = 3
        elif self.id == 2:
            self.x = board_width - 3 - 1
        self.y = board_height // 2 - self.height // 2

    def draw(self, screen, board_width):
        for i in range(self.height):
            screen.addstr(self.y + i, self.x, self.char)

        if self.id == 1:
            screen.addstr(3, (board_width // 4), str(self.score))
        elif self.id == 2:
            screen.addstr(3, (board_width // 4) * 3, str(self.score))

    def check_input(self, input_key, board_height):
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
