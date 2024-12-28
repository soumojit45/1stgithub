''' Create a simple calculator that performs addition, subtraction, multiplication, and division based on user input. '''
import math
print('''
            1: add
            2: minus
            3: division
            4: multiplication
            5: exp
            6: sin(x)  x in degree
            7: cos(x)  x in degree
            8: tan(x)  x in degree
            9: cosec(x)  x in degree
            10: sec(x)  x in degree
            11: cot(x)  x in degree
''')

option=int(input("enter an option = "))
if option==1:
    n1=float(input("enter a number = "))
    n2=float(input("enter a number = "))
    print(f"{n1} + {n2} = {n1+n2}")
elif option==2:
    n1=float(input("enter a number = "))
    n2=int(input("enter a number = "))
    print(f"{n1} - {n2} = {n1-n2}")
elif option==3:
    n1=float(input("enter a number = "))
    n2=float(input("enter a number = "))
    print(f"{n1} / {n2} = {n1/n2}")
elif option==4:
    n1=float(input("enter a number = "))
    n2=float(input("enter a number = "))
    print(f"{n1} X {n2} = {n1*n2}")
elif option==5:
    n1=float(input("enter base = "))
    n2=float(input("enter power = "))
    print(f"{n1} ^ {n2} = {n1**n2}")
elif option==6:
    x_in_degree = float(input(" enter value of x : "))
    x_in_radian = math.radians(x_in_degree)
    print(f"SIN {x_in_degree} = {math.sin(x_in_radian):.4f}")
elif option==7:
    x_in_degree = float(input(" enter value of x : "))
    x_in_radian = math.radians(x_in_degree)
    print(f"COS {x_in_degree} = {math.cos(x_in_radian):.4f}")
elif option==8:
    x_in_degree = float(input(" enter value of x : "))
    x_in_radian = math.radians(x_in_degree)
    print(f"TAN {x_in_degree} = {math.tan(x_in_radian):.4f}")
elif option==9:
    x_in_degree = float(input(" enter value of x : "))
    x_in_radian = math.radians(x_in_degree)
    print(f"COSEC {x_in_degree} = {(1/math.sin(x_in_radian)):.4f}")
elif option==10:
    x_in_degree = float(input(" enter value of x : "))
    x_in_radian = math.radians(x_in_degree)
    print(f"SEC {x_in_degree} = {(1/math.cos(x_in_radian)):.4f}")
elif option==11:
    x_in_degree = float(input(" enter value of x : "))
    x_in_radian = math.radians(x_in_degree)
    print(f"COT {x_in_degree} = {(1/math.tan(x_in_radian)):.4f}")
else:
    print("PRINT A VALID OPTION ")