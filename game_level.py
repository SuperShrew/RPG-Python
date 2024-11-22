class Level():
  def __init__(self, map):
    self.map = map
  def generate(self, width, height):
    self.height = height
    self.map = []
    for x in range(0, height):
      self.map.append(["-"]*width)
    return self.map
  def add_dash(self, x, y, map):
    map[y][x] = "-"
    return map
  def add_enemy(self, x, y, map):
    map[y][x] = "+"
    return map
  def add_item(self, x, y, map):
    map[y][x] = "*"
    return map
  def add_door(self, x, y, map):
    map[y][x] = "#"
    return map
  def add_lever(self, x, y, map, state):
    if state:
      map[y][x] = "1"
      return map
    elif state == False:
      map[y][x] = "X"
      return map
    else:
      print("Invalid Lever state in class: Level, file: game_level.py")
      input("> ")
      return False
  def add_wall(self, x, y, map):
    map[y][x] = "%"
    return map
  def add_player(self, x, y, map):
    map[y][x] = "@"
    return map
  def add_shop(self, x, y, map):
    map[y][x] = "S"
    return map
