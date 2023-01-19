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
arrayButton = []

arrayButton.append(Button(sc, '+1', score.textColor, (0,255,200), sizeButton, 100, 400, 0, 0))
arrayButton.append(Button(sc, '+1 к клику', score.textColor, (0,255,100), sizeButton, 240, 400, 30, 1.2))
arrayButton.append(Button(sc, '+5 в сек', score.textColor, (0,255,255), sizeButton, 380, 400, 40, 1.3))
arrayButton.append(Button(sc, '+2 к у клик', score.textColor, (0,255,50), sizeButton, 240, 540, 80, 1.5))
arrayButton.append(Button(sc, '+5 к сек', score.textColor, (0,255,150), sizeButton, 380, 540, 100, 1.7))


stats.earsec()

while True:

    event(stats, arrayButton)
    update(bgColor, sc, score, arrayButton)