'''def average(a,b):
    print("Average of two numbers is: ", (a+b)/2)    
average(10, 20)'''

def average(a=5,b=7):
    print(a)
    print(b)
    return (a+b)/2 
result = average(b=10, a=20)
print(result)