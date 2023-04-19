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
        # self.hover_color = hover_color
        # self.click_color = click_color
    
    def isMouseOn(self):
         # get mouse position
        mouse_pos = pg.mouse.get_pos()
        
        # check if mouse is on button
        if self.x < mouse_pos[0] < self.x + self.w and self.y < mouse_pos[1] < self.y + self.h:
            return True
        else:
            return False
    
    def isClicked(self):
        # check if left mouse button is down while mouse is on button
        if self.isMouseOn() and pg.mouse.get_pressed()[0]:
            return True
        else:
            return False
import sys 
import pygame as pg

pg.init()
run = True
win_x, win_y = 800, 480
screen = pg.display.set_mode((win_x, win_y))
btn = Button(20,20,100,100) # สร้าง Object จากคลาส Button ขึ้นมา
rec = Rectangle()

while(run):
    screen.fill((255, 255, 255))
    if btn.isClicked():
        btn.color = 255,0,255
    elif btn.isMouseOn():
        btn.color = 128,128,128
    else:
        btn.color = (255,0,0)
    btn.draw(screen)
    
    pg.display.update()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            run = False