import sys
import pygame as pg
class InputBox:
    
    def __init__(self, x, y, w, h, text=''):
        self.rect = pg.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:# ทำการเช็คว่ามีการคลิก Mouse หรือไม่
            if self.rect.collidepoint(event.pos): #ทำการเช็คว่าตำแหน่งของ Mouse อยู่บน InputBox นี้หรือไม่
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE # เปลี่ยนสีของ InputBox
            
        if event.type == pg.KEYDOWN:
            if self.active:
                if event.key == pg.K_RETURN:
                    print(self.text)

                elif event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                
                else:
                    # if input_box_first_name.active or input_box_last_name.active or input_box_age.active:
                    self.text += event.unicode
                    
                # Re-render the text.
                self.txt_surface = FONT.render(self.text, True, self.color)

    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, Screen):
        # Blit the text.
        Screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pg.draw.rect(Screen, self.color, self.rect, 2)


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
    
    def isMouseOn(self):
         # get mouse position
        mouse_pos = pg.mouse.get_pos()
        
        # check if mouse is on button
        if self.x < mouse_pos[0] < self.x + self.w and \
           self.y < mouse_pos[1] < self.y + self.h:
            return True
        else:
            return False
    
    def isClicked(self):
        # check if left mouse button is down while mouse is on button
        if self.isMouseOn() and pg.mouse.get_pressed()[0]:
            return True
        else:
            return False

class Textbox(InputBox):
    def __init__(self,x=0,y=0,text = "",textsize = 22,textcolor = (0,0,0),font = None):
        self.x = x
        self.y = y
        self.text = text
        self.textsize = textsize
        self.textcolor = textcolor
        self.font = font
       
    def show_text(self,Screen):
        text_surface = FONT.render(self.text,True,self.textcolor)
        text_rect = text_surface.get_rect()
        text_rect.topleft = (self.x, self.y)
        Screen.blit(text_surface, text_rect)
        

pg.init()

win_x, win_y = 800, 480
white = (255, 255, 255)
black = (0,0,0)
green = (124,252,0)
red = (255,0,0)
screen = pg.display.set_mode((win_x, win_y))

submit_button = Button(90,345,100,30,green) # สร้าง Object จากคลาส Button ขึ้นมา
text = ""
# rec = Rectangle()


COLOR_INACTIVE = pg.Color('lightskyblue3') # ตั้งตัวแปรให้เก็บค่าสี เพื่อนำไปใช้เติมสีให้กับกล่องข้อความตอนที่คลิกที่กล่องนั้นๆอยู่
COLOR_ACTIVE = pg.Color(black)     # ^^^
FONT = pg.font.Font(None, 32)


input_box_first_name = InputBox(100, 120, 140, 32)
input_box_last_name = InputBox(100, 200, 140, 32)
input_box_age = InputBox(100, 280, 140, 32)
input_boxes = [input_box_first_name,input_box_last_name, input_box_age ] # เก็บ InputBox ไว้ใน list เพื่อที่จะสามารถนำไปเรียกใช้ได้ง่าย


# font = pg.font.Font('freesansbold.ttf', 32) # font and fontsize
# font_ans = pg.font.Font('freesansbold.ttf', 22)
# text_first_name = font.render('First name', True, black, white) # (text,is smooth?,letter color,background color)
# text_last_name = font.render('Last name', True, black, white)
# text_age = font.render('Age', True, black, white)
# text_submit = font.render('Submit',True,black,green)

text_head_line = Textbox(330,40,"Personal form",40)

text_first_name = Textbox(100,90,"Firstname",32)
text_last_name = Textbox(100,170,"Lastname",32)
text_age = Textbox(100,250,"Age",32)
text_submit = Textbox(100,350,"Submit",32)
text_boxes = [text_first_name,text_last_name,text_age,text_submit]

output_text = Textbox(100,400,"",22)


run = True
while run:
    screen.fill(white)
    submit_button.draw(screen)
    # screen.blit(text_first_name,(100,50))
    # screen.blit(text_last_name,(100,150))
    # screen.blit(text_age,(100,250))
    # screen.blit(text_submit,(100,350))
    
    text_head_line.show_text(screen)

    for box in input_boxes: # ทำการเรียก InputBox ทุกๆตัว โดยการ Loop เข้าไปยัง list ที่เราเก็บค่า InputBox ไว้
        box.update() # เรียกใช้ฟังก์ชัน update() ของ InputBox
        box.draw(screen) # เรียกใช้ฟังก์ชัน draw() ของ InputBox เพื่อทำการสร้างรูปบน Screen

    for show in text_boxes:
        show.show_text(screen)
    
    output_text.show_text(screen)

    # ans = f"Hello {input_box_first_name.text} {input_box_last_name.text}! You are {input_box_age.text} years old."
    # if submit_button.isClicked():
    #     if input_box_first_name.text == '' and input_box_last_name.text == '' and input_box_age.text == '':
    #         ans_submit = font_ans.render("Please text in box.",True,black,white)
    #         screen.blit(ans_submit, (100,400))
    #     elif input_box_age.text.isdigit():
    #         ans_submit = font_ans.render(ans,True,black,white)
    #         screen.blit(ans_submit, (100,400))
    #         # print(f"Hello {input_box_first_name.text} {input_box_last_name.text}! You are {input_box_age.text} years old.")
    #     else:
    #         ans_submit = font_ans.render("Please text in Age box.",True,red,white)
    #         screen.blit(ans_submit, (100,400))
    #         # print("Please enter a valid age (numbers only).")

    if submit_button.isClicked():
            if input_box_age.text.isdigit():
                output_text.text = f"Hello {input_box_first_name.text} {input_box_last_name.text}! You are {input_box_age.text} years old."
            # if not input_box_first_name.text.isalpha() or not input_box_last_name.text.isalpha():
            #     output_text.textcolor = red
            #     output_text.text = "Please enter a valid name in the Firstname or Lastname box (alphabet only)"
            if not input_box_age.text.isdigit():
                output_text.textcolor = red
                output_text.text = "Please enter a valid age in the Age box (numbers only)."
    
    for event in pg.event.get():
        

        for box in input_boxes:
            box.handle_event(event)
        
    
        if event.type == pg.QUIT:
            pg.quit()
            # sys.exit()
            run = False
        
    pg.time.delay(1)
    pg.display.update()
    