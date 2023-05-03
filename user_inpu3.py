from _curses import echo

calc_to_unit = 24
name_of_unit = "hours"


def days_of_units(num_of_days):
    condition_check = num_of_days > 0
    print(type(condition_check))

    if num_of_days > 0:
        return (f"{num_of_days} days are {num_of_days * calc_to_unit}")
    elif num_of_days == 0:
        return "you entered zero number"
    else:
        return "you enter negtive value"


user_input = input("Hey this is input exemple, pls put number\n")
user_input_var = int(user_input)
calc_units = days_of_units(user_input_var)
print(calc_units)
#
print(isinstance(calc_units, bool))
