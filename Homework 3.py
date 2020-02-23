# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 12:59:33 2020

Homework 3!

@author: samya
"""

import random
import matplotlib.pyplot as plt
import numpy as np


def rand_list_gen():
    length = int(input("What length should the list be? "))
    numbers = []
    for x in range (0,length):
        numbers.append(round(random.random(),3))

    print(numbers)
    return(numbers)
    
def rand_list_calc(x):
    list_sum = 0
    for i in numbers:
        list_sum += i
    
    print ("The sum of all numbers in the list is %.3f." % list_sum )
    
    list_avg = list_sum/len(numbers)
    
    print ("The average of all numbers in the list is %.3f." % list_avg)
    

def circle_plotter():
    circle1 = plt.Circle((5, 5), 2, color='blue')
    ax = plt.gca()
    ax.cla()
    ax.set_xlim((0, 10))
    ax.set_ylim((0, 10))
    ax.add_artist(circle1)
    plt.savefig('plotcircles.png')
    plt.show()


def negative_replacer():
    list_of_integers = []
    for x in range (0,10):
        list_of_integers.append(round(random.randint(-10,10)))
    
    print(list_of_integers)
    
    positive_list = [i if i >= 0 else 0 for i in list_of_integers]
    
    print(positive_list)
    

def list_operations():
    a = []
    b = []
    
    for x in range (0,10):
        a.append(round(random.randint(0,10)))
    for x in range (0,10):
        b.append(round(random.randint(0,10)))
    
    
    print (a)
    print (b)
    
    decision = input(" '+' or '-'? ")
    
    if decision == "+":
        c = list(np.array(a) + np.array(b))
    elif decision == "-":
        c =list(np.array(a) - np.array(b))
    
    print(c)

if __name__ == "__main__":
    while True:
        print("Which program do you want to run?")
        print("1. Random list generator")
        print("2. Random list calculator (RUN 1 BEFORE RUNNING THIS)")
        print("3. Circle plotter")
        print("4. Negative integer replacer")
        print("5. List operations tester")
        print("Or type 'exit' to leave the program!")
        menu_decision = input().upper()
        
        if menu_decision == "1":
            numbers = rand_list_gen()
        
        elif menu_decision == "2":
            rand_list_calc(numbers)
            
        elif menu_decision == "3":
            circle_plotter()
            
        elif menu_decision == "4":
            negative_replacer()
            
        elif menu_decision == "5":
            list_operations()
            
        elif menu_decision == "EXIT":
            break
        else:
            print("Invalid input.")