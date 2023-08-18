#!/usr/bin/env python3

def happy_new_year():
    counter = 10
    while counter >= 1:
        print(counter)
        counter -= 1
        
    print("Happy New Year!")
happy_new_year()

def square_integers(int_list):
    return [y**2 for y in int_list]
#    print(square_integers([1, 2, 3, 4]))



def fizzbuzz_printer():
    for x in range (1, 101):
        if x % 3 == 0 and x % 5 == 0:
            print("FizzBuzz")
        elif x % 3 == 0:
            print("Fizz")
        elif x % 5 == 0:
            print("Buzz")
        else:
            print(x)
fizzbuzz_printer() 
