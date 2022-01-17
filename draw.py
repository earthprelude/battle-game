import turtle 
from player import * 

# set up window
screen = turtle.Screen()
screen.setup(400, 400)
screen.bgcolor("gray")

# user turtle
u = turtle.Turtle() 
u.ht() 
u.left(90)
u.penup() 
u.goto(-100, -80)
u.color("white")

# bot turtle 
b = turtle.Turtle()
b.left(90)
b.ht() 
b.penup() 
b.goto(100, 80)
b.color("white")

def show_turtle(t, image): 
    screen.register_shape(image)
    t.shape(image)
    t.showturtle()

def show_user(user): 
    show_turtle(u, user.image) 
  
def show_bot(bot): 
    show_turtle(b, bot.image)
  
def update_bot(bot): 
    b.clear()
    b.goto(-30, 80)
    b.write(bot.health, font=("Arial", 30, "bold"))
    b.goto(100, 80)
  
def move_user(): 
    u.goto(b.pos())
    u.goto(-100, -80)
  
def move_bot(): 
    b.goto(u.pos())
    b.goto(100, 80)
  
def update_user(user): 
    u.clear() 
    u.goto(0, -80)
    u.write(user.health, font=("Arial", 30, "bold"))
    u.goto(-100, -80)
  
def draw_update(user, bot): 
    update_user(user)
    update_bot(bot)
