import pygame

class Upgrade():

    def __init__(self, sc, textUpgradeButton, textColor, sizeButton):

        self.buttonUpgColor = (0,255,100)
        self.textColor = textColor
        self.sc = sc
        self.surf = pygame.Surface((sizeButton))
        self.surfRect = self.surf.get_rect()
        self.surfRect.centerx = 200
        self.surfRect.centery = 400
        self.font = pygame.font.SysFont(None, 18)
        self.textUpgButton = textUpgradeButton
        self.priceButton = 10
        
    def showUpgButton(self):

        self.surf.fill(self.buttonUpgColor)
        self.sc.blit(self.surf,self.surfRect)

    def showTextUpgButton(self):

        self.textImg = self.font.render(str(self.textUpgButton), True, self.textColor, self.buttonUpgColor)
        self.textRect = self.textImg.get_rect()
        self.textRect.centerx = self.surfRect.centerx
        self.textRect.centery = self.surfRect.centery 
        self.sc.blit(self.textImg, self.textRect)

        self.priceImg = self.font.render(str(self.priceButton), True, self.textColor, self.buttonUpgColor)
        self.priceRect = self.textImg.get_rect()
        self.priceRect.right = self.surfRect.right + 25
        self.priceRect.centery = self.surfRect.centery + 10
        self.sc.blit(self.priceImg, self.priceRect)