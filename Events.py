import pygame

def event(stats, arrayButton):

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            stats.stop()
            exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                a,b = event.pos[0],event.pos[1]
                
                if (a > arrayButton[0].surfRect.left and a < arrayButton[0].surfRect.right) and (b > arrayButton[0].surfRect.top and b < arrayButton[0].surfRect.bottom ):
                    stats.score += int(arrayButton[0].textButton)

                if (a > arrayButton[1].surfRect.left and a < arrayButton[1].surfRect.right) and (b > arrayButton[1].surfRect.top and b < arrayButton[1].surfRect.bottom ):
                    if arrayButton[1].priceButton > 1000000:

                        arrayButton[1].textButton = 'max'

                    elif stats.score >= arrayButton[1].priceButton:

                        arrayButton[0].textButton = '+' + str(int(arrayButton[0].textButton) + int(arrayButton[1].textButton.split()[0]))
                        stats.score -= arrayButton[1].priceButton
                        arrayButton[1].priceButton = int(arrayButton[1].priceButton * arrayButton[1].factorButton)

                if (a > arrayButton[2].surfRect.left and a < arrayButton[2].surfRect.right) and (b > arrayButton[2].surfRect.top and b < arrayButton[2].surfRect.bottom):

                    if arrayButton[2].priceButton > 1000000:
                        arrayButton[2].textButton = 'max'

                    elif stats.score >= arrayButton[2].priceButton:
                        stats.earnings += int(arrayButton[2].textButton.split()[0])
                        stats.score -= arrayButton[2].priceButton
                        arrayButton[2].priceButton = int(arrayButton[2].priceButton * arrayButton[2].factorButton)
                    
                if (a > arrayButton[3].surfRect.left and a < arrayButton[3].surfRect.right) and (b > arrayButton[3].surfRect.top and b < arrayButton[3].surfRect.bottom):

                    if arrayButton[3].priceButton > 1000000:
                        arrayButton[3].textButton = 'max'

                    elif stats.score >= arrayButton[3].priceButton:
                        c = arrayButton[1].textButton.split()
                        c[0] ='+' + str(int(c[0]) + int(arrayButton[3].textButton.split()[0]))
                        arrayButton[1].textButton = ' '.join(c)
                        stats.score -= arrayButton[3].priceButton
                        arrayButton[3].priceButton = int(arrayButton[3].priceButton * arrayButton[3].factorButton)
                        
                    
                if (a > arrayButton[4].surfRect.left and a < arrayButton[4].surfRect.right) and (b > arrayButton[4].surfRect.top and b < arrayButton[4].surfRect.bottom):

                    if arrayButton[4].priceButton > 1000000:
                        arrayButton[4].textButton = 'max'

                    elif stats.score >= arrayButton[4].priceButton:
                        c = arrayButton[2].textButton.split()
                        c[0] = '+' + str(int(c[0]) + int(arrayButton[4].textButton.split()[0]))
                        arrayButton[2].textButton = ' '.join(c)
                        stats.score -= arrayButton[4].priceButton
                        arrayButton[4].priceButton = int(arrayButton[4].priceButton * arrayButton[4].factorButton)

def update(bgColor, sc, score, arrayButton):

    sc.fill(bgColor)
    score.ScoreImage()
    score.showScore()

    for button in arrayButton:

        button.showButton()

        button.showTextButton()

    pygame.display.update()