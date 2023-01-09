import pygame

def event():

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

def update(bgColor, sc, score, button):

    sc.fill(bgColor)
    score.showScore()
    button.showButton()
    button.showTextButton()

    pygame.display.update()