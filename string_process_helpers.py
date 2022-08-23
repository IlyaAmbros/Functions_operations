def remooveSpace( name ) :
    name_ = name.strip()
    return name_

def fixCase( name ) :
    name_ = name.capitalize()
    return name_

#############################
# HW1: refactor the code bellow -> pass value through a variable
# correct_name = fixCase( remooveSpace("      dOrIn       "))
name_1 = remooveSpace("      dOrIn       ")
name_2 = fixCase(name_1)
print ( F"|{name_2}|")