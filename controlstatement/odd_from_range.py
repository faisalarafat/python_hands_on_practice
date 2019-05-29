a,b = [int(x) for x in input("Enter minimum and maximum number separated by comma: ").split(sep=',')]
i=a
if i%2 == 0: i = x+1
while(i<=b):
    print(i)
    i+=2