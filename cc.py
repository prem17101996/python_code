import math
a=int(input())
while(a>=0):
    if(a==2 or a==3):
        print("false")
        break
    b=int(math.sqrt(a))
    a=a-(b*b)
else:
    print("true")
