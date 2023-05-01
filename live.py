def welcome():
   welcome = input("name: ")
   print("Hello", welcome, "and Welcome to the World of Games (WoG), Here you can find many cool games to play.")
welcome()

def load_game():
   load_game = input("please choose a game to play: 1-3")
   val = int(load_game)
   if val == 1:
      print("Memory Game - a sequence of numbers will aasppear for 1 second and you have to guess it back")
   elif val == 2:
      print("Guess Game - guess a number and see if you chose like the computer")
   if val == int:
      print("Weather Roulette - Guess the current temperature currently in Jerusalem")
   elif val != enumerate:
       print("print write number only:")


load_game()

def difficulty_game():
   game = input("please choose a difficulty_game to play between: 1-5")
   difficulty_game = open("/var/tmp/game.txt", "a+")
   difficulty_game.write(game+"\n"+"lalala")
   difficulty_game.close()

   if game  == 1:
      print("difficulty_game_Level1")
   elif game == 2:
      print("difficulty_game_level2")
   if game == 3:
      print("difficulty_game_Level3")
   elif game == 4:
      print("difficulty_game_Level4")
   if game == 5:
      print("difficulty_gameLevel5")


# difficulty_game = open("/var/tmp/game.txt", "r+")
# difficulty_game.write(int + "\n")

difficulty_game()

# def my_file():
#         #import (difficulty_game())
#         my_file = open("/var/tmp/game.txt", "r+")
#         my_file.write("hey" + "\n")
#         my_file.write("hey" + load_game(difficulty_game()))
#         my_file.write(difficulty_game())
#         my_file.writelines(difficulty_game=input())
# my_file()


