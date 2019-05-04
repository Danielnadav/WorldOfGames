import random
def get_guess_from_user():

     get_guess_num = input("please choose Number : 1-100")
     get_guess_1 = get_guess_num
     GenerateNumber = int(random.randint(1, 100))
     get_num_res = GenerateNumber
     print(GenerateNumber)
     try:
        if get_guess_1 == get_num_res:
             print("wwwwwwww")
        elif get_guess_1 !=get_num_res:
             print("nooooo")
     except:
         print("calca problem please check")
get_guess_from_user()