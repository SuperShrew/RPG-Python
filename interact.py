import os
import time
from dialog import *
def inter(map, coords, level_num, inventory, items):
  if map[0][3] == "@" and level_num == 1 and not("WOODEN SWORD" in inventory) or map[1][2] == "@" and level_num == 1 and not("WOODEN SWORD" in inventory) or map[2][3] == "@" and level_num == 1 and not("WOODEN SWORD" in inventory):
    old_man()
    return "old_man"
  elif map[0][3] == "@" and level_num == 1 and "WOODEN SWORD" in inventory or map[1][2] == "@" and level_num == 1 and "WOODEN SWORD" in inventory or map[2][3] == "@" and level_num == 1 and "WOODEN SWORD" in inventory:
    print("old man: hi")
    input("> ")
    return "old_man"
  elif map[2][0] == "@" and level_num == 1 or map[3][1] == "@" and level_num == 1:
    door()
    return "door_1"
  elif map[1][2] == "@" and level_num == 2 or map[0][1] == "@" and level_num == 2 or map[0][3] == "@" and level_num == 2:
    door()
    return "door_2"
  elif map[3][0] == "@" and level_num == 2 and map[2][0] == "*" or map[2][1] == "@" and level_num == 2 and map[2][0] == "*" or map[1][0] == "@" and level_num == 2 and map[2][0] == "*":
    print("you found SHARP QUARTZ CRYSTAL")
    input("> ")
    return "add_item_1"
  elif map[2][3] == "@" and level_num == 2 or map[3][2] == "@" and level_num == 2:
    door()
    return "door_3"
  elif map[2][2] == "@" and level_num == 2 and map[2][3] == "+" or map[1][2] == "@" and level_num == 2 and map[2][3] == "+":
    return "enemy_1"
  try:
    if map[0][1] == "@" and level_num == 3:
      door()
      return "door_4"
    elif map[1][1] == "@" and level_num == 3:
      return "lever_1"
    elif map[2][1] == "@" and level_num == 3:
      return "lever_2"
    elif map[3][1] == "@" and level_num == 3:
      return "lever_3"
    elif map[4][1] == "@" and level_num == 3:
      return "lever_4"
    elif map[1][3] == "@" and level_num == 3 and map[1][4] == "*" or map[2][4] == "@" and level_num == 3 and map[1][4] == "*":
      return "item_2"
    elif map[1][4] == "@" and level_num == 3 or map[0][3] == "@" and level_num == 3:
      return "shop_1"
    elif map[4][3] == "@" and level_num == 3 or map[3][4] == "@" and level_num == 3:
      return "door_5"
  except:
    pass
