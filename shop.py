import os
selling_items = {"WOODEN SWORD": 25, "RED HEALTH POTION": 15, "INK SAC": 10, "STONE SWORD": 25, "SHINY STONE": 40, "SHARP QUARTZ CRYSTAL": 60}

class Shop():
  def __init__(self, weapons, items):
    self.items = items
    self.weapons = weapons
    self.is_buying = False
    self.is_selling = False
  def buy(self, inventory, inventory2, money):
    os.system("clear")
    self. money = money
    self.inventory = inventory
    self.inventory2 = inventory2
    self.is_buying = True
    while self.is_buying:
      print("Choose item to Buy:", self.items, self.weapons, "money: ", self.money, "$")
      choice = input("> ")
      choice = choice.upper()
      if choice in self.items and self.money >= (self.items[choice]) or choice in self.weapons and self.money >= (self.weapons[choice]):
        print("you have bought", choice)
        if choice in self.items:
          self.money = self.money - (self.items[choice])
          self.inventory2.append(choice)
        else:
          self.money = self.money - (self.weapons[choice])
          a = (self.weapons[choice])
          self.inventory[choice] = a
        print("You have", self.money, "$ left")
        print("continue buying? (y/n)")
        if input("> ") == "y":
          self.is_buying = True
        else:
          self.is_buying = False
        os.system("clear")
      else:
        print(choice, "cannot be bought")
        print("continue buying? (y/n)")
        if input("> ") == "y":
          self.is_buying = True
        else:
          self.is_buying = False
        os.system("clear")
  def sell(self, inventory, inventory2, money):
    os.system("clear")
    self.money = money
    self.inventory = inventory
    self.inventory2 = inventory2
    self.is_selling = True
    while self.is_selling:
      print("Choose item to sell:", self.inventory, self.inventory2)
      choice = input("> ")
      choice = choice.upper()
      if choice in self.inventory or choice in self.inventory2:
        print("You have sold:", choice, "for", selling_items[choice], "$")
        if choice in self.inventory:
          self.inventory.pop(choice)
        else:
          self.inventory2.remove(choice)
        self.money = self.money + (selling_items[choice])
        input("> ")
        print("continue selling? (y/n)")
        if input("> ") == "y":
          self.is_selling = True
        else:
          self.is_selling = False
        os.system("clear")
      else:
        print(choice, "cannot be sold")
        print("continue selling? (y/n)")
        if input("> ") == "y":
          self.is_selling = True
        else:
          self.is_selling = False
        os.system("clear")
