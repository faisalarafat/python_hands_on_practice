x = int(input("Enter a number for checking prime or not: "))
primeFlag = True
for i in range(2, x):
    if(x%i == 0):
        primeFlag=False
if(primeFlag):
    print("Prime Number")
else:
    print("Not a Prime Number")