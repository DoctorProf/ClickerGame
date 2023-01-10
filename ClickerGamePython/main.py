import pygame
from Score import *
from Events import *
from Stats import *
from Button import *
from UpgradeButton import *

pygame.init()
sc = pygame.display.set_mode((700, 800))
pygame.display.set_caption('ClickerGame')
bgColor = (255,255,255)
stats = Stats()
score = Score(sc, stats, bgColor)
button = Button(sc, '+1', score.textColor)
upgradeButton = Upgrade(sc, '+1 к клику', score.textColor, button.sizeButton)

while True:

    event(button, stats,upgradeButton)
    update(bgColor, sc, score, button, upgradeButton)