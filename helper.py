import random, time
from draw import *

# added line to draw update with graphics
def status(user, bot): 
  print ("\n" + "-" * 40)
  user.status()
  bot.status() 
  print ("-" * 40)
  draw_update(user, bot)

def user_move(user, bot): 
  print ("Choose a move:")
  for m in user.moves: 
    print (m) 
  answer = input(">") 
  if answer in user.moves: 
    print (user.name, ":",  answer)
    move = user.moves[answer]
    move(bot)
    move_user()
  else: 
    print ("Invalid")
    user_move(user, bot)
  
  time.sleep(1) 
  status(user, bot)

def bot_move(user, bot): 
  print ("Computer's turn...")
  time.sleep(1)
  print("")
  move_name = random.choice(list(bot.moves.keys()))
  move = bot.moves[move_name]
  print (bot.name, ":", move_name)
  move(user)
  move_bot()
  time.sleep(1)
  status(user, bot)