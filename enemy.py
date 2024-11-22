class Enemy:
  def __init__(self, name, health, damage):
    self.name = name
    self.health = health
    self.damage = damage
    self.is_defeated = False
  def attack(self):
    print(self.name, "attacked dealing", self.damage, "damage!")
    input("> ")
    return self.damage
  def is_attacked(self, loss, weapon):
    self.weapon = weapon
    print("you attacked", self.name, "with", self.weapon)
    self.loss = loss
    self.health = self.health - self.loss
    input("> ")
    if self.health <= 0:
      self.is_defeated = True
      print("you defeated " + self.name + "!")
      input("> ")
