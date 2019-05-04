import random
from forex_python.converter import CurrencyRates
def get_money_interval():

    user_difficulty = input("please put difficulty number:")
    user_difficulty_int = int(user_difficulty)
    c = CurrencyRates()
    currenecy = c.get_rate('USD', 'ILS')
    print(currenecy)
    print("The machine will genrreate randon nmber, you will have to guess the value to ILS ")
    Random_number = int(random.randint(1,101))

    print(Random_number)

    total_amount = Random_number * currenecy


    user_guess1 = int(input("user please a number what will be the Cuerrency "  ))
    user_guess2 = int(user_guess1 * currenecy)
    var1 = -1
    interval = int(user_difficulty_int - user_guess2)
    interval2 = int(user_difficulty_int + user_guess2)
    machine_sum = currenecy * Random_number
    user_guess = int(user_guess2 + interval + interval2)

    user_sum = int(currenecy * user_guess)

    try:
        if user_sum == machine_sum:
            print("yes you are correct")
        elif user_sum !=  machine_sum:
            print("NOPE - wrong guess Please play again")
    except:
            print("Worng calc")

 #   exit()
    for x in range(2):
        return get_money_interval()
        break
get_money_interval()








