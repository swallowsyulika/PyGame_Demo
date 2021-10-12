import pygame

class Sw():

    def __init__(self,sets,win):
        """foundational swallows."""
        self.win = win
        self.image = pygame.image.load('swallows.png')
        self.sets = sets
        
        self.rect = self.image.get_rect()
        self.win_rect = win.get_rect()
        #location
        self.rect.centerx = self.win_rect.centerx
        self.rect.bottom = self.win_rect.bottom

        self.center = float(self.rect.centerx)
        #moving
        self.mr = False
        self.ml = False

    def swupdate(self):
        """update sw's location to move."""
        if self.mr and self.rect.right < self.win_rect.right:
            self.center += self.sets.sw_speed
        if self.ml and self.rect.left > 0:
            self.center -= self.sets.sw_speed
        self.rect.centerx = self.center

    def putsswallow(self):
        """put it to current location."""
        self.win.blit(self.image,self.rect)

    def center_sw(self):
        self.center = self.win_rect.centerx
    
