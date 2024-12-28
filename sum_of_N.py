def sum_natural_num(last_term):
    if(last_term==1):
        return 1
    return last_term+sum_natural_num(last_term-1)
last_term = int(input("enter last number = "))
print(sum_natural_num(last_term))
# enter last number = 100 output : 5050

