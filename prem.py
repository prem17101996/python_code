
'''def fact(n):
    if n<1:
        return (1)
    else: return(n * fact(n-1))

print(fact(5))'''


'''t=int(input())
for i in range(t):
    (a,b,c)=map(int,input().split(' '))
    lst=[]
    lst.append(a)
    lst.append(b)
    lst.append(c)
    lst.sort()
    print(lst[1])'''

#3 6 8


(a,b,c,d)=map(int,(input().split(' ')))
lst=[a,b,c]
print(lst)
mul=1
for i in range(len(lst)):
    mul=mul*lst[i]
    i+=1
print(mul)
lst2=[]
for j in range(len(lst)):
    devide=int(mul/lst[j])
    lst2.append(devide)
print(lst2)

lst3=[]
for i in lst2:
    print(i)
    i=str(i)

    add=0
    for j in range(len(i)):
        add=add+int(i[j])

    print(add)

    lst3.append(add)
print(lst3)
lst3.sort()
print(lst3)
print(lst3[-1])
