def scores_file_name():
        import os 
        game = input ("please choose a difficulty_game to play between: 1-5")
        input_game = int(game)
        input_game.my_file = open("/var/tmp/socres.txt", "w+")
        input_game.my_file.write(game)
        if input_game != int:
            print = "error please put numbers only"
            return game
        else:
            game = list
            print "\n" * 100
scores_file_name()

