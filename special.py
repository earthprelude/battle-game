from player import Player
import time, random

class Spiderman(Player): 
  def __init__(self):
    Player.__init__(self, "Spiderman") 
    self.moves["web shooter"] = self.web_shooter
    self.image = "images/spideycartoon.gif"
    self.special = 2
    
  def web_shooter(self, enemy):
    self.attack(enemy, 40)
      

class Voldemort(Player): 
  def __init__(self):
    Player.__init__(self, "Voldemort") 
    self.image = "images/voldemort_small.gif"
    self.moves.pop("attack")
    self.moves["killing curse"] = self.avadakedavra
    self.moves["regeneration"] = self.heal
    
  def avadakedavra(self, enemy): 
    print("AVADA KEDAVRA!")
    time.sleep(1)
    if random.randint(0, 3): 
      self.attack(enemy, 50)
    else: 
      print("Voldemort's curse rebounded!")
      self.attack(self, 50)

    
class Thanos(Player): 
  def __init__(self):
    Player.__init__(self, "Thanos")
    self.image = "images/thanos.gif"
    self.moves["smash"] = self.attack
    self.moves["Thanos Snap"] = self.finger_snap
    self.moves.pop("attack")
    self.moves.pop("heal")
 
  def finger_snap(self, enemy): 
    damage = round(enemy.health / 2) 
    self.attack(enemy, damage)
    n = random.uniform(0, self.health/2)
    self.attack(self, round(n))
    
    

  def __init__(self):
    Player.__init__(self, "Elsa") 
    self.moves["ice blast"] = self.ice_blast
  def ice_blast(self, enemy): 
    self.attack(enemy, 30)
    self.heal(enemy, 10)
    
class Jedi(Player): 
  def __init__(self):
    Player.__init__(self, "Jedi")
    self.moves.pop("attack") 
    self.moves["lightsaber slash"] = self.attack
    self.moves["force whirlwind"] = self.force_attack
    self.moves["battlemind"] = self.force_mind
    self.image = "images/rey.gif"
    self.specialmove = 2
    self.energy += 0.1
  def lightsaber(self, enemy): 
    self.attack(enemy, 40)
  def force_mind(self, enemy): 
  
    self.energy += 0.2
    print("Meditation increases the concentration and willpower of " + self.name)
    print(self.name + " has increased energy.")
    if self.energy >= 1.8: 
      self.moves.pop("battlemind")
      
  def force_attack(self, enemy): 
    self.attack(enemy, 60)
    self.specialmove -= 1
    if self.specialmove > 0: 
      print(str(self.specialmove) + " time left to use this move.")
    else: 
      self.moves.pop("force whirlwind")



class Pikachu(Player):
    def __init__(self):
        Player.__init__(self, "Pikachu")
        self.image = "images/pikachu_small.gif"
        self.moves["thunder shock"] = self.thunder_shock
        self.moves.pop("attack")
        self.moves["quick attack"] = self.attack

    # special move
    def thunder_shock(self, enemy):
        damage = random.randint(40, 50)  # strong attack
        self.attack(enemy, damage)
        if random.randint(0, 1):         # 50% chance 
            self.health -= 10            # lowers his own health! 
            
    def evolve(self):                   # option to evolve into next level.
        print("Pikachu evolves into Raichu!")
        self.name = "Raichu"
        self.health += 20
        self.energy += 1 
        self.moves["electro ball"] = self.electro_ball
        
    def electro_ball(self, enemy): 
        self.attack(enemy, 80)      # super strong attack 