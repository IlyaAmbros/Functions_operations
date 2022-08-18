## Students Database
#   * data structers
#   * functional programming
#   * CRUD operations
#   * interactivity
#   * libs ( random , faker )
#   * usimg "pip"
import random
import os
from faker import Faker
fake = Faker()

stud_names = []     # str
stud_grades = []    # float
stud_years = []     # int

def genStudents( amount = 10 ) :
    for i in range ( amount ) :
        stud_names.append ( fake.name() )
        stud_years.append ( random.randint( 1,5 ) )
        stud_grades.append ( round ( random.uniform( 5.0 , 10.0 ) , 2 ) ) # HW1 : round values dd.xx

def printStudents() :
    for i in range ( len (stud_names) ) :
        print ( "-" * 48 )
        print ( f"| {stud_names[i]:30} | {stud_years[i]:<4} | {stud_grades[i]:<4} |")
    print ( "-" * 48 )

def addStudent() :
    s_name = input ( "Enter new student name : " )
    s_year = int ( input ( "Enter new student year : " ) )
    s_grade = float ( input ( "Enter new student grade : " ) )

    stud_names.append( s_name )
    stud_years.append( s_year )
    stud_grades.append( s_grade )

def editStudent():
    s_name = input ( "Enter the name of the student to edit : ")
    s_index = -1
    for i in range ( len ( stud_names ) ) :
        if stud_names[i] == s_name :
            s_index = i
            break
    if s_index >= 0 :
        stud_years.pop(s_index)
        new_stud_years = int ( input ( "Enter the student's new year : ") )
        stud_years.insert( s_index , new_stud_years )
        stud_grades.pop(s_index)
        new_stud_grades = float ( input ( "Enter the student's new grade : ") )
        stud_grades.insert( s_index , new_stud_grades )

def removeStudent():
    s_name = input ( "Enter the name of the student to delete : ")
    s_index = -1
    for i in range ( len ( stud_names ) ) :
        if stud_names[i] == s_name :
            s_index = i
            break
    if s_index >= 0 :
        stud_names.pop(s_index)
        stud_years.pop(s_index)
        stud_grades.pop(s_index)

def printMenu():
    print ( "### STUDENTS DATABASE ###" )
    print ( "1. Show students list" )
    print ( "2. Add a student" )
    print ( "3. Edit a student" )
    print ( "4. Remove a student" )
    print ( "0. Exit" )
    print ( "##########################" )
    option = int ( input ( ">>> " ) )
    return option

# HW3 : a. find the best student ( find maximum value ) 
def the_best_student():
  maximal = 0
  for i in range ( len ( stud_names ) ) :
    if stud_grades[i] > maximal :
      maximal = stud_grades[i]
      the_best_student = stud_names[i]
  print ( "The best student in the course is :" , the_best_student , " with a grade " , maximal , " !")

# HW3 : b. show all students within a grade range ( 7 - 9 ) 
def find_good_students():
  good_students = []
  for i in range ( len ( stud_names ) ) :
      if 7.00 <= stud_grades[i] <= 9.00 :
        good_students.append(stud_names[i])
  print ( "The good students in the course are :" , end="")
  for j in range ( len ( good_students ) ) :
    print (f" {j + 1} ) {good_students[j]} " , end="")
  print()
########################################################
genStudents(10)
while True :
    os.system("cls")
    option = printMenu()

    if option == 1 :
        printStudents()
        the_best_student()
        find_good_students()
        input ( "hit enter to continue" )
    elif option == 2 :
        addStudent()
    elif option == 3 :
        # HW2 : finish the edit code
        #       user -> sttudents name
        #       find by name
        #       new grade / year
        editStudent()
    elif option == 4 :
        removeStudent()
    elif option == 0 :
        break