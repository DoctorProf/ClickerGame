import pygame

def event(button, stats, upgradeButton):

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                a,b = event.pos[0],event.pos[1]
                if (a > button.surfRect.left and a < button.surfRect.right) and (b > button.surfRect.top and b < button.surfRect.bottom ):
                    stats.score += int(button.textButton)
                if (a > upgradeButton.surfRect.left and a < upgradeButton.surfRect.right) and (b > upgradeButton.surfRect.top and b < upgradeButton.surfRect.bottom ):
                    if upgradeButton.priceButton > 10000:
                        upgradeButton.textUpgButton = 'max'
                        upgradeButton.priceButton = 100000

                    elif stats.score >= upgradeButton.priceButton:

                        button.textButton = '+' + str(int(button.textButton) + 1)
                        stats.score -= upgradeButton.priceButton
                        upgradeButton.priceButton = int(upgradeButton.priceButton * 1.5)

def update(bgColor, sc, score, button, upgradeButton):

    sc.fill(bgColor)
    score.ScoreImage()
    score.showScore()
    button.showButton()
    upgradeButton.showUpgButton()
    button.showTextButton()
    upgradeButton.showTextUpgButton()

    pygame.display.update()