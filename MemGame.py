
import random
import time

def generate_sequence():
    try:
        print("Welcome to our Memory Game, Please try remmber the bumbers ;")
        mc_list=[]
        mc_list.append(random.sample(range(1, 101), 5))
        print(str(mc_list))
        time.sleep(4)
        print("\n" * 100)
    except:
        print("Error in random num")

    try:
        user_list=[]
        user_list.append(input("please put 5 numbers"))
        print("user list num is:" + str(user_list))
    except:
        print("error in list")

    try:
        game = str(mc_list)
        game1 = str(user_list)
        if game1 == game:
            print("Well done good memory")
        else:
             print("no luck lets play again")

    except:
        print("game code issue")

    # try:
    #     user_list=[]
    #     return generate_sequence()
    #
    #     if game == game1:
    # print("Ture")
    # else:
    #     print("false")
    # except:
    #     print("error is if game ==game")

generate_sequence()


#
# F
def call_play():
    return generate_sequence()

call_play()

