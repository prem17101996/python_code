m,d=input().split()
m=int(m)
d=float(d)
if(m%5==0 and (m+0.5)<d):
    
   print("{0:.2f}".format(d-m-0.5))

else:
    print(d)
