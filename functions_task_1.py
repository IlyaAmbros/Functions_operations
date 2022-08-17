## Функции. Оптимизация кода с использованием функций

def drawLine( length , direction ) :
    for i in range ( length ) :
        if direction == 'h' :
            print ( "-" , end="" )
        elif direction == 'v' :
            print ( "|" )

drawLine( 5, 'h' )
print ("\n")
drawLine( 3, 'v' )
#########################################

## Функции. Аргументы и возвращаемые значения

#########################################
def inputInt( message ) :
    result = int ( message )
    return result

def inputFloat( message ) :
    result = float ( message )
    return result

def inputBoolean( message ) :
    result = bool ( message )
    return result
#########################################
print ()
value = input("Enter some value: ")
res = inputInt( value )
print ( res )
#########################################
n = inputInt(5)
print( n )
m = inputInt(45)
print( m )
print( n + m )

n = inputFloat(5.35)
print( n )
m = inputFloat(445.747686)
print( m )
print( n + m )

n = inputBoolean(1)
print( n )
m = inputBoolean(0)
print( m )
print( n + m )
#########################################

## Функции. Аргументы и возвращаемые значения

#########################################
def wrap_brackets_1( text ):
  return "(" + text + ")"

def wrap_brackets_2( text ):
  return "[" + text + "]"

def wrap_brackets_3( text ):
  return "<" + text + ">"
#########################################
print( wrap_brackets_3 ( wrap_brackets_3 ( ( wrap_brackets_3 ( wrap_brackets_2 (wrap_brackets_2 ( wrap_brackets_2 ( wrap_brackets_1 ( "12345" ) ) ) ) ) ) ) ) )