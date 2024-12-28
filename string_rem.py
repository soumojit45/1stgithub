# Write a python function to remove a given word from a list ad strip it at the same time.
def remove_from_string(l,word):
    n=[]
    for item in l:
        if not(item==word):
            n.append(item.strip(word))
    return n
l=["harry","rohan","kuran","simran"]
print(remove_from_string(l,"an"))