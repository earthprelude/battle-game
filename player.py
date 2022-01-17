import random
import time


class Player:
    
    """
    A class used to represent a Player.

    Attributes
    ----------
    name : str
        the name of the player
    health : int
        the health of the player (default 100)
    energy : int
        the energy level of the player (default 1)
    moves: dictionary 
        the keys are move names (strings), the values are methods available to the player
        
    Methods
    -------
    status() prints the player's name and health
    show_moves() prints out a list of moves available to player 
    attack() lowers health of enemy player 
    heal() increases player's own health
    
    """

    def __init__(self, name="Player"):      
        """ __init__() method initializes new instance (object) of Player class. 
      
        Parameters
        ----------
        name : str (optional)
            The name of the player (default is "Player")
        """
        self.name = name
        self.health = 100
        self.energy = 1
        self.moves = {"attack": self.attack, "heal": self.heal}
        self.image = ""

    def status(self): 
        """ status() method prints out a Player's name and health properties"""
        print(self.name, " health: ", self.health)
    
    def show_moves(self): 
        """ show_moves() prints out list of keys (move names) in moves dictionary"""
        print(self.name, "moves:")
        for move_name in self.moves.keys(): 
          print(move_name)

    def attack(self, enemy, damage=None):
        """ attack() method lowers health of enemy player. 
      
        Parameters
        ----------
        enemy : Player object

        damage: int (optional)
            Amount subtracted from enemy player health.
            If not provided, a random integer is chosen for damage.
            """
            
        if not damage:                       # if there is no 2nd argument
            damage = random.randint(20, 40)  # random integer for damage
        damage *= self.energy                # multiply by energy

        enemy.health -= damage
        print(self.name+"'s attack did", damage, "damage to", enemy.name)


    def heal(self, enemy=None):
        """ heal() method increases player's own health. 
        
        Parameters
        ----------
        enemy : Player object (optional)
        """ 
        n = random.randint(25, 40)        # random number for health increase
        n *= self.energy                  # multiplied by energy level
        self.health += n
        print(self.name, "healed self", n)
        
        
 
