import pygame.font

class Button():

    def __init__(self,sets,win,msg):
        """Button."""
        self.win = win
        self.win_rect = win.get_rect()

        self.width,self.height = 200,50
        self.button_color = (255,153,18)
        self.text_color = (255,255,255)
        self.font = pygame.font.SysFont(None,48)

        self.rect = pygame.Rect(0,0,self.width,self.height)
        self.rect.center = self.win_rect.center

        self.puts_msg(msg)

    def puts_msg(self,msg):
        """puts msg."""
        self.msg_image = self.font.render(msg,True,self.text_color,
                                          self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        """Draw button."""
        self.win.fill(self.button_color,self.rect)
        self.win.blit(self.msg_image,self.msg_image_rect)
