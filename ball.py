import random


class Ball:
    def __init__(self, board_width, board_height, ball_max_speed_x, ball_max_speed_y):
        self.x = board_width // 2
        self.y = board_height // 2 - 1

        self.speed_x = random.choice([-ball_max_speed_x, ball_max_speed_x])
        self.speed_y = random.uniform(-ball_max_speed_y, ball_max_speed_y)

    def draw(self, pause, start, screen):
        if not pause and start:
            self.x += self.speed_x
            self.y += self.speed_y
        screen.addstr(int(self.y), int(self.x), "o")

    def reset(self, side, board_width, board_height, ball_max_speed_x, ball_max_speed_y):
        self.x = board_width // 2
        self.y = board_height // 2

        self.speed_y = random.uniform(-ball_max_speed_y, ball_max_speed_y)

        if side == "left":
            self.speed_x = ball_max_speed_x
        elif side == "right":
            self.speed_x = -ball_max_speed_x

    def check_collision_wall(self, player1, player2, board_width, board_height, ball_max_speed_x, ball_max_speed_y):
        if self.y <= 1:
            self.speed_y = random.uniform(0, ball_max_speed_y)
        if self.y >= board_height - 1:
            self.speed_y = random.uniform(-ball_max_speed_y, 0)

        if self.x <= 0:
            player2.score += 1
            self.reset("left", board_width, board_height,
                       ball_max_speed_x, ball_max_speed_y)

        if self.x >= board_width:
            player1.score += 1
            self.reset("right", board_width, board_height,
                       ball_max_speed_x, ball_max_speed_y)

    def check_collision_player(self, player, ball_max_speed_x, ball_max_speed_y):
        if player.id == 1:
            if self.x <= player.x + 1:
                if player.y <= self.y <= player.y + player.height:
                    self.speed_x = ball_max_speed_x
                    self.speed_y = random.uniform(-ball_max_speed_y,
                                                  ball_max_speed_y)

        elif player.id == 2:
            if self.x >= player.x - 1:
                if player.y <= self.y <= player.y + player.height:
                    self.speed_x = -ball_max_speed_x
                    self.speed_y = random.uniform(-ball_max_speed_y,
                                                  ball_max_speed_y)
