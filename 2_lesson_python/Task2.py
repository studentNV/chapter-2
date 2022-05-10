#!/usr/bin/env python
def task2_print_all_even_numbers(numbers):
    for i in numbers:
        if type(i) != int:
            print("\t\tTask2.\nYou did something wrong!\nThe procedure accepts only numbers!\n"
                  "You directed ", numbers)
            return 1

    print("\t\tTask2.\nStart print list! You directed ", numbers)
    for var in numbers:
        if var != 254:
            if var % 2 == 0:
                print(var, end=' ')
        else:
            break

    print()
    return 0


print("-=Correct argument=-")
task2_print_all_even_numbers((1, 2, 3, 4, 5, 6, 10, 20, 254, 24, 74))
print("-=Incorrect argument=-")
task2_print_all_even_numbers((1, 2, 3, "asd"))
