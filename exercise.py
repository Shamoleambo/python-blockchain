name = input("What is your name?")
age = int(input("How old are you?"))


def print_name_and_age_one_string(name='', age=0):
    print(name + ' ' + str(age))


def print_any_data_one_string(firstValue='', secondValue=''):
    print(str(firstValue) + ' ' + str(secondValue))


def calculate_dacades(time=0):
    return time//10


print_name_and_age_one_string(name, age)
print_any_data_one_string(True, 3.3)
print_any_data_one_string(calculate_dacades(age))
