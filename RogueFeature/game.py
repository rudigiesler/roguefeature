import pygame
from pygame.locals import *

BLOCKWIDTH = 23
BLOCKHEIGHT = 10
TITLE = "RogueFeature"
FPS = 60
ScreenWidth = 52 * BLOCKWIDTH
ScreenHeight = 52 * BLOCKHEIGHT

pygame.init()
fpsClock = pygame.time.Clock()

windowSurfaceObj = pygame.display.set_mode((ScreenWidth, ScreenHeight))
pygame.display.set_caption("RogueFeature v0.0.0")

running = True

while running:
    windowSurfaceObj.fill(pygame.Color(0, 0, 0))

    pygame.display.set_caption(TITLE + ' (fps: %f)' % fpsClock.get_fps())

    fpsClock.tick(FPS)

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
