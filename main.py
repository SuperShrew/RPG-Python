#assigning the game map
map = [["-"]*4, 
       ["-"]*4, 
       ["-"]*4, 
       ["-"]*4]

#importing
import time
import os
import keyboard
from dialog import *
from enemy import *
from game_level import *
from battle import *
from interact import *
from shop import *

#declaring variables
game_over = False
door5_unlocked = False
door3_entered = False
bool1 = bool
shop1_active = False
action = ""
level = Level(map)
level.generate(4, 4)
move = ""
Health = 40
inventory = {}
inventory2 = []
money = 0
id = [2, 1]
coords = [0, 0]
map[coords[0]][coords[1]] = "@"
map[1][3] = "!"
map[3][0] = "#"
collected_item_1 = False
collected_item_2 = False
door1 = False
door2 = False
door3 = False
door4 = False
door5 = False
door6 = False
door7 = False
game_loop1 = True
game_loop2 = False
game_loop3 = False
game_loop4 = False
main_loop = True
lever1A = bool
lever1B  = bool
lever1C = bool
lever1D = bool
shop1 = Shop({"STONE SWORD": 30}, {"RED HEALTH POTION": 25, "KEY1": 15})

#main game loop
while main_loop:

  #checking if player has come through door 2, if they have, then make the map level 1
  if door2:
    door2 = False
    game_loop1 = True
    map = level.generate(4, 4)
    coords = [2, 0]
    map[coords[0]][coords[1]] = "@"
    map[1][3] = "!"
    map[3][0] = "#"
    #start level 1

  while game_loop1:
    move = ""
    #printing map and key
    for o in range(0, level.height):
      print(map[o])
    print("'-' = background, '@' = player, '#' = door, '!' = NPC")
    try:
      #asking for command
      action = input("Use wasd to move \nenter command:\n 1 = interact \n 2 = check inventory \n> ")
    except:
      print("Invalid syntax")
      time.sleep(1)
      os.system("clear")
      #checking that the tile the player wants to move onto exists, and if it does, it checks if it is background
    if action == "w" and coords[0] - 1 > -1 and map[coords[0] - 1][coords[1]] == "-":
      map[coords[0]][coords[1]] = "-"
      coords[0] -= 1
      map[coords[0]][coords[1]] = "@"
    elif action == "s" and coords[0] + 1 < 4 and map[coords[0] + 1][coords[1]] == "-":
      map[coords[0]][coords[1]] = "-"
      coords[0] += 1
      map[coords[0]][coords[1]] = "@"
    elif action == "d" and coords[1] + 1 < 4 and map[coords[0]][coords[1] + 1] == "-":
      map[coords[0]][coords[1]] = "-"
      coords[1] += 1
      map[coords[0]][coords[1]] = "@"
    elif action == "a" and coords[1] - 1 > -1 and map[coords[0]][coords[1] - 1] == "-":
      map[coords[0]][coords[1]] = "-"
      coords[1] -= 1
      map[coords[0]][coords[1]] = "@"
      #action 2
    elif action == "1":
      #assigning the interact function to a variable so it only runs once
      inter_1 = inter(map, coords, 1, inventory, inventory2)
      #adding a wooden sword if inter_1 returns old_man
      if inventory == {} and inter_1 == "old_man":
        inventory["WOODEN SWORD"] = 10
      #stopping the loop for level 1 and setting door 1 to true which means it is being used/opened
      elif inter_1 == "door_1":
        door1 = True
        game_loop1 = False
    elif action == "2":
      print(inventory, inventory2, "money:", money)
      input("> ")
    else:
      print("Invalid input")
      time.sleep(1)
    os.system("clear")
    
#checking if door 1 or 4 has been opened if so then make game loop 2 true
  if door1 or door4:
    game_loop2 = True
  #setting map to 4x4
    map = level.generate(4, 4)
    #setting coords for if you came through door 4 or 1
    if door4:
      coords = [3, 2]
    else:
      coords = [1, 2]
    door1 = False
    door4 = False
    map[coords[0]][coords[1]] = "@"
    map[0][2] = "#"
    map[2][3] = "+"
    #checking if player has collected item 1
    if collected_item_1 == False:
      map[2][0] = "*"
    map[3][3] = "#"

  while game_loop2:
    if game_over:
      game_loop1 = False
      game_loop2 = False
      game_loop3 = False
      game_loop4 = False
      door1 = False
      door2 = False
      door3 = False
      door4 = False
      door5 = False
      door6 = False
      door7 = False
      scroll("GAME OVER...\n", 0.3)
      input("> ")
      continue
    move = ""
    for o in range(0, level.height):
      print(map[o])
    print("'-' = background, '@' = player, '*' = item, '#' = door, '+' = enemy")
    try:
      time.sleep(0.1)
      action = input("Use wasd to move \nenter command:\n 1 = interact \n 2 = check inventory \n 3 = check health \n 4 = use item \n> ")
      time.sleep(0.1)
    except:
      print("Invalid syntax")
      time.sleep(1)
      os.system("clear")
    if action == "w" and coords[0] - 1 > -1 and map[coords[0] - 1][coords[1]] == "-":
      map[coords[0]][coords[1]] = "-"
      coords[0] -= 1
      map[coords[0]][coords[1]] = "@"
    elif action == "s" and coords[0] + 1 < 4 and map[coords[0] + 1][coords[1]] == "-":
      map[coords[0]][coords[1]] = "-"
      coords[0] += 1
      map[coords[0]][coords[1]] = "@"
    elif action == "d" and coords[1] + 1 < 4 and map[coords[0]][coords[1] + 1] == "-":
      map[coords[0]][coords[1]] = "-"
      coords[1] += 1
      map[coords[0]][coords[1]] = "@"
    elif action == "a" and coords[1] - 1 > -1 and map[coords[0]][coords[1] - 1] == "-":
      map[coords[0]][coords[1]] = "-"
      coords[1] -= 1
      map[coords[0]][coords[1]] = "@"
    elif action == "1":
      inter_1 = inter(map, coords, 2, inventory, inventory2)
      if inter_1 == "add_item_1":
        inventory["SHARP QUARTZ CRYSTAL"] = 20
        map[2][0] = "-"
        collected_item_1 = True
        os.system("clear")
      elif inter_1 == "door_2":
        door2 = True
        game_loop2 = False
      elif inter_1 == "door_3":
        door3 = True
        game_loop2 = False
        game_loop3 = True
      elif inter_1 == "enemy_1":
        tuple_output1 = battle(id, inventory, Health, inventory2)
        (Health1, inventory1, items, bool1, Game_over) = tuple_output1
        Health = Health1
        inventory = inventory1
        inventory2 = items
        game_over = Game_over
        if bool1:
          map[2][3] = "-"
    elif action == "2":
      print(inventory, inventory2, "money:", money)
      input("> ")
      if bool1 == True:
        map[2][3] = "-"
    elif action == "3":
      print("Health:", Health)
      input("> ")
    elif action == "4":
      print("Which item do you want to use out of your inventory:", inventory2)
      use = input("> ")
      if use.upper() == "RED HEALTH POTION":
        print("Health restored by 20 points.")
        Health += 20
        input("> ")
        used = True
      else:
        used = False
        print("You can't use", use, "at this point.")
        input("> ")
      if use.upper() in inventory2 and used:
        use = use.upper()
        inventory2.remove(use)
    else:
      print("Invalid input")
      time.sleep(1)
    os.system("clear")

  if door3 or door6:
    map = level.generate(5, 5)
    map = level.add_door(0, 0, map)
    map = level.add_lever(0, 1, map, False)
    map = level.add_lever(0, 2, map, False)
    map = level.add_lever(0, 3, map, False)
    map = level.add_lever(0, 4, map, False)
    map = level.add_wall(2, 0, map)
    map = level.add_wall(2, 1, map)
    map = level.add_wall(2, 2, map)
    map = level.add_wall(2, 3, map)
    map = level.add_wall(2, 4, map)
    map = level.add_player(1, 0, map)
    map = level.add_door(4, 4, map)
    if not(collected_item_2):
      map = level.add_item(4, 1, map)
    map = level.add_shop(4, 0, map)
    if door3 and not(door3_entered):
      lever1A = False
      lever1B = False
      lever1C = False
      lever1D = False
      map = level.add_lever(0, 1, map, False)
      map = level.add_lever(0, 2, map, False)
      map = level.add_lever(0, 3, map, False)
      map = level.add_lever(0, 4, map, False)
      coords = [0, 1]
      door3_entered = True
    elif door3_entered:
      map = level.add_lever(0, 1, map, lever1A)
      map = level.add_lever(0, 2, map, lever1B)
      map = level.add_lever(0, 3, map, lever1C)
      map = level.add_lever(0, 4, map, lever1D)
      coords = [0, 1]
    else:
      map = level.add_lever(0, 1, map, lever1A)
      map = level.add_lever(0, 2, map, lever1B)
      map = level.add_lever(0, 3, map, lever1C)
      map = level.add_lever(0, 4, map, lever1D)
      coords = [3, 4]
    door3 = False
    door5 = False

  while game_loop3:
    if not(lever1A) and lever1B and lever1C and not(lever1D) and not(map[2][2] == "@"):
      map = level.add_dash(2, 2, map)
    else:
      if map[2][2] == "@":
        map = level.add_player(2, 2, map)
      else:
        map = level.add_wall(2, 2, map)
      if map[2][2] == "@":
        map = level.add_player(2, 2, map)
    for o in range(0, level.height):
      print(map[o])
    print("'-' = background, '%' = wall, 'X' = off-lever, '1' = on-lever, 'S' = shop, '*' = item, '#' = door")
    try:
      action = input("Use wasd to move \nenter command:\n 1 = interact \n 2 = check inventory \n 3 = check health \n 4 = use item \n> ")
    except:
      print("Invalid syntax")
      time.sleep(1)
      os.system("clear")
    if action == "w" and coords[0] - 1 > -1 and map[coords[0] - 1][coords[1]] == "-":
      map[coords[0]][coords[1]] = "-"
      coords[0] -= 1
      map[coords[0]][coords[1]] = "@"
    elif action == "s" and coords[0] + 1 < 5 and map[coords[0] + 1][coords[1]] == "-":
      map[coords[0]][coords[1]] = "-"
      coords[0] += 1
      map[coords[0]][coords[1]] = "@"
    elif action == "d" and coords[1] + 1 < 5 and map[coords[0]][coords[1] + 1] == "-":
      map[coords[0]][coords[1]] = "-"
      coords[1] += 1
      map[coords[0]][coords[1]] = "@"
    elif action == "a" and coords[1] - 1 > -1 and map[coords[0]][coords[1] - 1] == "-":
        map[coords[0]][coords[1]] = "-"
        coords[1] -= 1
        map[coords[0]][coords[1]] = "@"
    elif action == "1":
      inter_1 = inter(map, coords, 3, inventory, inventory2)
      if inter_1 == "door_4":
        door4 = True
        game_loop2 == True
        game_loop3 = False
      elif inter_1 == "lever_1":
        lever1A = not(lever1A)
      elif inter_1 == "lever_2":
        lever1B = not(lever1B)
      elif inter_1 == "lever_3":
        lever1C = not(lever1C)
      elif inter_1 == "lever_4":
        lever1D = not(lever1D)
      elif inter_1 == "shop_1":
        shop1_active = True
        while shop1_active:
          buy_sell = input("Buy or sell: \n 1 = buy \n 2 = sell \n> ")
          if buy_sell == "1":
            shop1.buy(inventory, inventory2, money)
            inventory = shop1.inventory
            inventory2 = shop1.inventory2
            money = shop1.money
          elif buy_sell == "2":
            shop1.sell(inventory, inventory2, money)
            inventory = shop1.inventory
            inventory2 = shop1.inventory2
            money = shop1.money
          if input("Exit shop? (y/n)\n> ") == "y":
            shop1_active = False
          else:
            pass
      elif inter_1 == "item_2":
        inventory2.append("SHINY STONE")
        print("You have found a SHINY STONE!")
        map = level.add_dash(4, 1, map)
        collected_item_2 = True
      elif inter_1 == "door_5":
        if not(door5_unlocked):
          print("The door is locked...")
          input("> ")
          if "KEY1" in inventory2:
            print("Use KEY1? (y/n)")
            if input("> ").lower() == "y":
              print("Door unlocked!")
              inventory2.remove("KEY1")
              door5_unlocked = True
              input("> ")
              door()
              door5 = True
              game_loop4 = True
              game_loop3 = False
      map = level.add_lever(0, 1, map, lever1A)
      map = level.add_lever(0, 2, map, lever1B)
      map = level.add_lever(0, 3, map, lever1C)
      map = level.add_lever(0, 4, map, lever1D)
      os.system("clear")
    elif action == "2":
      print(inventory, inventory2, "money:", money)
      input("> ")
    elif action == "3":
      print("Health: ", Health)
      input("> ")
    elif action == "4":
      print("Which item do you want to use out of your inventory:", inventory2)
      use = input("> ")
      if use.upper() == "RED HEALTH POTION":
        print("Health restored by 20 points.")
        Health += 20
        input("> ")
      else:
        print("You can't use", use, "at this point.")
        input("> ")
      if use.upper() in inventory2:
        use = use.upper()
        inventory2.remove(use)
    os.system("clear")

  if door5 or door7:
    map = level.generate(6, 6)
    map = level.add_player(0, 1, map)
    map = level.add_door(0, 0, map)
    map = level.add_door(5, 5, map)
    map = level.add_wall(1, 0, map)
    map = level.add_wall(1, 1, map)
    map = level.add_wall(1, 2, map)
    map = level.add_wall(1, 3, map)
    map = level.add_wall(1, 4, map)
    map = level.add_wall(1, 5, map)
    map = level.add_enemy(0, 4, map)
    map = level.add_lever(0, 5, map, False)
    map = level.add_wall(2, 1, map)
    map = level.add_item(2, 0, map)
    map = level.add_enemy(3, 0, map)
  while game_loop4:
    for o in range(0, level.height):
      print(map[o])
    input("> ")
    
