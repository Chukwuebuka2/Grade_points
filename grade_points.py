# A program to calculate the grade point of a someones result per semester

# importing numpy and pandas as the two module we are going to use
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

print('Please enter the following accordingly.\
You are only to register a minimum of nine courses and a maximum of\
ten')

# Create a list of courses, units and grades to store the user input
courses = []
unit = []
grades = []
# Putting the gps in a list
gps = []

# Read Course code,unit and grade obtained from a user

# For the first course
print('First Course')
course1 = str(input('Course Code: '))
course1 = course1.upper()
courses.append(course1)
unit1 = int(input('Enter Course unit: '))
unit.append(unit1)
grade1 = str(input('Enter grade: '))
grade1 = grade1.upper()
grades.append(grade1)

# For the second course
print('\nSecond Course')
course2 = str(input('Course Code: '))
course2 = course2.upper()
courses.append(course2)
unit2 = int(input('Enter Course unit: '))
unit.append(unit2)
grade2 = str(input('Enter grade: '))
grade2 = grade2.upper()
grades.append(grade2)

# For the third course
print('\nThird Course')
course3 = str(input('Course Code: '))
course3 = course3.upper()
courses.append(course3)
unit3 = int(input('Enter Course unit: '))
unit.append(unit3)
grade3 = str(input('Enter grade: '))
grade3 = grade3.upper()
grades.append(grade3)

# For the fourth course
print('\nFourth Course')
course4 = str(input('Course Code: '))
course4 = course4.upper()
courses.append(course4)
unit4 = int(input('Enter Course unit: '))
unit.append(unit4)
grade4 = str(input('Enter grade: '))
grade4 = grade4.upper()
grades.append(grade4)

# For the fifth course
print('\nFifth Course')
course5 = str(input('Course Code: '))
course5 = course5.upper()
courses.append(course5)
unit5 = int(input('Enter Course unit: '))
unit.append(unit5)
grade5 = str(input('Enter grade: '))
grade5 = grade5.upper()
grades.append(grade5)

# For the sixth course
print('\nSixth Course')
course6 = str(input('Course Code: '))
course6 = course6.upper()
courses.append(course6)
unit6 = int(input('Enter Course unit: '))
unit.append(unit6)
grade6 = str(input('Enter grade: '))
grade6 = grade6.upper()
grades.append(grade6)

# For the seventh course
print('\nSeventh Course')
course7 = str(input('Course Code: '))
course7 = course7.upper()
courses.append(course7)
unit7 = int(input('Enter Course unit: '))
unit.append(unit7)
grade7 = str(input('Enter grade: '))
grade7 = grade7.upper()
grades.append(grade7)

# For the eight course
print('\nEight Course')
course8 = str(input('Course Code: '))
course8 = course8.upper()
courses.append(course8)
unit8 = int(input('Enter Course unit: '))
unit.append(unit8)
grade8 = str(input('Enter grade: '))
grade8 = grade8.upper()
grades.append(grade8)

# For the ninth course
print('\nNinth Course')
course9 = str(input('Course Code: '))
course9 = course9.upper()
courses.append(course9)
unit9 = int(input('Enter Course unit: '))
unit.append(unit9)
grade9 = str(input('Enter grade: '))
grade9 = grade9.upper()
grades.append(grade9)

# For the tenth course
print('\nTenth Course')
course10 = str(input('Course Code: '))
course10 = course10.upper()
courses.append(course10)
unit10 = int(input('Enter Course unit: '))
unit.append(unit10)
grade10 = str(input('Enter grade: '))
grade10 = grade10.upper()
grades.append(grade10)

#Computations

# Calculating TGP
for grade in grades:
    gp = ''
    if grade == 'A':
        gp = 5
    elif grade == 'B':
        gp = 4
    elif grade == 'C':
        gp = 3
    elif grade == 'D':
        gp = 2
    elif grade == 'E':
        gp = 1
    elif grade == 'F':
        gp  = 0
    gps.append(gp)
    
# Calculating the TNU
TNU = sum(unit)

# Let's turn the unit list and gps list into array
np_unit = np.array(unit)
np_gps = np.array(gps)

# To calculate the TGP
TGP = np.multiply(np_unit, np_gps)

# Hence the GP for that semester is
GP = np.divide(sum(TGP), TNU)

# Now to display the result 

# First we put all in a dictionary
dict_result = {'COURSES': courses, 'UNITS': unit, 'GRADES': grades}

# Then we put it in DataFrame to display in tabular manner
result = pd.DataFrame(dict_result)
print(result)
print(GP)

