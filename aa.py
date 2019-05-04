def difficulty_game():

   difficulty_game = input("please choose a difficulty_game to play between: 1-5")
   game = int(difficulty_game)
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

    difficulty_game = open("/var/tmp/games.txt", "w+")
    difficulty_game.write(int + "\n")
    difficulty_game.close
difficulty_game()



