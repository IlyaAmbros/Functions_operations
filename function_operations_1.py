# function definition 

def hi_man( lang , name ) :
    if name :
        if lang == "en" :
            print ( f"Hellow {name} !" )
        if lang == "ru" :
            print ( f"Привет {name} !" )
        if lang == "ro" :
            print ( f"Salut {name} !" )
        else :
            print ( f"ERROR !!!" )

name = input ( "Enter a name - " )
lang = input ( "Enter the language - " )
hi_man( lang , name )