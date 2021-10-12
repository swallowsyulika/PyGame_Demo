import sys
import pygame
from bullet import Bullet
from monster import Monster
from time import sleep

def check_event_down(event,sw,sets,win,bullets):
    """Respond to keydown"""
    if event.key == pygame.K_RIGHT:
        sw.mr = True
    elif event.key == pygame.K_LEFT:
        sw.ml = True
    elif event.key == pygame.K_SPACE:
        fire(sets,win,sw,bullets)
    elif event.key == pygame.K_ESCAPE:
        pygame.quit()
        sys.exit()
        
def check_event_up(event,sw):
    """Respond to keydup"""
    if event.key == pygame.K_RIGHT:
        sw.mr = False
    elif event.key == pygame.K_LEFT:
        sw.ml = False

def check_event(sw,sets,win,bullets,st,pyton,cats):
    #this loop will enter any keyboard and mouse event
    for event in pygame.event.get():
            
        #when click X to close
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        #move
        elif event.type == pygame.KEYDOWN:
            check_event_down(event,sw,sets,win,bullets)               
        elif event.type == pygame.KEYUP:
            check_event_up(event,sw)
        #play?
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x,mouse_y = pygame.mouse.get_pos()
            check_play(st,pyton,mouse_x,mouse_y,sets,win,sw,bullets,cats)

def boom(sets,win,sw,cats,bullets):
    #if bullets hit cats
    boom = pygame.sprite.groupcollide(bullets,cats,True,True)
                                     # A       B    >X  >X
    if len(cats) == 0:    #if cats team are 0
        bullets.empty()
        create_team(sets,win,sw,cats)

def updatabullet(bullets,sets,win,sw,cats):
    #let bullets move
    for i in bullets:
        i.buupdata()
    for bullet in bullets.copy():
        if bullet.rect.bottom <=0 :
            bullets.remove(bullet)
    boom(sets,win,sw,cats,bullets)
    
def fire(sets,win,sw,bullets):
    #fire the bullets
    if len(bullets) < sets.bullet_num:
            new_bullet = Bullet (sets,win,sw)
            bullets.add(new_bullet)

def get_num_cats_x(sets,cat_width):
    #get how many cats in the team
    able_space_x = sets.screen_width - 2 * cat_width
    num_cats_x = int(able_space_x / (2 * cat_width))
    return num_cats_x

def get_num_cats_y(sets,cat_height,sw_height):
    #get how many row in the screen
    able_space_y = (sets.screen_height - (3 * cat_height) - sw_height)
    num_cats_y = int(able_space_y / (2 * cat_height))
    return num_cats_y

def create_cat(sets,win,cats,xnum,ynum):
    #creat single cat and add to team
    cat = Monster(sets,win)
    cat_width = cat.rect.width
    cat.x = cat_width + 2 * cat_width * xnum
    cat.rect.x = cat.x
    cat.rect.y = cat.rect.height + 2 * cat.rect.height * ynum
    cats.add(cat)
    
def create_team(sets,win,sw,cats):
    #create a team of cats
    cat = Monster(sets,win)
    xnum_cats = get_num_cats_x(sets,cat.rect.width)
    ynum_cats = get_num_cats_y(sets,cat.rect.height,sw.rect.height)

    for ynum in range(ynum_cats - 1):  #too many
        for xnum in range(xnum_cats):
            create_cat(sets,win,cats,xnum,ynum)

def check_team_edges(sets,cats):
    #if cats team edges then change direction
    for cat in cats.sprites():
        if cat.check_edges():
            change_direction(sets,cats)
            break
def change_direction(sets,cats):
    #change direction
    for cat in cats.sprites():
        cat.rect.y += sets.cat_drop_speed
    sets.team_direction *= -1

def sw_hit(sets,sw,cats,st,win,bullets):
    #if sw is hit
    if st.sw_left > 0:
        st.sw_left -= 1
    
        cats.empty()
        bullets.empty()

        create_team(sets,win,sw,cats)
        sw.center_sw()
        
        sleep(0.5)
    else:
        st.game_act = False
        pygame.mouse.set_visible(True)
        
def check_cats_bottom(sets,sw,cats,st,win,bullets):
    #if cats team touch the bottom
    win_rect = win.get_rect()
    for cat in cats.sprites():
        if cat.rect.bottom >= win_rect.bottom:
            sw_hit(sets,sw,cats,st,win,bullets)
            break
    
def cats_updata(sets,sw,cats,st,win,bullets):
    #let cats move
    check_team_edges(sets,cats)
    for i in cats:
        i.moupdata()
    if pygame.sprite.spritecollideany(sw,cats):
        sw_hit(sets,sw,cats,st,win,bullets)
    check_cats_bottom(sets,sw,cats,st,win,bullets)

def check_play(st,pyton,mouse_x,mouse_y,sets,win,sw,bullets,cats):
    button_clicked = pyton.rect.collidepoint(mouse_x,mouse_y)
    if button_clicked and not st.game_act:
        pygame.mouse.set_visible(False)
        st.reset()
        st.game_act = True
        cats.empty()
        bullets.empty()
        create_team(sets,win,sw,cats)
        sw.center_sw()
        
def fps(sets,win,sw,bullets,cats,st,pyton):
    win.fill(sets.bgc)
    for bullet in bullets.sprites():
        bullet.putsbullet()
    sw.putsswallow()
    cats.draw(win)
    if not st.game_act:
        pyton.draw_button()
    
    #fps
    pygame.display.flip()
