#!/usr/bin/env python
def task1_self_study():
    print("Pleas enter sequence of comma-separated numbers")
    user_numbers = input()
    print("Input list")
    print(list(user_numbers.split(",")))
    print("Input tuple")
    print(tuple(user_numbers.split(",")))


task1_self_study()
