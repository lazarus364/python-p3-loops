#!/usr/bin/env python3

def happy_new_year():
    # Code goes here!
    counter = 10
    while counter > 0:
        print(counter)
        counter -= 1 
    print("Happy New Year!")


    pass

def square_integers(int_list):
    # code goes here!
    squared_list = []
    for number in int_list:
        squared_list.append(number * number)
    return squared_list
numbers = [1, 2, 3, 4, 5]
squared_numbers = square_integers(numbers)    

def fizzbuzz():
    # code goes here!
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)            
    pass
