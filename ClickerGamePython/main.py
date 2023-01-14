import pygame
from Score import *
from Events import *
from Stats import *
from Button import *


pygame.init()
sc = pygame.display.set_mode((700, 800))
pygame.display.set_caption('ClickerGame')
bgColor = (255,255,255)
sizeButton = (70, 70)
stats = Stats()
score = Score(sc, stats, bgColor)
button = Button(sc, '+1', score.textColor, (0,255,200), sizeButton, 100, 400, 0)
upgradeButton = Button(sc, '+1 к клику', score.textColor, (0,255,100), sizeButton, 240, 400, 20)
runButton = Button(sc, '+1 в сек', score.textColor, (0,255,255), sizeButton, 380, 400, 30)
stats.earsec()

while True:

    event(button, stats,upgradeButton, runButton)
    update(bgColor, sc,stats, score, button, upgradeButton, runButton)