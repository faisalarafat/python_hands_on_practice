num = int(input("Enter an Integer number: "))
for i in range(1,num):
    if i%10==0:
        continue
    elif i>100:
        break
    print(i)