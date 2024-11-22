import time
import os

def old_man():
  os.system("clear")
  print("old man: Hello there young one!")
  input("> ")
  print("old man: If you are to carry on you'll need a weapon to defend yourself.")
  input("> ")
  print("old man: here, have this")
  input("> ")
  print("You obtained: WOODEN SWORD!")
  input("> ")
  print("old man: it's not the best of weapons but it'll do you good. Good luck!")
  input("> ")

def door():
  print("You opened the door and went through...")
  input("> ")
  os.system("clear")

def unfinished():
  print("This level is under construction.")
  print("Coming soon...")
  input("> ")

def scroll(string, delay):
  for letter in string:
    print(letter, end="", flush=True)
    time.sleep(delay)
