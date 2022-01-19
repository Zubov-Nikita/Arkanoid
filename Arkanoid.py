# coding: utf8\
from tkinter import *
import random


class Block :
    width=30
    height=80
    color='red'
    x_block=0
    y_block=0
    render_object=0
    
    def __init__(self,color,x_block,y_block):
        self.color=color
        self.x_block=x_block
        self.y_block=y_block
    def render(self):
        self.render_object=conv.create_rectangle(self.x_block,self.y_block,self.x_block+self.height,self.y_block+self.width,fill=self.color,outline='white')
    def __del__(self):
        conv.delete(self.render_object)   
def add_point():
    global score_count
    score_count=score_count+10
    conv.itemconfig(score,text=str(score_count))       
    



root = Tk()
root.title("Арканоид")
conv = Canvas (root, width=800, height=800, bg='Black') #конва

score_count=0                                           #счётчик

pole=conv.create_rectangle(0,0,800,650,fill='Black')    #поле

conv.create_rectangle(0,650,805,805,fill='gray')        #инф
ball = conv.create_oval(396,590,410,604,fill="Yellow")  #шарик   
okno=0
def exid_mes():
    root.destroy()
    okno.destroy()


def gameover_message(label):
    global okno

    okno=Tk()
    okno.title("okno")
    okno.geometry("300x100")
    okno.config(bg="white")
    
    label=Label(okno,text=label,font="Arial 16",fg="Black",bg="white")
    label.pack()

    button=Button(okno,text="Попробовать снова",command=restart)
    button.config(width=20,height=2,bg="green",fg="blue")
    button.pack()

    button_exit_mes=Button(okno,text="Выход",command=exid_mes)
    button_exit_mes.config(width=20,height=2,bg="red",fg="blue")
    button_exit_mes.pack()   
    
    
    

def render_blocks():
    global blocks
    blocks=[]
   
    xCreate=0
    yCreate=0
   
    for i in range(80):
        block=Block('red',xCreate,yCreate)
        block.render()
        blocks.append(block)
        xCreate=xCreate+80
        if xCreate==800:
            xCreate=0
            yCreate=yCreate+30
    

board=conv.create_rectangle(325,600,475,625,fill='white')




score = conv.create_text(750,710, text=str(score_count),font="Arial 30", fill="white")
conv.create_text(750,670, text=("Очки"),font="Arial 30", fill="white")



bord_old_coords = conv.coords(board)
ball_old_coords = conv.coords(ball)

bord_old_coords = conv.coords(board)
ball_old_coords = conv.coords(ball)

ball_speed_y=-7
spid = [-7,-6,-5,-4,-3,-2,-1,1, 2, 3, 4, 5, 6, 7, 8]
ball_speed_x=random.choice(spid)

    
game_flag = 0
def move_ball():
    global ball_speed_x,ball_speed_y,game_flag,blocks
    
    
    conv.move(ball,ball_speed_x,ball_speed_y)
    
    delta=7
    ball_x1=conv.coords(ball)[0]
    ball_y1=conv.coords(ball)[1]
    ball_x2=conv.coords(ball)[2]
    ball_y2=conv.coords(ball)[3]
    ball_x_center=(ball_x1+ball_x2)/2
    ball_y_center=(ball_y1+ball_y2)/2

    board_x1=conv.coords(board)[0]
    board_y1=conv.coords(board)[1]
    board_x2=conv.coords(board)[2]
    board_y2=conv.coords(board)[3]

   
    

    if ball_x1 <= conv.coords(pole)[0]:                 #левкрай
        ball_speed_x=random.randint(4,7)
        
    if ball_y1 <=conv.coords(pole)[1]:                 #верхкрай 
        ball_speed_y=ball_speed_y*-1
        
    if ball_x2 >= conv.coords(pole)[2]:                #правкрай
        ball_speed_x=random.randint(-7,-4)

        
    if ball_y2 >= conv.coords(pole)[3]:                 #низкрай
        game_flag=0
        gameover_message("Вы проиграли =( увы ")

        

    if board_x1 <= ball_x_center <= board_x2 and board_y1 <= ball_y2 <= board_y1 + delta : #борд касание верха
        ball_speed_y=ball_speed_y*-1
        
      

    if board_y1 <= ball_y_center <=board_y2 and board_x2 <= ball_x1 <= board_x2 + delta: #борд касание право
        
        ball_speed_x=ball_speed_x*-1
    
    if board_y1 <= ball_y_center <=board_y2 and board_x1 -delta <= ball_x2  <= board_x1:  #борд касание лево
        
        ball_speed_x=ball_speed_x*-1

    for block in blocks :
        
        block_x1=conv.coords(block.render_object)[0]
        block_y1=conv.coords(block.render_object)[1]
        block_x2=conv.coords(block.render_object)[2]
        block_y2=conv.coords(block.render_object)[3]
        
        if block_x1-delta<= ball_x_center <= block_x2  + delta and block_y2<= ball_y1<= block_y2+ delta: #блок касание низ
            ball_speed_y=ball_speed_y*-1
          
            blocks.remove(block)
            add_point()
            break
        
        if block_y1-delta <= ball_y_center <=block_y2 +delta and block_x2-delta <= ball_x1 <= block_x2+ delta: #блок касание право
        
            ball_speed_x=ball_speed_x*-1
            blocks.remove(block)
            add_point()
            break
            
        
        if block_y1 -delta <= ball_y_center <=block_y2 + delta and  block_x1-delta <= ball_x2<= block_x2+delta: #блок касание лева
            
            ball_speed_x=ball_speed_x*-1
            blocks.remove(block)
            add_point()
            break
   
        if block_x1-delta <= ball_x_center <= block_x2  + delta and block_y1-delta<= ball_y2<= block_y1: #блок касание верх
            ball_speed_y=ball_speed_y*-1
            blocks.remove(block)
            add_point()
            break
                   
board_speed=0
def move_board():
    if (board_speed > 0) and (conv.coords(board)[2]<795):
        conv.move(board,board_speed,0)
    elif (board_speed < 0) and (conv.coords(board)[0]>5):
        conv.move(board,board_speed,0)
        

def button_up(event): 
    global board_speed
    board_speed=0 
conv.bind("<KeyRelease>",button_up)   

def batton_on(event):
    global game_flag,board_speed,score_count,ball_speed_x,ball_speed_y
    #print (event.keysym)
    
    if event.keysym=="Left":
        board_speed=-10
    elif event.keysym=="Right":
        board_speed=10
def restart():  
    global game_flag,board_speed,score_count,ball_speed_x,ball_speed_y,okno
    score_count=0
    conv.itemconfig(score,text=str(score_count))
    board_speed=0
    conv.coords(board,bord_old_coords[0],bord_old_coords[1],bord_old_coords[2],bord_old_coords[3])
    ball_speed_y=-7
    ball_speed_x=random.randint(-7,4)
    conv.coords(ball,ball_old_coords[0],ball_old_coords[1],ball_old_coords[2],ball_old_coords[3])
    game_flag=1  
    render_blocks()
    main()
    okno.destroy()
        
conv.bind("<KeyPress>",batton_on)
conv.focus_set()

game_flag = 1
def main():
    global blocks,game_flag
    move_board()
    move_ball()
    if len(blocks)==0:
        gameover_message("Вы выиграли =) поздравляем")
        game_flag = 0
        
    if game_flag == 1 :
        root.after(30,main)

button_exit=Button(root,text="Выход",command=root.destroy)
button_exit.config(width=20,height=2,bg="green",fg="blue")
button_exit.place(x=650, y=750)

render_blocks()          
main()
conv.pack()
root.mainloop()

okno.mainloop()

render_blocks() 
