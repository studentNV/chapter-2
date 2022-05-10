#!/usr/bin/env python
def task6_returns_dict(str_user):
    dict_return = {}
    for i in str_user:
        buf_symbol_count = 0
        for j in str_user:

            if i == j:
                buf_symbol_count += 1
        dict_return[i] = buf_symbol_count
    return dict_return


print(task6_returns_dict("Hello World"))
print(task6_returns_dict("asdasdasd"))
