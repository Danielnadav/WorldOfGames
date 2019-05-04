def generate_number():

    from random import randint
    for _ in range(10):
        value = randint(0, 10)
        print(value)


generate_number()

def test_file():
    text_file = int(generate_number())
    text_file = open("/var/tmp/game.txt", "w+")
    text_file.write = int()
    text_file.close
difficulty_game = input("please choose a difficulty_game to play between: 1-5")
   game = int(difficulty_game)


#generate_number.writelines(difficulty_game=input())
# # def my_file():
# #     my_file = open("/var/tmp/secret_number.txt", "a+")
# #
# #     my_file.write(generate_number())
# #
#
# from random import seed
# from random import randint
# # seed random number generator
# seed(1)
# # generate some integers
# for _ in range(10):
# 	value = randint(0, 10)
# 	print(value)