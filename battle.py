import os
import time
from enemy import *
Game_over = False
def battle(id, inventory, life, items):
  global Game_over
  Game_over = False
  Loop = True
  bool = False
  os.system("clear")
  # Checking which level the enemy is on and which enemy it is
  if id == [2, 1]:
    ENEMY = Enemy("LAND SQUID", 12, 6)
    while Loop:
      print(inventory)
      try:
        weapon = input("choose a weapon from your inventory: ").upper()
        ENEMY.is_attacked((inventory[weapon]), weapon)
      except:
        pass
      if weapon == "SHARP QUARTZ CRYSTAL":
        print("Your SHARP QUARTZ CRYSTAL shattered!")
        input("> ")
        inventory.pop(weapon)
      if ENEMY.is_defeated == False and ENEMY.health > 0:
        print("Enemy Health:", ENEMY.health)
        input("> ")
        life -= ENEMY.attack()
      if ENEMY.is_defeated:
        Loop = False
        bool = True
        items.append("INK SAC")
        items.append("RED HEALTH POTION")
        return life, inventory, items, bool, Game_over
      else:
        print("Health:", life)
        input("> ")
      if life <= 0:
        Game_over = True
        return life, inventory, items, bool, Game_over
