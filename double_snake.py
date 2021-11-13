import pygame as pg
from random import randrange
import sys

XSIZE = 1200
YSIZE = 800
BASE = 50
FPS = 6


def rect(point: tuple) -> tuple:
    return point[0], point[1], BASE-2, BASE-2



class Snake:

    def __init__(self):
       pass



class App:

    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode([XSIZE, YSIZE])
        self.clock = pg.time.Clock()
        self.snake = [(randrange(0, XSIZE - 500, BASE), randrange(0, YSIZE, BASE))]

    def run(self):
        dx = BASE
        dy = 0
        length = 1
        add_fps = 0
        apple = (randrange(0, XSIZE, BASE), randrange(0, YSIZE, BASE))
        while True:
            x = self.snake[-1][0]
            y = self.snake[-1][1]
            print(x, y, self.snake)
            self.screen.fill((175,238,238))
            pg.draw.circle(self.screen, 'RED', (apple[0]+BASE/2, apple[1]+BASE/2), BASE/2.5)
            pg.draw.line(self.screen, 'BROWN', (apple[0] + BASE / 2, apple[1] -8),
                         (apple[0] + BASE / 2 - 4, apple[1]+8), 4)
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

            # eating an apple
            if apple[0] == x and apple[1] == y:
                apple = (randrange(0, XSIZE, BASE), randrange(0, YSIZE, BASE))
                length += 1
                add_fps = int(length/2)

            if x > XSIZE or x < 0 or y > YSIZE or y < 0:
                break

            # check for collision
            if (dx+x, dy+y) not in self.snake:
                self.snake.append((dx+x, dy+y))
                self.snake = self.snake[-length:]
            else:
                break
            self.clock.tick(FPS+add_fps)


if __name__ == '__main__':
    app = App()
    app.run()
