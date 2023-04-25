
calc_to_unit= 24
name_of_unit = "hours"
name_of_test = "tim"

def days_of_units(num_of_days, custom_message):
    print(f"{num_of_days} days are {num_of_days * calc_to_unit}")
    print(custom_message)
    # print(f"{num_of_days} {20 * to_second} {name_of_unit}")
    # print(f"34 days are {35 * to_second} minutes")
days_of_units(35, "awesome")
days_of_units(20, "woow")


def scope_of_days(num_of_age):
    my_var = "variable inside function"
    print(name_of_test)
    print(my_var)
scope_of_days(20)