from random import *
import pygame as pg
import time
BLACK = (0, 0, 0)
SUPERLIGHTBLUE = (148, 255, 238)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 51)
RED = (255, 0, 0)
LIGHTBLUE = (0, 255, 255)
WHITE = (255, 255, 255)
timem = 0
timem2 = 10
points = 0
pg.init()
clock = pg.time.Clock()
window = pg.display.set_mode((500, 500))
start_time = time.time()
end_time = time.time()
class TextArea():
    def __init__(self, x = 100, y = 275, widght = 300, height = 50, color = LIGHTBLUE):
        self.rect = pg.Rect(x, y, widght, height)
        self.fill = color
    def set_text(self, text, fsize = 35, textcolor = BLACK):
        self.text = text
        self.image = pg.font.Font(None, fsize).render(text, True, textcolor)
    def draw(self, shiftx = 10, shifty = 12.5):
        pg.draw.rect(window, self.fill, self.rect)
        window.blit(self.image, (self.rect.x + shiftx, self.rect.y + shifty))
    def collidepoint(self, x, y):
        return self.rect.collidepoint(x, y)
# dback = TextArea(20, 250, 100, 125, (0, 0, 0))
# dback.set_text('')
cards = []
back = []
x = 5
for i in range(4):
    a = TextArea(x, 250, 75, 100)
    a.set_text('')
    cards.append(a)
    aback = TextArea(x, 250, 100, 125, BLACK)
    aback.set_text('')
    back.append(aback)
    x += 130
# b = TextArea(280, 250, 75, 100)
# b.set_text('ctrl+v')
# bback = TextArea(280, 250, 100, 125, (0, 0, 0))
# bback.set_text('')
# c = TextArea(410, 250, 75, 100)
# c.set_text('ctrl+v')
# cback = TextArea(410, 250, 100, 125, (0, 0, 0))
# cback.set_text('')
# d = TextArea(20, 250, 75, 100)
# d.set_text('ctrl+v')
wait = 0
num = 0
while True:
    window.fill(SUPERLIGHTBLUE)
    timer = pg.font.Font(None, 56).render('Время:'+str(timem2), True, BLACK)
    score = pg.font.Font(None, 56).render('Счёт:'+str(points), True, BLACK)
    window.blit(timer, (0, 0))
    window.blit(score, (390, 0))
    if wait == 0:
        for i in range(4):
            cards[i].set_text('')
            cards[i].fill = YELLOW
        num = randint(0, 3)
        cards[num].set_text('ctrl+v')
        wait = 20
    for event in pg.event.get():
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            x, y = event.pos
            for i in range(4):
                if cards[i].collidepoint(x, y):
                    if i == num:
                        cards[i].fill = GREEN
                        points += 1
                    else:
                        cards[i].fill = RED
                        points -= 1
    for i in range(4):
        back[i].draw()
        cards[i].draw()
    wait -= 1
    timem += 1
    if timem == 40 and points < 5:
        timem2 -= 1
        timem = 0
    if timem2 <= 0:
        window.fill(RED)
        lose = pg.font.Font(None, 56).render('Вы Проиграли!', True, BLACK)
        window.blit(lose, (125, 300))
    if points >= 5:
        window.fill(GREEN)
        win = pg.font.Font(None, 56).render('Вы Выиграли!', True, BLACK)
        win2 = pg.font.Font(None, 36).render('Время прохождения: '+str(10 - timem2), True, BLACK)
        window.blit(win, (125, 300))
        window.blit(win2, (125, 340))
    pg.display.update()
    clock.tick(40)
    # aback.draw()
    # a.draw()
    # bback.draw()
    # b.draw()
    # cback.draw()
    # c.draw()




















