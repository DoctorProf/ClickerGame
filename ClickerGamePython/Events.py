import pygame

def event(button, stats, upgradeButton, runButton):

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            stats.stop()
            exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                a,b = event.pos[0],event.pos[1]

                if (a > button.surfRect.left and a < button.surfRect.right) and (b > button.surfRect.top and b < button.surfRect.bottom ):
                    stats.score += int(button.textButton)

                if (a > upgradeButton.surfRect.left and a < upgradeButton.surfRect.right) and (b > upgradeButton.surfRect.top and b < upgradeButton.surfRect.bottom ):
                    if upgradeButton.priceButton > 10000:
                        upgradeButton.textUpgButton = 'max'

                    elif stats.score >= upgradeButton.priceButton:

                        button.textButton = '+' + str(int(button.textButton) + 1)
                        stats.score -= upgradeButton.priceButton
                        upgradeButton.priceButton = int(upgradeButton.priceButton * 1.3)

                if (a > runButton.surfRect.left and a < runButton.surfRect.right) and (b > runButton.surfRect.top and b < runButton.surfRect.bottom):
                    if runButton.priceButton > 10000:
                        runButton.textRunButton = 'max'

                    elif stats.score >= runButton.priceButton:
 
                        stats.earnings += 1
                        stats.score -= runButton.priceButton
                        runButton.priceButton = int(runButton.priceButton * 1.3)

def update(bgColor, sc,stats, score, button, upgradeButton, runButton):

    sc.fill(bgColor)
    score.ScoreImage()
    score.showScore()

    button.showButton()
    upgradeButton.showButton()
    runButton.showButton()

    button.showTextButton()
    upgradeButton.showTextButton()
    runButton.showTextButton()

    pygame.display.update()