

calc_to_unit= 24
name_of_unit = "hours"


def days_of_units(num_of_days):
    return (f"{num_of_days} days are {num_of_days * calc_to_unit}")

user_input = input("Hey this is input exemple\n")
user_input_var = int(user_input)
# user_input = input("enter some number of days\n")
# # #user input return the value we enter beofoe
calc_units = days_of_units(user_input_var)
print(calc_units)