import pygame
import random
pygame.init()

BR_WIDTH = 5
WIDTH = 400
HEIGHT = 600
TL_WIDTH = WIDTH/4 - BR_WIDTH
TL_HEIGHT = 150
VEL = 1
BG_COLOR = (0, 0, 0)
LN_COLOR = (255, 0, 0)
TL_COLOR = (0, 0, 255)
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Piano Tiles')
clock = pygame.time.Clock()

TILES = []
DONE = []
SCORE = 0
CURR = 0

class Tile:
    def __init__(self):
        self.CLM = random.randint(0,3)
        self.y = -1 * TL_HEIGHT
        self.x = WIDTH/4 * self.CLM + BR_WIDTH/2
        self.isclick = False
        TILES.append(self)
    def draw(self):
        if self.isclick:
            pygame.draw.rect(win, (0, 255, 0), (self.x, self.y, TL_WIDTH, TL_HEIGHT))
        else:
            pygame.draw.rect(win, TL_COLOR, (self.x, self.y, TL_WIDTH, TL_HEIGHT))
            pygame.draw.rect(win, (0, 255, 0), (self.x, self.y, TL_WIDTH, TL_HEIGHT), 5)
        self.y += VEL
    def check(self):
        global CURR, VEL
        if CURR == 1:
            VEL += 0.1
            CURR = 0
        global IDX
        if self.y >= HEIGHT - TL_HEIGHT:
            if self.isclick == False:
                pygame.quit()

def main():
    global ctr, SCORE, CURR
    isclick = False
    if 1 == 1:
        if TILES[len(TILES) - 1].y >= 0:
            TILES.append(Tile())
        tile = TILES[0]
    if ctr >= 30:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            if tile.CLM == 0 and tile.y + TL_HEIGHT >= 3 * HEIGHT/4 and tile.y <= 3 * HEIGHT/4:
                TILES.remove(tile)
                ctr = 0
                isclick = True
            else:
                pygame.quit()
        elif keys[pygame.K_s]:
            if tile.CLM == 1 and tile.y + TL_HEIGHT >= 3 * HEIGHT/4 and tile.y <= 3 * HEIGHT/4:
                TILES.remove(tile)
                ctr = 0
                isclick = True
            else:
                pygame.quit()
        elif keys[pygame.K_d]:
            if tile.CLM == 2 and tile.y + TL_HEIGHT >= 3 * HEIGHT/4 and tile.y <= 3 * HEIGHT/4:
                TILES.remove(tile)
                ctr = 0
                isclick = True
            else:
                pygame.quit()
        elif keys[pygame.K_f]:
            if tile.CLM == 3 and tile.y + TL_HEIGHT >= 3 * HEIGHT/4 and tile.y <= 3 * HEIGHT/4:
                TILES.remove(tile)
                ctr = 0
                isclick = True
            else:
                pygame.quit()
    if isclick:
        TILES.remove(TILES[0])
        SCORE += 1
        CURR += 1

def drawBorder():
    pygame.draw.rect(win, (255, 255, 255), (0, 3 * HEIGHT/4, WIDTH, HEIGHT), BR_WIDTH)
    pygame.draw.rect(win, LN_COLOR, (0, 0, WIDTH, HEIGHT), BR_WIDTH)
    pygame.draw.rect(win, LN_COLOR, (WIDTH/4 - BR_WIDTH/2, 0, WIDTH, HEIGHT), BR_WIDTH)
    pygame.draw.rect(win, LN_COLOR, (WIDTH/2 - BR_WIDTH/2, 0, WIDTH, HEIGHT), BR_WIDTH)
    pygame.draw.rect(win, LN_COLOR, (3 * WIDTH/4 - BR_WIDTH/2, 0, WIDTH, HEIGHT), BR_WIDTH)

def drawGameWin():
    win.fill(BG_COLOR)
    for i in TILES:
        i.draw()
    TILES[0].check()
    drawBorder()
    pygame.display.update()

TILES.append(Tile())

ctr = 0
run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    
    ctr += 1
    drawGameWin()
    main()