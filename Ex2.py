class Rectangle:
    def __init__(self,x=0,y=0,w=0,h=0, color=(255,0,0)):
        self.x = x # Position X
        self.y = y # Position Y
        self.w = w # Width
        self.h = h # Height
        self.color = color # Color
    def draw(self,screen):
        pg.draw.rect(screen,self.color,(self.x,self.y,self.w,self.h))

class Button(Rectangle):
    def __init__(self, x=0, y=0, w=0, h=0, color=(255,0,0)):
        Rectangle.__init__(self, x, y, w, h,color)

import sys 
import pygame as pg

pg.init()
run = True
win_x, win_y = 800, 480
screen = pg.display.set_mode((win_x, win_y))
btn = Button(340,180,100,100) # สร้าง Object จากคลาส Button ขึ้นมา
rec = Rectangle()

w_up = False
s_down = False
d_right = False
a_left = False

while(run):
    screen.fill((255, 255, 255))
    for event in pg.event.get():
        
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

        if event.type == pg.KEYDOWN and event.key == pg.K_w:
            # print("Key W up")
            w_up = True
            # btn.y -= 100
        if event.type == pg.KEYUP and event.key == pg.K_w:
            w_up = False

        if event.type == pg.KEYDOWN and event.key == pg.K_s: 
            # print("Key S down")
            s_down = True
            # btn.y += 100
        if event.type == pg.KEYUP and event.key == pg.K_s:
            s_down = False

        if event.type == pg.KEYDOWN and event.key == pg.K_d: 
            # print("Key D right")
            d_right = True
            # btn.x += 100
        if event.type == pg.KEYUP and event.key == pg.K_d: 
            d_right = False
        
        if event.type == pg.KEYDOWN and event.key == pg.K_a: 
            # print("Key A reft")
            a_left = True
            # btn.x -= 100
        if event.type == pg.KEYUP and event.key == pg.K_a: 
            a_left = False
    
    if w_up == True:
        btn.y -= 0.1
    if s_down == True:
        btn.y +=0.1
    if a_left == True:
        btn.x -=0.1
    if d_right == True:
        btn.x += 0.1

        
    btn.draw(screen)
    
    pg.display.update()
pg.quit()
sys.exit