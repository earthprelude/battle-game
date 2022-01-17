import random, time
from player import *
from helper import *
from draw import *
from special import *

def get_player(): 
  options = {"Pikachu":Pikachu(), "Spiderman":Spiderman(), "Jedi":Jedi()}
  print("Who do you want to play as?/n")
  for x in options: 
    print(x)
  print("")
  while True:
    choice = input(">")
    if choice in options: 
      return options[choice]
    else:
      print ("Invalid")


def battle(user, bot, level):
  if level == 2: 
    bot = Thanos()
    show_bot(bot)
    
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
    return 
  else: 
    print ("You win!")
    if level == 2: 
      return 
    time.sleep(1)
    print ("/nLevel up.../n")
    time.sleep(1)
    level += 1
    battle(user, bot, level) 

print("Get ready for battle.../n")
user = get_player()
bot = Voldemort()
show_user(user)
show_bot(bot)

level = 1 
battle(user, bot, level)
    
  
    