import random, time
from draw import *

"""
Displays the current status of two Player objects. 
----------
user : Player object 
bot : Player object
"""
def status(user, bot): 
  print ("\n" + "-" * 40)
  user.status()
  bot.status() 
  print ("-" * 40)
  draw_update(user, bot)

"""
Allows the user to select a move, and does that move against the bot Player.
----------
user : Player object 
bot : Player object
"""  
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

"""
Selects a random move for the bot Player against the user Player. 
----------
user : Player object 
bot : Player object
""" 
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
