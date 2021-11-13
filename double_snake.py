import pygame as pg
from random import randrange
import sys

XSIZE = 1200
YSIZE = 800
BASE = 50
FPS = 5


def rect(point: tuple) -> tuple:
    return point[0], point[1], BASE-2, BASE-2


class App:

    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode([XSIZE, YSIZE])
        self.snake = [(randrange(0, XSIZE-500, BASE), randrange(0, YSIZE, BASE))]
        self.apple = (randrange(0, XSIZE, BASE), randrange(0, YSIZE, BASE))
        self.clock = pg.time.Clock()

    def run(self):
        dx = BASE
        dy = 0
        length = 1

        while True:
            x = self.snake[-1][0]
            y = self.snake[-1][1]
            print(x, y, self.snake)
            self.screen.fill((175,238,238))
            pg.draw.rect(self.screen, 'RED', rect(self.apple))
            [pg.draw.rect(self.screen, 'GREEN', rect(x)) for x in self.snake]
            pg.display.flip()
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
            keys = pg.key.get_pressed()
            if keys[pg.K_LEFT]:
                dx = -BASE
                dy = 0
            if keys[pg.K_RIGHT]:
                dx = BASE
                dy = 0
            if keys[pg.K_UP]:
                dx = 0
                dy = -BASE
            if keys[pg.K_DOWN]:
                dx = 0
                dy = BASE

            if self.apple[0] == x and self.apple[1] == y:
                self.apple = (randrange(0, XSIZE, BASE), randrange(0, YSIZE, BASE))
                length += 1

            if x > XSIZE or x < 0 or y > YSIZE or y < 0:
                break

            self.snake.append((dx+x, dy+y))
            self.snake = self.snake[-length:]
            self.clock.tick(FPS)


if __name__ == '__main__':
    app = App()
    app.run()
