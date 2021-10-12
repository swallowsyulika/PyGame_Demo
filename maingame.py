
import pygame
from settings import Settings
from swallow import Sw
from monster import Monster
from gameset import Gameset
from button import Button
import gf
from pygame.sprite import Group


def run_game():
    #foundational set
    pygame.init()
    
    
    sets = Settings()
    win = pygame.display.set_mode((sets.screen_width,sets.screen_height))
     
    pygame.display.set_caption("Justgame")
    st = Gameset(sets)
    pyton = Button(sets,win,"Play")
    #make
    sw = Sw(sets,win)
    bullets = Group()
    cats = Group()
    gf.create_team(sets,win,sw,cats)
    
#    pygame.mixer.init()
#    pygame.mixer.music.load('KDA.mp3')
#    pygame.mixer.music.play()
 
    #starting main loop
    while True:
        
        gf.check_event(sw,sets,win,bullets,st,pyton,cats)
        if st.game_act:
            sw.swupdate()
            gf.updatabullet(bullets,sets,win,sw,cats)
            gf.cats_updata(sets,sw,cats,st,win,bullets)
        gf.fps(sets,win,sw,bullets,cats,st,pyton)

run_game()
