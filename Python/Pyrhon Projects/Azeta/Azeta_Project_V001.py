# "Aze Python 1.0" A program by Yos Sebastian

from mimetypes import init
import time
# Special Characters CHECK
import re
string_check = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
# ---------

# -------------------------------- GLOBAL VARIABLES ----------------------------------------------
main1="Azedefinition"
main2="Azelist"
main3="Skip"
main4="Aze"
main5="Exit"
main6="Aze Manual"
# ----- built-ins -------
integer1="integer"
integer2="Integer"
integer3="INTEGER"
string1="string"
string2="String"
string3="STRING"
float1="float"
float2="Float"
float3="FLOAT"
# -------------------------------- GLOBAL VARIABLES PART 2 ----------------------------------------
type_1 = "Type "
type_2 = " to get started with "
cat1 = "Python Syntax"
cat2 = "Python Comments"
cat3 = "Python Variables"
cat4 = "Python Data Types"
cat5 = "Python Numbers"
cat6 = "Python Strings"
cat7 = "Python Booleans"
cat8 = "Python Operators"
cat9 = "Python List"
cat10 = "Python Tuples"
cat11 = "Python Sets"
cat12 = "Python Dictionaries"
cat13 = "Python If-Else"
cat14 = "Python While Loops"
cat15 = "Python For Loops"
cat16 = "Python Functions"
cat17 = "Python Lambda"
cat18 = "Python Arrays"
cat19 = "Python Classes"
cat20 = "Python Inheritance"
cat21 = "Python Iterators"
cat22 = "Python Scope"
cat23 = "Python Modules"
cat24 = "Python Dates"
cat25 = "Python Math"
cat26 = "Python JSON"
cat27 = "Python RegEx"
cat28 = "Python PIP"
cat29 = "Python Try-Except"
cat30 = "Python User Input"
cat31 = "Python String Formatting"

# ------------------- GLOBAL VARIABLES FOR OPERATORS ----------------------
addition = "Addition"
subtraction = "Subtraction"
multiplication = "Multiplication"
division = "Division"
modulus = "Modulus"
exponentiation = "Exponentiation"
floor_division = "Floor Division"

aze_operators1 = "Arithmetic Operators"
aze_operators2 = "Assignment Operators"
aze_operators3 = "Comparison Operators"
aze_operators4 = "Logical Operators"
aze_operators5 = "Identity Operators"
aze_operators6 = "Membership Operators"
aze_operators7 = "Bitwise Operators"
# -----------------------


# -------------------- FOR VISUAL ------------------------------
def horizonline():
    print("------------------------------------------------------------------------------------")

# ----------------------- TO GET TO THE BEGINNING ------------------------------------
def initiation1():
    horizonline()
    print("What can I do for you?")
    print("Type \"Azelist\" to show you the complete list of what I can do") 
    print("Type \"Azedefinition\" if you want to know what\'s the program about")
    print("Type \"Exit\" to exit the program")
    print("Or just get started with any command you know in Aze Python")
    horizonline()
    inputmaster()

def initiation2():
    horizonline()
    print("I am sorry that I don't understand what you meant.")
    print("But this is just a very first program and maybe it is a bit rough")
    print("Let's start again")
    input("Press Enter to continue ...") 
    horizonline()
    initiation1()

# --------------------------------- FOR INPUTS IN MAIN MENU ------------------------------------
def inputmaster():
    horizonline()
    # -------------------------------- VARIABLES INPUTMASTER ------------------------------------
    print("Your input : ")
    input1=input()
    if input1 == main1:
        definitionaze()
    elif input1 == main2:
        listaze()
    # Arithmetic Operators ---------------------------------------
    elif input1 == addition:
        aze_addition()
    elif input1 == subtraction:
        aze_subtraction()
    elif input1 == multiplication:
        aze_multiplication()
    elif division == input1:
        aze_division()
    elif modulus == input1:
        aze_modulus()
    elif exponentiation == input1:
        aze_exponentiation()
    elif input1 == floor_division:
        aze_floordivision()
    elif aze_operators1==input1:
        listaze_operators1()
    elif aze_operators2==input1:
        listaze_operators2()
    elif aze_operators3==input1:
        listaze_operators3()
    elif aze_operators4==input1:
        listaze_operators4()
    elif aze_operators5==input1:
        listaze_operators5()
    elif aze_operators6==input1:
        listaze_operators6()
    elif aze_operators7==input1:
        listaze_operators7()
    # ---------- Per category ---------------
    elif cat1==input1:
        cat1_1()
    elif cat2==input1:
        cat2_2()
    elif cat3==input1:
        cat3_3()
    elif cat4==input1:
        cat4_4()
    elif cat5==input1:
        cat5_5()
    elif cat6==input1:
        cat6_6()
    elif cat7==input1:
        cat7_7()
    elif cat8==input1:      # Operators
        cat8_8()
    elif cat9==input1:
        cat9_9()
    elif cat10==input1:
        cat10_10()
    elif cat11==input1:
        cat11_11()
    elif cat12==input1:
        cat12_12()
    elif cat13==input1:
        cat13_13()
    elif cat14==input1:
        cat14_14()
    elif cat15==input1:
        cat15_15()
    elif cat16==input1:
        cat16_16()
    elif cat17==input1:
        cat17_17()
    elif cat18==input1:
        cat18_18()
    elif cat19==input1:
        cat19_19()
    elif cat20==input1:
        cat20_20()
    elif cat21==input1:
        cat21_21()
    elif cat22==input1:
        cat22_22()
    elif cat23==input1:
        cat23_23()
    elif cat24==input1:
        cat24_24()
    elif cat25==input1:
        cat25_25()
    elif cat26==input1:
        cat26_26()
    elif cat27==input1:
        cat27_27()
    elif cat28==input1:
        cat28_28()
    elif cat29==input1:
        cat29_29()
    elif cat30==input1:
        cat30_30()
    elif cat31==input1:
        cat31_31()

    # Closure --------------------------------------------------
    elif main5==input1:
        close()
    else:
        initiation2()
    horizonline()

def inputSkip_arithemtic_operators():
    addition = "Addition"
    subtraction = "Subtraction"
    multiplication = "Multiplication"
    division = "Division"
    modulus = "Modulus"
    exponentiation = "Exponentiation"
    floor_division = "Floor Division"
    input2=input()
    if main3==input2:
        initiation1()
    elif main4==input2:
        initiation1()
    elif main5==input2():
        close()
    elif addition==input2:
        aze_addition()
    elif subtraction==input2:
        aze_subtraction()
    elif multiplication==input2:
        aze_multiplication()
    elif division==input2:
        aze_division()
    elif modulus==input2:
        aze_modulus()
    elif exponentiation==input2:
        aze_exponentiation()
    elif floor_division == input2:
        aze_floordivision()

# +++++++++++++++++++++++++++++++++++++++++++++++++++++ ARITHMETIC ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def aze_addition():
    horizonline()
    print("You will give me two numbers that I will sum up")

    x = input("Your input : ")
    if not x.isnumeric():                   # remember that isnumeric will allow you to enter weird inputs like ² 
        initiation2()                       # and still have it counted as a valid number, but int would still not be able to convert it, so your program would crash 

    y = input("The second number : " )
    if not y.isnumeric():
        initiation2()

    print("The result of this addition is ")
    print(str(x),"+",str(y),"=", int(x)+int(y))
    horizonline()
    print("Type \"Aze\" to go back to main menu or press Enter to do this again")
    inputa=input()
    if main3==inputa:
        initiation1()
    if main4==inputa:
        initiation1()
    else:
        aze_addition()

def aze_subtraction():
    horizonline()
    print("You will give me two numbers")

    x = input("Minuend : ")
    if not x.isnumeric():                   # remember that isnumeric will allow you to enter weird inputs like ² 
        initiation2()                       # and still have it counted as a valid number, but int would still not be able to convert it, so your program would crash 

    y = input("Subtrahend : " )
    if not y.isnumeric():
        initiation2()

    print("The result of this subtraction is ")
    print(str(x),"-",str(y),"=", int(x)-int(y))
    horizonline()
    print("Type \"Aze\" to go back to main menu or press Enter to do this again")
    inputa=input()
    if main3==inputa:
        initiation1()
    if main4==inputa:
        initiation1()
    else:
        aze_addition()

def aze_multiplication():
    horizonline()
    print("You will give me two numbers to be multiplicated with each other")
    print("Multiplication is the act or process of multiplying")

    x = input("First number : ")
    if not x.isnumeric():                   # remember that isnumeric will allow you to enter weird inputs like ² 
        initiation2()                       # and still have it counted as a valid number, but int would still not be able to convert it, so your program would crash 

    y = input("Second number : " )
    if not y.isnumeric():
        initiation2()

    print("The result of this Multiplication is ")
    print(str(x),"*",str(y),"=", int(x)*int(y))
    horizonline()
    print("Type \"Aze\" to go back to main menu or press Enter to do this again")
    inputa=input()
    if main3==inputa:
        initiation1()
    if main4==inputa:
        initiation1()
    else:
        aze_multiplication()
    
def aze_division():
    horizonline()
    print("You will give me two numbers")
    print("Division is a simple operation in which a number is divided")

    x = input("Dividend : ")
    if not x.isnumeric():                   # remember that isnumeric will allow you to enter weird inputs like ² 
        initiation2()                       # and still have it counted as a valid number, but int would still not be able to convert it, so your program would crash 

    y = input("Divisor : " )
    if not y.isnumeric():
        initiation2()

    print("The result of this Division is ")
    print(str(x),"/",str(y),"=", int(x)/int(y))
    horizonline()
    print("Type \"Aze\" to go back to main menu or press Enter to do this again")
    inputa=input()
    if main3==inputa:
        initiation1()
    if main4==inputa:
        initiation1()
    else:
        aze_division()


def aze_modulus():
    horizonline()
    print("You will give me two numbers")
    print("Modulus is to find the remainder after division")

    x = input("Dividend : ")
    if not x.isnumeric():                   # remember that isnumeric will allow you to enter weird inputs like ² 
        initiation2()                       # and still have it counted as a valid number, but int would still not be able to convert it, so your program would crash 

    y = input("Divisor : " )
    if not y.isnumeric():
        initiation2()

    print("The result of this Modulus is ")
    print(str(x),"%",str(y),"=", int(x)%int(y))
    horizonline()
    print("Type \"Aze\" to go back to main menu or press Enter to do this again")
    inputa=input()
    if main3==inputa:
        initiation1()
    if main4==inputa:
        initiation1()
    else:
        aze_modulus()

def aze_exponentiation():
    horizonline()
    print("You will give me two numbers")
    print("Exponentiation is the operation of raising one quantity to the power of another.")

    x = input("Base : ")
    if not x.isnumeric():                   # remember that isnumeric will allow you to enter weird inputs like ² 
        initiation2()                       # and still have it counted as a valid number, but int would still not be able to convert it, so your program would crash 

    y = input("Exponent : " )
    if not y.isnumeric():
        initiation2()

    print("The result of this Exponentiation is ")
    print(str(x),"^",str(y),"=", int(x)^int(y))
    horizonline()
    print("Type \"Aze\" to go back to main menu or press Enter to do this again")
    inputa=input()
    if main3==inputa:
        initiation1()
    if main4==inputa:
        initiation1()
    else:
        aze_exponentiation()

def aze_floordivision():
    horizonline()
    print("You will give me two numbers")
    print("Floor division is a normal division operation except that it returns the largest possible integer.")

    x = input("Dividend : ")
    if not x.isnumeric():                   # remember that isnumeric will allow you to enter weird inputs like ² 
        initiation2()                       # and still have it counted as a valid number, but int would still not be able to convert it, so your program would crash 

    y = input("Divisor : " )
    if not y.isnumeric():
        initiation2()

    print("The result of this Floor Division is ")
    print(str(x),"//",str(y),"=", int(x)//int(y))
    horizonline()
    print("Type \"Aze\" to go back to main menu or press Enter to do this again")
    inputa=input()
    if main3==inputa:
        initiation1()
    if main4==inputa:
        initiation1()
    else:
        aze_floordivision()

# ++++++++++++++++++++++++++++++++++++++ ASSIGNMENT OPERATORS ++++++++++++++++++++++++++++++++++++++++++++++++

def aze_assignment():
    horizonline()
    print("Welcome to Assignment Operators")
    print("Assignment operators are used to assign values to variables")
    print("For now this feature only accepts integer :)")
    print("Give me a number for the variable x")
    x = input("x = ")
    if not x.isnumeric():                   # remember that isnumeric will allow you to enter weird inputs like ² 
        initiation2()                       # and still have it counted as a valid number, but int would still not be able to convert it, so your program would crash 
    print("Give me a second number that will modify your x with")
    y = input("y = ")
    if not y.isnumeric():                   # remember that isnumeric will allow you to enter weird inputs like ² 
        initiation2()                       # and still have it counted as a valid number, but int would still not be able to convert it, so your program would crash 
    horizonline()
    print("To cut the bullshit, I will give you the list of results of what happened to your x")
    horizonline()
    print("As a reminder, your initial x was ",str(x))
    print("With (+), x is now ", "x = x + ",str(y)," = ",int(x)+int(y))
    print("With (-), x is now ", "x = x - ",str(y)," = ",int(x)-int(y))
    print("With (*), x is now ", "x = x * ",str(y)," = ",int(x)*int(y))
    print("With (/), x is now ", "x = x / ",str(y)," = ",int(x)/int(y))
    print("With (%), x is now ", "x = x % ",str(y)," = ",int(x)%int(y))
    print("With (//), x is now ", "x = x // ",str(y)," = ",int(x)//int(y))
    print("With (**), x is now ", "x = x ** ",str(y)," = ",int(x)**int(y))
    print("With (&), x is now ", "x = x & ",str(y)," = ",int(x)&int(y))
    print("With (|), x is now ", "x = x | ",str(y)," = ",int(x)|int(y))
    print("With (^), x is now ", "x = x ^ ",str(y)," = ",int(x)^int(y))
    print("With (>>), x is now ", "x = x >> ",str(y)," = ",int(x)>>int(y))
    print("With (<<), x is now ", "x = x << ",str(y)," = ",int(x)<<int(y))
    horizonline()
    print("Type \"Aze\" to go back to main menu or press Enter to do this again")
    inputa=input()
    if main3==inputa:
        initiation1()
    if main4==inputa:
        initiation1()
    if main5==inputa:
        close()
    else:
        aze_assignment()

# ++++++++++++++++++++++++++++++++++ Comparison Operators +++++++++++++++++++++++++++++++

def aze_comparison():
    horizonline()
    print("Welcome to Comparison Operators")
    print("Comparison operators are used to compare two values")
    print("This feature accepts strings and integers")
    print("You need to assign values for two variables, but")
    print("Both of them must be either INTEGERS or STRINGS")
    horizonline()
    x = input("Variable x is ")      
    y = input("Variable y is ")
    horizonline()
    if (x.isnumeric() and  y.isnumeric()) or (not x.isnumeric() and not y.isnumeric()):
        print("The Equality or x == y is ", x == y, "because :", x, "equals to", y, "is", x==y)
        print("The Inequality or x != y is ", x != y, "because :", x, "not equals to", y, "is", x!=y)
        print("The Greatness or x > y is ", x == y, "because :", x, "greater than", y, "is", x>y)
        print("The Lessness or x < y is ", x == y, "because :", x, "less than", y, "is", x<y)
        print("The Greatness and Equality or x >= y is ", x >= y, "because :", x, "greater or equals to", y, "is", x>=y)
        print("The Lessness and Equality or x <= y is ", x <= y, "because :", x, "less or equals to", y, "is", x==y)
        horizonline()
    else:
        print("I told you not to put different types of value into the variables")
        print("Now start again with Comparison Operators")
        input("Press Enter to continue...")
        horizonline()
        aze_comparison()
    print("Type \"Aze\" to go back to main menu or press Enter to do this again")
    inputa=input()
    if main3==inputa:
        initiation1()
    if main4==inputa:
        initiation1()
    if main5==inputa:
        close()
    else:
        aze_comparison()
    horizonline()

# ++++++++++++++++++++++++++++++++++++++ LOGICAL OPERATORS ++++++++++++++++++++++++++++++++++++++++++++++++
def aze_logical():
    horizonline()
    print("Welcome to Logical Operators")
    print("Logical operators are used to combine conditional statements.")
    print("This feature accepts string or integer")
    print("I can put this in huge amounts of examples, but I will show you few")
    print("as long as you get the idea.")
    print("You need to assign values for three variables, but")
    print("All of them of them must be either INTEGERS or STRINGS")
    horizonline()
    x = input("Variable x is ")      
    y = input("Variable y is ")
    z = input("Variable z is ")
    print("We will use z as your base comparator")
    horizonline()
    if (x.isnumeric() and  y.isnumeric() and z.isnumeric()) or (not x.isnumeric() and not y.isnumeric() and not z.isnumeric()):
        print("AND Operator.",z," < ",x," and ",z," < ",y)
        print("Result :", z < x and z < y)
        print("OR Operator.",z," < ",x," or ",z," < ",y)
        print("Result :", z < x or z < y)
        print("NOT Operator."," Not ",z," > ",x," and ",z," < ",y)
        print("Result :",not(z>x and z<y))
    else:
        print("I told you not to put different types of value into the variables")
        print("Now start again with Comparison Operators")
        input("Press Enter to continue...")
        horizonline()
        aze_logical()
    print("Type \"Aze\" to go back to main menu or press Enter to do this again")
    inputa=input()
    if main3==inputa:
        initiation1()
    if main4==inputa:
        initiation1()
    if main5==inputa:
        close()
    else:
        aze_logical()
    horizonline()

# ++++++++++++++++++++++++++++++++++++++ IDENTITY OPERATORS ++++++++++++++++++++++++++++++++++++++++++++++++
def aze_identity():
    horizonline()
    print("Welcome to Identity Operators")
    print("Identity operators are used to compare the objects, not if they are equal") 
    print("but if they are actually the same object, with the same memory location")
    print("This feature accepts string or integer")
    print("You need to assign values for two variables, but")
    print("Both of them of them must be either INTEGERS or STRINGS")
    horizonline()
    x = input("Variable x is ")      
    y = input("Variable y is ")
    if (x.isnumeric() and  y.isnumeric()) or (not x.isnumeric() and not y.isnumeric()):
        print(x," is ",y," = ",x is y)
        print(x," is not ",y," = ", x is not y)
        horizonline()
    else:
        print("I told you not to put different types of value into the variables")
        print("Now start again with Comparison Operators")
        input("Press Enter to continue...")
        horizonline()
        aze_comparison()
    print("Type \"Aze\" to go back to main menu or press Enter to do this again")
    inputa=input()
    if main3==inputa:
        initiation1()
    if main4==inputa:
        initiation1()
    if main5==inputa:
        close()
    else:
        aze_identity()
    horizonline()


# ++++++++++++++++++++++++++++++++++++++ MEMBERSHIP OPERATORS ++++++++++++++++++++++++++++++++++++++++++++++++
def aze_membership():
    horizonline()
    print("Welcome to Membership Operators")
    print("Membership operators are used to test if a sequence is presented in an object") 
    print("This feature accepts string or integer")
    print("You need to assign values for two, but")
    print("But variable x is a list")
    horizonline()
    xlist = input("Enter elements of a list seperated by space ")
    user_list=xlist.split()
    print("\n")
    print('List of x: ', user_list)
    y = input("Variable y is ")
    horizonline()
    print("IN Operator : Returns True if a sequence with the specified value is present in the object")
    print("Is y in the list?",y in user_list)
    if (y in user_list) == True:
        print(y, "is indeed in the list")
    else:
        print("No, ",y," is not in the list")
    print("NOT IN Operator : Returns True if a sequence with the specified value is not present in the object")
    print("Is y not in the list?",y not in user_list)
    if (y not in user_list) == True:
        print(y, "is indeed not in the list")
    else:
        print("No, actually ",y," is in the list")
    horizonline()
    print("Type \"Aze\" to go back to main menu or press Enter to do this again")
    inputa=input()
    if main3==inputa:
        initiation1()
    if main4==inputa:
        initiation1()
    if main5==inputa:
        close()
    else:
        aze_membership()
    horizonline()
# ++++++++++++++++++++++++++++++++++++++ BITWISE OPERATORS ++++++++++++++++++++++++++++++++++++++++++++++++
def aze_bitwise():
    horizonline()
    print("Welcome to Bitwise Operators")
    print("Bitwise operators are used to compare (binary) numbers")
    print("Please input only INTEGERS for these two variables")
    print("I will convert your numbers into binary")
    x = input("x = ")
    if not x.isnumeric():                   # remember that isnumeric will allow you to enter weird inputs like ² 
        print("I told you to put integers only. Now we start again")
        aze_bitwise()                       # and still have it counted as a valid number, but int would still not be able to convert it, so your program would crash 
    y = input("y = ")
    if not y.isnumeric():                   # remember that isnumeric will allow you to enter weird inputs like ² 
        print("I told you to put integers only. Now we start again")
        aze_bitwise()                         # and still have it counted as a valid number, but int would still not be able to convert it, so your program would crash 
    print("X in Binary is ")
    DecimalToBinary(int(x))
    print('')
    print("Y in Binary is ")
    DecimalToBinary(int(y))
    print('')
    horizonline()
    print("Assume that x and y have been converted to binaries")
    print("Bitwise AND (&) -> x & y")
    print(int(x)," & ",int(y)," = ",int(x)&int(y))
    print("Bitwise OR (|) -> x | y")
    print(int(x)," & ",int(y)," = ",int(x)|int(y))
    print("Bitwise NOT (~) -> ~ x")
    print("We only need one variable for this one")
    print("~",int(x)," = ", ~int(x))
    print("~",int(y)," = ", ~int(y))
    print("Bitwise XOR (^) -> x ^ y")
    print(int(x)," ^ ",int(y)," = ",int(x)^int(y))
    print("Bitwise right shift (>>) -> x >> y")
    print(int(x)," >> ",int(y)," = ",int(x)>>int(y))
    print("Bitwise left shift (<<) -> x << y")
    print(int(x)," << ",int(y)," = ",int(x)<<int(y))
    horizonline()
    print("Type \"Aze\" to go back to main menu or press Enter to do this again")
    inputa=input()
    if main3==inputa:
        initiation1()
    if main4==inputa:
        initiation1()
    if main5==inputa:
        close()
    else:
        aze_bitwise()
    horizonline()


def DecimalToBinary(num):               # TO CONVERT DECIMAL TO BINARY
     
    if num >= 1:
        DecimalToBinary(num // 2)
    print(num % 2, end = '')
 



# ----------------- SKIP BUTTONS ------------------------------------------------
def inputSkip_Azelist():
    horizonline()
    input3=input()
    if main3 == input3:
        initiation1()
    elif main4 == input3:
        initiation1()
    elif main2==input3:
        listaze()
    elif main5==input3:
        close()
    elif main1==input3:
        definitionaze()
    elif main2==input3:
        listaze()
    # OPERATORS ==============================================
    elif aze_operators1==input3:
        listaze_operators1()
    elif aze_operators2==input3:
        listaze_operators2()
    elif aze_operators3==input3:
        listaze_operators3()
    elif aze_operators4==input3:
        listaze_operators4()
    elif aze_operators5==input3:
        listaze_operators5()
    elif aze_operators6==input3:
        listaze_operators6()
    elif aze_operators7==input3:
        listaze_operators7()
    else:
        initiation1()

def Skipmaster():
    horizonline()
    input3=input()
    if main3 == input3:
        initiation1()
    elif main4 == input3:
        initiation1()
    elif main2==input3:
        listaze()
    elif main5==input3:
        close()
    elif main1==input3:
        definitionaze()
    elif main2==input3:
        listaze()
    horizonline()

# ------------------------------ CONTENTS -------------------------------------------------
def listaze():
    horizonline()
    print("This is a long list to show the basic features of Python.")
    print("Type \"Aze\" to go to main menu or press Enter to proceed into the list")
    Skipmaster()
    horizonline()
    print("Type \"Python Intro\" to be introduced with Python")
    print("Or type \"Learn Python\" to be advised how to start learning Python.")
    horizonline()
    print("Type \"Aze\" to go to main menu or press Enter to proceed into the list")
    Skipmaster()
    horizonline()
    print(type_1 + "\"" + cat1 + "\"" + type_2 + cat1)
    print(type_1 + "\"" + cat2 + "\"" + type_2 + cat2)
    print(type_1 + "\"" + cat3 + "\"" + type_2 + cat3)
    print(type_1 + "\"" + cat4 + "\"" + type_2 + cat4)
    print(type_1 + "\"" + cat5 + "\"" +  type_2 + cat5)
    print(type_1 + "\"" + cat6 + "\"" +  type_2 + cat6)
    print(type_1 + "\"" + cat7 + "\"" + type_2 + cat7)
    print(type_1 + "\"" + cat8 + "\"" +  type_2 + cat8)     # Python Operators
    print(type_1 + "\"" + cat9 + "\"" + type_2 + cat9)
    print(type_1 + "\"" + cat10 + "\"" + type_2 + cat10)
    print(type_1 + "\"" + cat11 + "\"" + type_2 + cat11)
    print(type_1 + "\"" + cat12 + "\"" + type_2 + cat12)
    print(type_1 + "\"" + cat13 + "\"" + type_2 + cat13)
    print(type_1 + "\"" + cat14 + "\"" + type_2 + cat14)
    print(type_1 + "\"" + cat15 + "\"" + type_2 + cat15)
    print(type_1 + "\"" + cat16 + "\"" + type_2 + cat16)
    print(type_1 + "\"" + cat17 + "\"" + type_2 + cat17)
    print(type_1 + "\"" + cat18 + "\"" + type_2 + cat18)
    print(type_1 + "\"" + cat19 + "\"" + type_2 + cat19)
    print(type_1 + "\"" + cat20 + "\"" + type_2 + cat20)
    print(type_1 + "\"" + cat21 + "\"" + type_2 + cat21)
    print(type_1 + "\"" + cat22 + "\"" + type_2 + cat22)
    print(type_1 + "\"" + cat23 + "\"" + type_2 + cat23)
    print(type_1 + "\"" + cat24 + "\"" + type_2 + cat24)
    print(type_1 + "\"" + cat25 + "\"" + type_2 + cat25)
    print(type_1 + "\"" + cat26 + "\"" + type_2 + cat26)
    print(type_1 + "\"" + cat27 + "\"" + type_2 + cat27)
    print(type_1 + "\"" + cat28 + "\"" + type_2 + cat28)
    print(type_1 + "\"" + cat29 + "\"" + type_2 + cat29)
    print(type_1 + "\"" + cat30 + "\"" + type_2 + cat30)
    print(type_1 + "\"" + cat31 + "\"" + type_2 + cat31)
    horizonline()
    input("Press Enter to go back to main menu...")
    initiation1()
    horizonline()
    time.sleep(1)


# ------------------------------ SYNTAX --------------------------
def cat1_1(): # Syntax Category
    horizonline()
    print("This is about Python Syntax")
    print("""
    The syntax of the Python programming language is the set of rules that defines 
    how a Python program will be written and interpreted
    (by both the runtime system and by human readers).""")
    horizonline()
    print("If you have active Python in a shell or command-prompt")
    print("Python syntax can be executed by writing directly in the command line")
    print("Or you can create python file (.py) and run it in the command line.")
    print("Press Enter to continue...")
    horizonline()
    print("Python has Indentation")
    print("Indentation refers to the spaces at the beginning of a code line")
    print("Where in other programming languages the indentation in code is readability only,")
    print("The indentation in Python is very important.")
    print("Python uses indentation to indicate a block of code")
    horizonline()
    print("Example :")
    print("Below is a correct example of code - also not an output")
    print("If x > y:")
    print("    print(\"Correct Indentation\")")
    print("Below is a wrong example of code - also not an output.")
    print("If x > y:")
    print("print(\"Wrong Indentation\")")
    input("If you understood, press Enter to continue...")
    horizonline()
    print("You will be given \"Syntax Error\" if your indentation is wrong")
    print("But the number of spaces is up to you as a programmer, the most common use is four, but it has to be at least one.")
    print("Also you have to use the same number of spaces in the same block of code, otherwise Python will give you an error.")
    horizonline()
    input("Press Enter to go back to main menu.")
    initiation1()

def cat2_2(): # Comments Category
    maintenance()

def cat3_3(): # Variable Category
    vartype=''
    horizonline()
    print("Welcome to Python Variables!")
    print("Variables are containers for storing data values.")
    horizonline()
    print("First, let's try to create variables")
    varname=input("Give me a name for a variable      : ")

    if(string_check.search(varname) == None):
        varname=(str(varname))
    else:
        horizonline()
        print("Unfortunately, your variable contains Special Characters.")
        print("And Python doesn't accept Special Characters in variable name.")
        print("Now we restart this feature")
        input("Press Enter to continue...")
        cat3_3()
    
    print("Next, give me the value for this variable  : ")
    varvalue=input(varname + " = ",)
    def vartypedef():
        print("You want to decide if this value is string, integer, or even float")
        nonlocal vartype
        vartype=input("Data type : ")

        nonlocal varvalue
        if (integer1 or integer2 or integer3) == vartype:
            if varvalue.isnumeric():
                varvalue=int(varvalue)
            elif not varvalue.isnumeric():
                horizonline()
                print("Wow, you lied to a program. That's pathetic. Your value is not even numeric. Now resubmit the variable type.")
                horizonline()
                vartypedef()
        elif (string1 or string2 or string3) == vartype:
            varvalue=str(varvalue)
        elif (float1 or float2 or float3) == vartype:
            if varvalue.isnumeric():
                varvalue=float(varvalue)
            elif not varvalue.isnumeric():
                horizonline()
                print("Wow, you lied to a program. That's pathetic. Your value is not even numeric. Now resubmit the variable type.")
                horizonline()
                vartypedef()
        else:
            horizonline()
            print("You must assign a data type for your variable!")
            horizonline()
            vartypedef()
    vartypedef()
    horizonline()
    print("Great!")
    print("You have a variable with the name of " + varname)
    print("And the value of " + varname + " is " + varvalue)
    if varname.isnumeric():
        print("Weird that you assign a variable name with numbers only, but you have : ")
        print(varname + " = " + varvalue)
    elif not varname.isnumeric():
        print(varname + " = " + varvalue)
    print("The type of " + varname + " is " + type(varname))
    print("The type of " + varvalue + " is " + type(varvalue))
    horizonline()
    print("For extra information.")
    print("Specifiyng the data type of a variable is called Casting.")
    print("Also Variable names are case-sensitive.")
    horizonline()
    print("Type \"Aze\" to go back to main menu or press Enter to do this again")
    inputa=input()
    if main3==inputa:
        initiation1()
    elif main4==inputa:
        initiation1()
    elif main5==inputa:
        close()
    else:
        cat3_3()
    
def cat4_4(): # Data Types Category
    maintenance()

def cat5_5(): # Syntax Category
    maintenance()

def cat6_6(): # Syntax Category
    maintenance()

def cat7_7(): # Syntax Category
    maintenance()

# ---------------------------------------------------------------- OPERATORS -----------------------------------------------------------------
    
def cat8_8(): # Operators Category
    horizonline()
    print("This is a list about Operators")
    horizonline()
    print("Type \"Arithmetic Operators\" to see the list in Arithmetic Operators Category")
    print("Type \"Assignment Operators\" to start with Assignment Operators Category")
    print("Type \"Comparison Operators\" to start with Comparison Operators Category")
    print("Type \"Logical Operators\" to start with Logical Operators Category")
    print("Type \"Identity Operators\" to start with Identity Operators Category")
    print("Type \"Membership Operators\" to start with Membership Operators Category")
    print("Type \"Bitwise Operators\" to start with Bitwise Operators Category")
    horizonline()
    print("Input your command or press Enter to go back to main menu..")
    print("((A typo will make you go back to main menu.))")
    inputSkip_Azelist()
    time.sleep(1)

def listaze_operators1(): # Arithmetic
    horizonline()
    print("This is a list about Arithmetic Operators:")
    horizonline()
    print("-- Here is about arithmetic operators --")
    print("Arithmetic operators are used with numeric values to perform common mathematical operations.")
    print("Type \"Addition\" to sum two numbers together")
    print("Type \"Subtraction\" to subtract a number from another number")
    print("Type \"Multiplication\" to multiply two numbers with each other")
    print("Type \"Division\" to divide between two numbers")
    print("Type \"Modulus\" to find out the remainers of a division between two numbers")
    print("Type \"Exponentation\" to do a power calculation between two numbers")
    print("Type \"Floor Division\" to find out how many times can a Divisor divide a Divident")
    horizonline()
    inputSkip_arithemtic_operators()
    time.sleep(1)

def listaze_operators2(): # Assignment
    horizonline()
    aze_assignment()
    time.sleep(1)
    horizonline()

def listaze_operators3(): # Comparison
    horizonline()
    aze_comparison()
    time.sleep(1)
    horizonline()

def listaze_operators4(): # Logical
    horizonline()
    aze_logical()
    time.sleep(1)
    horizonline()

def listaze_operators5(): # Identity
    horizonline()
    aze_identity()
    time.sleep(1)
    horizonline()

def listaze_operators6(): # Membership
    horizonline()
    aze_membership()
    time.sleep(1)
    horizonline()

def listaze_operators7(): # Bitwise
    horizonline()
    aze_bitwise()
    time.sleep(1)
    horizonline()

# ----------------------------------- List Category ----------------------------------

def cat9_9(): # Syntax Category
    maintenance()

def cat10_10(): # Syntax Category
    maintenance()

def cat11_11(): # Syntax Category
    maintenance()

def cat12_12(): # Syntax Category
    maintenance()

def cat13_13(): # Syntax Category
    maintenance()

def cat14_14(): # Syntax Category
    maintenance()

def cat15_15(): # Syntax Category
    maintenance()

def cat16_16(): # Syntax Category
    maintenance()

def cat17_17(): # Syntax Category
    maintenance()

def cat18_18(): # Syntax Category
    maintenance()

def cat19_19(): # Syntax Category
    maintenance()

def cat20_20(): # Syntax Category
    maintenance()

def cat21_21(): # Syntax Category
    maintenance()

def cat22_22(): # Syntax Category
    maintenance()

def cat23_23(): # Syntax Category
    maintenance()

def cat24_24(): # Syntax Category
    maintenance()

def cat25_25(): # Syntax Category
    maintenance()

def cat26_26(): # Syntax Category
    maintenance()

def cat27_27(): # Syntax Category
    maintenance()

def cat28_28(): # Syntax Category
    maintenance()

def cat29_29(): # Syntax Category
    maintenance()

def cat30_30(): # Syntax Category
    maintenance()

def cat31_31(): # Syntax Category
    maintenance()


# ------------------ WHAT ABOUT A GOOD CLOSURE ----------------------------
def definitionaze():
    print("...")
    time.sleep(1)  
    print("Program name : Aze Python (Version 1.1)")
    print("I am a program that mainly can show you basic features in Python.")
    print("So that we can have better understanding about them.")
    print("So please use my features :)")
    print("Please be advised that this program doesn't accept typos unfortunately :(")
    print("Type \"Aze Manual\" to see the complete manual of this program in another window" )
    print("Written by Yos Sebastian (IG:@yos.sebastian)")
    input("Press Enter to continue...")
    horizonline()
    initiation1()
    
def close():
    horizonline()
    print("Sad to see you go :(")
    print("For your info :")
    print("Aze Python is expected to have basic calculator feature in the future update")
    print("So, I hope you come back and use my features again :)")
    print("If you have suggestions or want to criticize, write to yossebastiands@gmail.com.")
    print("-------------------------------------------- PROGRAM ENDED --------------------------------------------")
    quit()

def maintenance():
    horizonline()
    print("This section is under maintenance")
    input("Press Enter to continue...")
    horizonline()
    initiation1()

# -------------------- THE BEGINNING OF PROGRAM ------------------------------------------------
horizonline()
print("Hello! I am a program made by Yos Sebastian called Aze Python")
print("This is version 1.1")
horizonline()

input("Press Enter to continue...")
horizonline()

time.sleep(1)       # A delay given. (time) is the imported package. (sleep) is a function within (time)

initiation1()

horizonline()


