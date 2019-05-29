'''math,phy,che = [int(x) for x in input("Enter marks of three subjects separated by space:").split(sep=' ')]
if (math>=35 and math<=100) and (phy>=35 and phy<=100) and (che>=35 and che<=100): 
    avg = (math+phy+che)/3
    if avg<=59:
        print("You got grade C")
    elif avg>59 and avg<=69:
        print("You got grade B")
    elif avg>69:
        print("You got grade A")
else:
    print("You have failed the exam! better luck for next time")
'''
    
math,phy,che = [int(x) for x in input("Enter marks of three subjects separated by space:").split(sep=' ')]
if(math<35 or phy<35 or che<35):
    print("You have failed the exam! better luck for next time")
else:
    avg = (math+phy+che)/3
    if avg<=59:
        print("You got grade C")
    elif avg<=69:
        print("You got grade B")
    else:
        print("You got grade A")
