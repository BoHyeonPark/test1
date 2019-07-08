#!/usr/bin/python3
try:
    num = int(input("Enter: "))
    print(10/num)
except ZeroDivisionError:
    print("No zero, only enter number")
except ValueError:
    print("Enter number value!")
