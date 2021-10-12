import pygame
from pygame.sprite import Sprite

class Monster(Sprite):
    """monster create."""

    def __init__(self,sets,win):
        """monster settings."""
        super(Monster,self).__init__()
        self.win = win
        self.sets = sets
        #make
        self.image = pygame.image.load('monster.png')
        self.rect = self.image.get_rect()
        #set
        self.rect.x=self.rect.width
        self.rect.y=self.rect.height

        self.x = float(self.rect.x)

    def check_edges(self):
        win_rect = self.win.get_rect()
        if self.rect.x >= win_rect.right:
            return True
        elif self.rect.x <= 0 :
            return True
        
    def moupdata(self):
        """monster moving."""
        cat_speed = float(self.sets.cat_speed)
        self.x += cat_speed * self.sets.team_direction
        self.rect.x = self.x        
        
    
