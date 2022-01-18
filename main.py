import random, time
from player import *
from helper import *
from draw import *
from special import *

# gets valid player selection from user  
def get_player(): 
  options = {"Pikachu":Pikachu(), "Spiderman":Spiderman(), "Jedi":Jedi()}
  print(" / ".join(options.keys()))
  while True:
    choice = input(">")
    if choice in options: 
      return options[choice]
    else: 
      print ("Invalid")

# game logic for the battle
def battle(user, bot, level):  
  print ("Your opponent will be...", bot.name)
  status(user, bot)  
  while user.health > 0 and bot.health > 0:
    user_move(user, bot)
    time.sleep(2)
    if bot.health > 0: 
      bot_move(user, bot)
  
  if user.health < 0 and bot.health < 0: 
    print ("Tie!")
  elif user.health < 0: 
    print ("You lose...") 
  else: 
    print ("You win!")
    if level == 2: 
      return 
    else:  
      bot = Thanos()
      show_bot(bot)
    time.sleep(1)
    print ("\nLevel up...\n")
    time.sleep(1)
    level += 1
    battle(user, bot, level) 

# setup 
print("Get ready for battle...\nWho do you choose to play as?")
user = get_player()
bot = Voldemort()
show_user(user)
show_bot(bot)

level = 1 
battle(user, bot, level)
    
  
    
