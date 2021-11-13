import pygame as pg
from random import randrange, choice
import sys

XSIZE = 1200
YSIZE = 800
BASE = 50
FPS = 6


def rect(point: tuple) -> tuple:
    return point[0], point[1], BASE - 2, BASE - 2


class Snake:
    def __init__(self, keys: tuple = (pg.K_LEFT, pg.K_RIGHT, pg.K_UP, pg.K_DOWN)):
        self.snake = [(randrange(0, XSIZE - 500, BASE), randrange(0, YSIZE, BASE))]
        self.x = self.snake[-1][0]
        self.y = self.snake[-1][1]
        self.length = 1
        self.dx = BASE
        self.dy = 0
        self.keys = keys
        self.color = choice(["YELLOW", "GREEN", "BLACK", "NAVY", "GREY", "BROWN"])

    def move_snake(self, apple):
        # eating an apple
        new_apple = False
        end_game = False
        if apple[0] == self.x and apple[1] == self.y:
            apple = (randrange(0, XSIZE, BASE), randrange(0, YSIZE, BASE))
            self.length += 1
            new_apple = True

        # proceed keys actions
        keys = pg.key.get_pressed()
        if keys[self.keys[0]]:
            self.dx = -BASE
            self.dy = 0
        if keys[self.keys[1]]:
            self.dx = BASE
            self.dy = 0
        if keys[self.keys[2]]:
            self.dx = 0
            self.dy = -BASE
        if keys[self.keys[3]]:
            self.dx = 0
            self.dy = BASE

        # check boundaries
        if self.x > XSIZE or self.x < 0 or self.y > YSIZE or self.y < 0:
            end_game = True

        # check for collision
        if (self.dx + self.x, self.dy + self.y) not in self.snake:
            self.x += self.dx
            self.y += self.dy
            self.snake.append((self.x, self.y))
            self.snake = self.snake[-self.length:]
        else:
            end_game = True

        return new_apple, end_game


class App:

    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode([XSIZE, YSIZE])
        self.clock = pg.time.Clock()

    def run(self):
        score = 0
        snakes = [Snake(), Snake((pg.K_a, pg.K_d, pg.K_w, pg.K_s))]
        add_fps = 0
        apple = (randrange(0, XSIZE, BASE), randrange(0, YSIZE, BASE))
        while True:
            self.screen.fill((175, 238, 238))
            # draw apple
            pg.draw.circle(self.screen, 'RED', (apple[0] + BASE / 2, apple[1] + BASE / 2), BASE / 2.5)
            pg.draw.line(self.screen, 'BROWN', (apple[0] + BASE / 2, apple[1] - 8),
                         (apple[0] + BASE / 2 - 4, apple[1] + 8), 4)
            # draw snakes
            for snake in snakes:
                [pg.draw.rect(self.screen, snake.color, rect(x)) for x in snake.snake]
                is_apple, is_end = snake.move_snake(apple)
                if is_apple:
                    score += 1
                    print(f"score: {score}")
                    apple = (randrange(0, XSIZE, BASE), randrange(0, YSIZE, BASE))
                if is_end:
                    print("GAME OVER")
                    pg.quit()
                    sys.exit()
            pg.display.flip()
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
            self.clock.tick(FPS + add_fps)


if __name__ == '__main__':
    app = App()
    app.run()
