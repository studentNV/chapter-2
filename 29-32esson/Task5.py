#!/usr/bin/env python
def task5_returns_list(list_numbers):
    list_return = []
    for i in list_numbers:
        if type(i) != int:
            list_return.append(i)
    if list_return:
        print("You've passed some extra elements that I can't parse: ", list_return)
        return 1
    for i in (range(3)):
        if not list_numbers:
            break
        list_return.append(max(list_numbers))
        list_numbers.remove(max(list_numbers))
    return list_return


print("\nNormal list")
print(task5_returns_list([12, 456, 23, 1]))
print("\nList with strings")
task5_returns_list(["violetta", 456, "abc", 1])
print("\nShort list")
print(task5_returns_list([23, 1]))
print("\nEmpty list")
print(task5_returns_list([]))
