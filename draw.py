import turtle 
from player import * 

# Constants
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400
USER_X = -160
USER_Y = -80
BOT_X = 160 
BOT_Y = 80
LUNGE = 50
SLIDE = 100
TURN = 45

# set up window
screen = turtle.Screen()
screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
screen.bgcolor("black")

# user turtle
u = turtle.Turtle() 
u.ht() 
u.left(90)
u.penup() 
u.goto(USER_X, USER_Y)
u.color("white")

# bot turtle 
b = turtle.Turtle()
b.left(90)
b.ht() 
b.penup() 
b.goto(BOT_X, BOT_Y)
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
    b.goto(BOT_X - SLIDE - LUNGE, BOT_Y)
    b.write(bot.health, font=("Arial", 30, "bold"))
    b.goto(BOT_X, BOT_Y)
  
def move_user(): 
    u.goto(USER_X + LUNGE, USER_Y + LUNGE)
    u.right(TURN)
    u.left(TURN)
    u.goto(USER_X, USER_Y)
  
def move_bot(): 
    b.goto(BOT_X - LUNGE, BOT_Y - LUNGE)
    b.left(TURN)
    b.right(TURN)
    b.goto(BOT_X, BOT_Y)
  
def update_user(user): 
    u.clear() 
    u.goto(USER_X + SLIDE, USER_Y)
    u.write(user.health, font=("Arial", 30, "bold"))
    u.goto(USER_X, USER_Y)
  
def draw_update(user, bot): 
    update_user(user)
    update_bot(bot)
