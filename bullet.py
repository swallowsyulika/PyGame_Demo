import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Build bullet for sw."""
    
    def __init__(self,sets,win,sw):
        """Create a bullet."""
        super(Bullet,self).__init__()
        self.win = win

        #Create a bullet at 0,0 and set correct location
        self.rect = pygame.Rect(0,0,sets.bullet_width,sets.bullet_height)
        self.rect.centerx = sw.rect.centerx
        self.rect.top = sw.rect.top

        #set bullet's y as a float value
        self.y = float(self.rect.y)

        self.color = sets.bullet_color
        self.speed = sets.bullet_speed

    def buupdata(self):
        """Move bullet."""
        self.y -= self.speed  #top y=0
        self.rect.y = self.y

    def putsbullet(self):
        """puts to screen.""" 
        pygame.draw.rect(self.win,self.color,self.rect)
