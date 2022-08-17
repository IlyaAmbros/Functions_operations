# * generate random 2d array
# * print 2d array
# * calculate average value 2d array

# SRP 

from random import randint
from math import ceil

###################################################
# HW1 : pass value range as arguments
def random2darray( rows , cols , value_1 , value_2 ) :
    matrix = []
    for ri in range ( rows ) :
        row = []
        for ci in range ( cols ) :         
            row.append ( randint ( value_1 , value_2 ) )
        matrix.append ( row )
    return matrix
###################################################

###################################################
# HW2 : add a header 
#       size: 5 x 3
def print2darray( matrix ) :
    print ()
    print ( f"SIZE : {rows} X {cols}" )
    for ri in range ( rows ) :
        for ci in range ( cols ) :         
            print ( f"|{matrix[ri][ci] : 5}|" , end = " ")      
        print ()
###################################################

###################################################
# HW3 : create another function
#       that finds min , max values
#       return grouped
def min_max2darray( matrix ) :
    min_max = [
            [],
            []
        ]
    maximal = matrix[0][-1]
    minimal = matrix[0][-1]
    for ri in range ( len ( matrix ) ) :
        for ci in range ( len ( matrix ) ) :
            # Find MAXIMAL
            if matrix[ci][ri] > maximal :
                maximal = matrix[ci][ri]
                min_max[0].append(maximal)
            # Find MINIMAL
            if matrix[ci][ri] < minimal :
                minimal = matrix[ci][ri]
                min_max[1].append(minimal)
    return min_max
###################################################

###################################################
def printmin_max2darray( min_max ) :
    print ()       
    print ( f"Maximum value in the table - {min_max[0][len(min_max[0]) - 1]:5}\n")
    print ( f"Minimum value in the table - {min_max[1][len(min_max[1]) - 1]:5}\n")
###################################################

###################################################
def average2darray( matrix ) :
    s = 0
    h = len ( matrix )
    w =  len ( matrix[0] )
    for ri in range ( h ) :
        for ci in range ( w ) :         
            s += matrix[ri][ci]
    average = s / ( h * w )
    return average
###################################################

print ()
print ( "Enter the size of the table :\n" )
rows = int ( input ( "1) rows - " ) )
print ()
cols = int ( input ( "2) cols - " ) )
print ()
print ( "Enter the range of values in you want to work with :\n" )
value_1 = int ( input ( "1) value_1 - " ) )
print ()
value_2 = int ( input ( "2) value_2 - " ) )
print ()

if value_1 < value_2 :
    data = random2darray ( rows , cols , value_1 , value_2 )
    print2darray( data )
    a = average2darray( data )
    min_max = min_max2darray( data )
    printmin_max2darray( min_max )
    print ( f"Average = {a:5.3}\n" )
else : 
    print ( "This range cannot be created !!!" )