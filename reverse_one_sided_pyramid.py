'''row=int(input("enter the row = "))
for item in range(0,row):
    print("*"*(row-item),end="")
    print("")
'''
# ANOTHER WAY USING FUNCTION
def pattern(n):
    if(n==0):
        return
    print("*"*n)
    pattern(n-1)
pattern(5)