import pygame

class Score():

    def __init__(self, sc, stats, bgColor):

        self.bgColor = bgColor
        self.sc = sc
        self.scRect = sc.get_rect()
        self.stats = stats
        self.textColor = (0,0,0)
        self.font = pygame.font.SysFont(None, 36)
        self.ScoreImage()
    
    def ScoreImage(self):

        self.ScoreImg = self.font.render(str(self.stats.score), True, self.textColor, self.bgColor)
        self.scoreRect = self.ScoreImg.get_rect()
        self.scoreRect.centerx = self.scRect.centerx
        self.scoreRect.centery = self.scRect.centery -200

    def showScore(self):

        self.sc.blit(self.ScoreImg, self.scoreRect)