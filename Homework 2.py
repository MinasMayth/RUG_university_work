# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 23:26:17 2020

@author: samya
"""

import json

def first_time_run():
    
    #First time run as to setup the basic version of the list. This creates a dictionary that contains all elements of the given lists,
    #and saves it to a json file.
    json_data = { 'names' : ['Nils', 'Mark', 'Marilyn', 'Mariam', 'Albert'],

    'homework' : [2, 10, 4, 6, 7],

    'exam' : [20, 55, 33, 60, 45],

    'project' : [12, 30, 21, 24, 22] 
                }

    with open("student_results.json","w") as f:
        json.dump(json_data,f)

    return ("done")
    
def read_file():
    
    
    #This is the funciton for reading the data file. It opens the created file with Json and then reads out the values individually.
    
    #Counter for making sure all corresponding scores are being shown together
    counter = 0
    
    #This opens the student_results json file and assigns local variables
    with open("student_results.json", "r") as f:
        results = json.load(f)
        names = results["names"]
        homework = results["homework"]
        exam = results["exam"]
        project = results["project"]
    
    #This part goes through each value in names once and prints the coressponding scores and totals.    
    for i in names:
        final_grade = homework[counter] + exam[counter] + project[counter]
        
        #Conditional variable to check if passed or not
        if final_grade >= 50:
            student_result = "Pass"
        else:
            student_result = "Fail"
        
        print (i , homework[counter] , exam[counter] , project[counter], final_grade, student_result)
        counter += 1
        
    
    return("done")

def write_file():
    
    #This function allows the user to edit the list and append new results
    
    #same as above, open the json and assign local variables
    with open("student_results.json", "r") as f:
        results = json.load(f)
        names = results["names"]
        homework = results["homework"]
        exam = results["exam"]
        project = results["project"]

    #Here the User is asked to append to the lists
    names.append(input ("Enter Name: "))
    homework.append(int(input ("Enter Homework Grade: ")))
    exam.append(int(input ("Enter Exam Grade: ")))
    project.append(int(input ("Enter Project Grade: ")))
    
    #Assignment of the lists to one dictionary for graceful storing
    
    json_data = {
            
            'names' : names,

    'homework' : homework,

    'exam' : exam,

    'project' : project        
            
            }

    #writes the new data to the file
    with open("student_results.json","w") as f:
        json.dump(json_data,f)
    
    return ("done")


if __name__ == "__main__":
    
    #Main loop. Some conditiions for text entry commands and a break command.
    while True:
        user_input = input ("first time, read or write? (exit to break)").lower()

        if user_input == "first time":
            print (first_time_run())
        elif user_input == "read":
            print (read_file())
        elif user_input == "write":
            print (write_file())
        elif user_input == "exit":
            break
        else:
            print ("Invalid input.")
