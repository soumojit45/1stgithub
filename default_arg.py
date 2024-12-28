def greet(name,ending="yo yo"):
    print(f"hello {name} good morning",end=" ")
    print(ending)
name=input("enter your name = ")
greet(name)     # it prints yo yo
greet(name,"thanks")    # it prints thanks at last