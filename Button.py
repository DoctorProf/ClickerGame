import pygame

class Button:

    def __init__(self, sc, textButton, textColor, buttonColor, sizeButton, x, y, priceButton, factorButton):

        self.buttonColor = buttonColor
        self.textColor = textColor
        self.sc = sc
        self.sizeButton = sizeButton
        self.factorButton = factorButton
        self.surf = pygame.Surface((self.sizeButton))
        self.surfRect = self.surf.get_rect()
        self.surfRect.x = x
        self.surfRect.y = y
        self.font = pygame.font.SysFont(None, 18)
        self.textButton = textButton
        self.priceButton = priceButton
        
    def showButton(self):

        self.surf.fill(self.buttonColor)
        self.sc.blit(self.surf,self.surfRect)

    def showTextButton(self):

        self.textImg = self.font.render(str(self.textButton), True, self.textColor, self.buttonColor)
        self.textRect = self.textImg.get_rect()
        self.textRect.centerx = self.surfRect.centerx
        self.textRect.centery = self.surfRect.centery 
        self.sc.blit(self.textImg, self.textRect)

        self.priceImg = self.font.render(str(self.priceButton), True, self.textColor, self.buttonColor)
        self.priceRect = self.priceImg.get_rect()
        self.priceRect.centerx = self.surfRect.centerx
        self.priceRect.centery = self.surfRect.centery
        self.priceRect.bottom = self.surfRect.bottom  - 15
        self.sc.blit(self.priceImg, self.priceRect)