import pygame

class Button():

    def __init__(self, sc, textButton, textColor):

        self.buttonColor = (0,255,200)
        self.textColor = textColor
        self.sc = sc
        self.surf = pygame.Surface((50,50))
        self.surfRect = self.surf.get_rect()
        self.surfRect.centerx = 100
        self.surfRect.centery = 400
        self.font = pygame.font.SysFont(None, 24)
        self.textButton = textButton
        
    def showButton(self):

        self.surf.fill(self.buttonColor)
        self.sc.blit(self.surf,self.surfRect)

    def showTextButton(self):

        self.textImg = self.font.render(str(self.textButton), True, self.textColor, self.buttonColor)
        self.textRect = self.textImg.get_rect()
        self.textRect.centerx = self.surfRect.centerx
        self.textRect.centery = self.surfRect.centery 
        self.sc.blit(self.textImg, self.textRect)