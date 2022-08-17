#   LIFT UP
# -----------------
#   7 |[  ]|
#   6 |    |
#   5 |    |
#   4 |    |    H
#   3 |    |
#   2 |    |
#   1 |    |
# -----------------
# 1. call
# 2. dest
# 3. enter 
# 4. exite

# * input
# * list 
# * function
# * file

#######################################
from os import system
from time import sleep

floor_max = 7
floor_min = 1

lift_floor = 7
human_floor = 1

human_in_lift = False 

def printFloors() :
    print ( "-" * 20 )
    for floor in range ( floor_max , floor_min - 1 , -1 ) :
        if human_in_lift and floor == lift_floor :
            print ( f"{floor}|[ H ]|")
        elif floor == lift_floor and floor == human_floor and not human_in_lift :            
            print ( f"{floor}|[   ]|   H")
        elif floor == human_floor and not human_in_lift :            
            print ( f"{floor}|     |   H")
        elif floor == lift_floor :            
            print ( f"{floor}|[   ]|")
        else :
            print ( f"{floor}|     |")
    print ( "-" * 20 )

def printMenu() :
    print ( "1. call" )
    print ( "2. dest" )
    print ( "3. enter" )
    print ( "4. exite" )
    option = int ( input ( ">>> " ) )
    return option

def call() :
    # HW1 : if / else --> DOWN / UP
    global lift_floor
    while lift_floor != human_floor :
        sleep(0.5)
        if lift_floor > human_floor :
            lift_floor -= 1
        elif lift_floor < human_floor :
            lift_floor += 1
        system ( "cls" )
        printFloors() 

def destination() :
    # HW1 : if / else --> DOWN / UP
    global lift_floor
    if human_in_lift == True :
        where_to = int ( input ( "Wich floor : " ) )
        while lift_floor != where_to :
            sleep(0.5)
            if lift_floor > where_to :
                lift_floor -= 1
            elif lift_floor < where_to :
                lift_floor += 1
            system ( "cls" )
            printFloors() 
    else :
        print ( "WARNING !!! There is no person in the elevator .")
        sleep(0.5)

def enter() :
    global human_in_lift
    if lift_floor == human_floor :
        human_in_lift = True
    else :
        print ( "WARNING yoy can fall !!!")
    
def exit() :
    global human_in_lift
    global human_floor
    if human_in_lift :
        human_in_lift = False
        human_floor = lift_floor
    else :
        print ( "WARNING human not in lift !!!")
#######################################
while True :
    system ( "cls" )
    printFloors() 
    option = printMenu()
    if option == 1:
        call()
    elif option == 2:
        destination()
    elif option == 3:
        enter()
    elif option == 4:
        exit()