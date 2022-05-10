#!/usr/bin/env python
from pprint import pprint as pp

context = "This script has the following PID: <ACTUAL_PID_HERE>. It was ran by <ACTUAL_USERNAME_HERE> to work happily " \
          "on <ACTUAL_OS_NAME>-<ACTUAL_OS_RELEASE>. "
print("\n-=First format=-\n")
pp(context)
print("\n-=Second format=-\n")
for i in context:
    if i == ".":
        print(".")
    else:
        print(i, end='')
