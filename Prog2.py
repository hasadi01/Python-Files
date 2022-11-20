# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 18:45:22 2021

@author: Grading ID: R7161
"""

# Pogram 2
# CIS 443-01
# Grading ID:R7161
# Due Date: 10/21/21
# This program creates two functions: one that will accept a number
# of students and a number of tests for each student, 
# stores these values in a 2-d list, and returns the list
# The second function summarizes the grades and makes frequencies for them

import matplotlib.pyplot as plt 
import numpy as np 
import seaborn as sns


def input_test_scores():
    student_scores = {} #2-d list to store student test scores
    students = int(input("Enter number of students: ")) # first get input for number of students
    number_of_tests = int(input("Enter the number of tests per student: ")) # get input for # of tests per student
    
    student_number = 0 
    for student in range(students): # for every student, increase the student number by 1
        student_number += 1 
        score_number = 0 
        scores = [] # score for each student stored in this list
        print(f'Enter test scores for student {student_number}: ')
        for test in range(number_of_tests): # for every test increase the test score number by 1
            score_number += 1 
            test_score = int(input(f"Enter score {score_number}: "))
            scores.append(test_score) # append the scores list with the test scores
        student_scores[student_number] = scores #student number is made key; scores are the values
    return student_scores

def summarize_test_scores(student_scores): 
    print("\nGrade Summary")
    print('Student  Mean  Grade')
    print('------- ------ ------')
    
    grades = {"A":0, "B":0, "C":0, "D":0, "F":0} # create 2-d list to store grades and initialize values to 0
    for student_number, scores in student_scores.items(): # for each score, calculate mean and assign letter 
        mean_score = sum(scores) / len(scores) # grade to mean depending on if score is >= to certain value
        if mean_score >= 90:
            grade = "A"
        elif mean_score >= 80:
            grade = "B"
        elif mean_score >= 70:
            grade = "C"
        elif mean_score >= 60:
            grade = "D"
        else:
            grade = "F"
        grades[grade] += 1 #incriment value (frequency) by 1 for each key in the 2-d list
        print(f'{student_number} {mean_score:>10} {grade:>4}')
    print("\nGrades and Frequencies")
    for grade, frequency in grades.items(): # for each key-value pair, print the grade and frequency
        print(f"{grade}: {frequency}")
  
       # next lines of code to create bar chart
    title = "Grade Frequencies"
    sns.set_style('whitegrid')
    axes = sns.barplot(x=grades.keys(), y=grades.values(), palette='bright') 
    axes.set_title(title)
    axes.set(xlabel="Grade", ylabel="Frequency")
   
    
   
student_scores = input_test_scores() # calling the function to get student scores
summarize_test_scores(student_scores) # passing the student scores to get summary


