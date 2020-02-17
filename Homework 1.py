# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 18:27:13 2020

@author: samya
"""

#Data collection
first_name = str(input("Input Student's First Name: "))
last_name = str(input("Input Student's Last Name: "))
math_grade = float(input("Input Student's Math Grade: "))
eng_grade = float(input("Input Student's English Grade: "))

#Average grade computation
avg_grade = (math_grade + eng_grade)/2

#Output
print ("The student's name is " + first_name, last_name + ". Their Math grade is " + str(math_grade) + ", and their English grade is " + str(eng_grade) + ". This results in an average of " + str(avg_grade) + ".")