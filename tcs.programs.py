#1 program

# w1 = input()
# for i in w1:
#     if i == "a" or i == "e" or i == "i" or i == "o" or i == "u" or i == "A" or i == "E" or i == "I" or i == "O" or i == "U":
#         w1 = w1.replace(i, "%")
#
# w2 = input()
# for i in w2:
#     if i == "a" or i == "e" or i == "i" or i == "o" or i == "u" or i == "A" or i == "E" or i == "I" or i == "O" or i == "U":
#         pass
#
#     else:
#         w2 = w2.replace(i, "#")
#
# w3 = input()
# w3 = w3.upper()
# print(w1 + w2 + w3)
#3
# number=int(input())
# n1=number
# n2=number
# lst=[1,1]
# lst1=[]
# lst2=[]
# for i in range(1,n1):
#     n11=2**i
#     lst1.append(n11)
# for i in range(1, n1):
#     n12 = 3 ** i
#     lst2.append(n12)
# for i in range(len(lst1)):
#     lst.append(lst1[i])
#     lst.append(lst2[i])
#
# result=(lst[number-1])
# print(result)
# import numpy as np
# lst1= ([1, 6, 5],[3 ,4, 8],[2, 12, 3])
# lst2=([3, 4, 6],[5, 6, 7],[6,56, 7])
# c=np.dot(lst1,lst2)
# print(c)
# num = int(input())
# arr = []
# sum = 0
# count = 0
# if num > 1:
#     for i in range(2, num + 2):
#         for j in range(2, i):
#             if i % j == 0:
#                 break
#         else:
#             arr.append(i)
# def is_prime(sum):
#     for i in range(2, (sum // 2) +2):
#         if sum % i == 0:
#             return False
#         else:
#             return True
# for i in range(0, len(arr)):
#     sum = sum + arr[i]
#     if sum <= num:
#         if is_prime(sum):
#             count = count + 1
#
# print(count)


##SQUARE FREE NUMBERS
# n=int(input())
# lst=[]
# lst1=[]
# for i in range(2,n+1):
#     if n % i == 0:
#         lst.append(i)
#         for j in range(i):
#             if j*j==i:
#                 lst1.append(i)
#
#
# lst2=[]
# lst=[2,3,4,6,8,9,12,18,36,72]
# lst1=[4,9,36]
# for i in lst:
#     for j in lst1:
#         if i%j==0:
#             lst2.append(i)
# lst2=set(lst2)
# lst3=list(lst2)
#
# for i in range(len(lst3)):
#     lst.remove(lst3[i])
# print(lst)
# print(len(lst))
# num=0
# n=[7, 7, 1, 3, 8, 2, 5]
# for i in range(len(n)):
#     if len(n)>0:
#         nmax= max(n)
#         num=num+nmax
#         ind=n.index(nmax)
#
#         if ind>1:
#             n.remove(n[ind-1])
#             n.remove(n[ind-1])
#             n.remove(n[ind-1])
#
#         else:
#             n.remove(n[0])
#             n.remove(n[0])
#
#
#
# print(num)
# nput: 20 3
# 921 107 270 631 926 543 589 520 595 93 873 424 759 537 458 614 725 842 575 195
# 1 100
# 50 600
# 1 1000
#
#
# n1=map(int,(input().split()))
# n1=list(n1)
# n2=list[map(int,(input().split()))]
# n3=list[map(int,(input().split()))]
# n4=list[map(int,(input().split()))]

#n2=list(n2)
# n3=list(n3)
# n4=list(n4)

#COUNTING ROCK SAMPLE

# n1=map(int, (input().split()[:2]))
# n1=list(n1)
# n2=map(int, (input().split()[:n1[0]]))
# n2=list(n2)
# n2.sort()
# lst1=[]
# for i in range(n1[1]):
#     n = map(int, (input().split()))
#     n=list(n)
#
#     lst=[]
#     for j in range(len(n2)):
#
#         if n[0]<n2[j]<n[1]:
#
#
#             lst.append(n2[j])
#
#     lst1.append(len(lst))
#
# for i in lst1:
#     print(i,end=" ")


#2  CONSECUTIVE PRIME NUMBER
# n=int(input())
# lst=[]
# for num in range(2,n+1):
#     for i in range(2,num):
#         if num%i==0:
#             break
#     else:
#         lst.append(num)
#
# add=2
# count=0
# for i in range(len(lst)-1):
#     add=add+lst[i+1]
#     if add in lst:
#         count+=1
#
# print(count)

#Kth FIND


# n,k=map(int,input().split())
# lst=[]
# for i in range(1,n+1):
#     if n%i==0:
#         lst.append(i)
# if len(lst)<k:
#     print("1")
# else:
#     print(lst[k])

#
# COLLECTING CANDEES PROBLEM
# t=int(input())
# for i in range(t):
#     n=int(input())
#     n1=list(map(int,(input().split() [:n])))
#     sum1=n1[0]
#     lst=[]
#     for j in range(1,len(n1)):
#         sum1=sum1+n1[j]
#
#         lst.append(sum1)
#
#     # add=0
#     # for k in range(len(lst)):
#     #     add=add+lst[k]
#     # print(add)
#     print(sum(lst))

#
# philaland coin program

# no_of_ways=int(input())
# value = list(map(int,input().split()))
# for i in value:
#     count = 0
#     #logic number of coins required will be one more than the earlier rupee value that was a power of 2
#     while i>=1:
#         i=i//2
#         count=count+1
#     print(count)

# EXCHANGE DIGITS PROBLEM
from itertools import permutations
# a="5312"
# b=1235
#
# # a1=str(a)
# # a,b=map(str,(input().split()))
#
# # lst=[]
# # for i in range(len(a1)):
# #     lst.append(int(a1[i]))
# lst=[]
# permlist=list(permutations((a)))
# for i in permlist:
#
#     lst.append(int("".join(i)))
# # print(lst)
# if b in lst:
#     lst.remove(b)
# # print(lst)
# lst1=[]
# for i in range(len(lst)):
#     subs=lst[i]-int(b)
#     lst1.append(subs)
# # print(lst1)
#
# n=0
# lst2=[]
# for i in range(len(lst1)):
#
#     if lst1[i]>=0:
#         # print(i)
#         lst2.append(lst[i])
#         mini=min(lst2)
# # print(lst2)
# print(mini)
# lst1i=lst.index(mini)
# print(lst1i)
# # print(lst[3])

# n="PREM KUMAR MISHRA"
# print(n[::-1])

from itertools import permutations
# a,b=map(str,(input().split()))
# a1=str(a)
# lst=[]
# for i in range(len(a1)):
#     lst.append(int(a1[i]))

# permlist=list(permutations([4,5],3))
# for i in permlist:
#     print(i)
# a,b=map(int,(input().split()))
# lst=[]
# lst.append(a)
# lst.append(b)
# k=int(input())
# if len(lst)==k:
#     perm=list(permutations(lst))
#     print(perm)
# t=1
# for i in range(t):
#     n=4
#     k=list(map(int,(input().split() [:n])))
#     perm=list(permutations(k))
#     print(perm)
#     for i in perm:
#         for j in i:
#             if

# import math
# n=int(input())
# l=[]
# c=0
# for i in range(n):
#     l.append(list(map(str,input().split())))
# for j in range(n):
#     for k in range(n):
#         if l[j][k]=='D':
#             c+=1
#
# print(math.floor(math.sqrt(c)))
# lst=[]
# for j in range(1,int(input("no of table:"))+1):
#     print(f"table of {j}")
#     for i in   range(1,11):
#         (n)=i*j
#
#         print(n)
#     print("\n")
# num="premmishra"
# lst=[1,2,3,4,5,6,7]
# for i in range(len(lst),0,-1):
#
#     if i%2==0:

#PAID TCS CODE////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#PROBLEM--1yes
#[1,2,1,3,2,5,3,7,5,11,8,13,13,17]____[1,1,2,3,5,8,13],[2,3,5,7,11,13,17]---[2,5,11,17][3,7,13]
'''n=int(input())
a=5
lst=[2,5]
b=3
lst1=[3]
c=1
lst2=[1,1]
lst3=[]
lst4=[]
for i in range(1,n//3-1):
    a=a+6
    lst.append(a)
print(lst)
for i in range(1,n//3):
    b=b+i*2+2
    lst1.append(b)
print(lst1)
for i in range(len(lst)):
    lst3.append(lst[i])
    lst3.append(lst1[i])
print(lst3)
for i in range(1,n//2+1):
    c=lst2[-2]+lst2[-1]
    lst2.append(c)
print(lst2)
for i in range(len(lst3)):
    lst4.append(lst2[i])
    lst4.append(lst3[i])
print(lst4)
print(lst4[n-1])'''

#PROBLEM--2no
#[10,14,27,33,35,19,42,44]
# [10,14,19,17,33,35,42,44]
'''lst1=[]
lst=[27,14,10,33,35,19,42,44]
lst1.append(min(lst))
lst.remove(min(lst))
lst1.extend(lst)
print(lst1)
print(lst)
b=lst.index(min(lst))

lst[0],lst[b]=lst[b],lst[0]
print(lst)'''
#PROBLEM--3yes
#COUNT REPETE NUMBER
'''lst=[1,2,2,3,4,1,2,3,4,3,3,3,4]
n=int(input())
count=0
for i in lst:
    if i==n:
        count+=1
print(count)'''
#PROBLEM--4 no
'''x="aggtabb"
x=list(x)
y="gxtxayb"
y=list(y)
lst=[]
for i in range(len(x)):
    if x[i] in y:
        print(x[i])
        lst.append(x[i])
        y1 = y.index(x[i])
        print(y1)
        y.remove(y[y1])
        x.remove(x[i])
        print(x)
        print(y)
        print(lst)
print(lst)'''

#5SUBSTRING yes
'''str="prem"
a=""
for i in range(len(str)):
    for j in range(i+1 ,len(str)+1):
        print(str[i:j])'''
#6 PROBLEM 6--PYTHAGORASyes
'''n=int(input())
lst=[]
lst1=[]
lst2=[]
for i in range(n+1):
    k=i*i
    for j in range(1,n):

        for p in range(1,n):
            add=j**2+p**2
            if add == k:
                lst.append(j)
                lst1.append(p)
                lst2.append(i)

for i in range(len(lst)):
    if i%2==0:
        print(lst[i],lst1[i],lst2[i])'''
#ARMSTRONG NUMBER--7yes
'''n=input()
lst=list(n)
order=len(lst)
num=0
for i in range(len(lst)):
    num=num+int(lst[i])**order
print(num)
if num==int(n):
    print("armstrong")
else:
    print("simple num")'''

#8-COUNT NUM yes
'''lst=[1,2,3,4,1,2,3,2,2,5,6]
lst1=set(lst)
lst1=list(lst1)
for i in range(len(lst1)):
    print(lst1[i],lst.count(lst1[i]))'''
#9--DECIMAL TO OCTAL yes
'''n=16
p=oct(n)
print(p[2:])'''
#10 BINARY TO OCTALyes

'''num=111
num=str(num)
lst=list(num)
lst=lst[::-1]
mul=0
for i in range(len(lst)):
    mul=mul+int(lst[i])*(2**i)

octal_num=oct(mul)
print(octal_num[2:])'''
#11LEAP YERA yes
'''year=int(input())
if year%4==0:
    if year%400==0:
        print("LEAP YEAR")
    else:
        print("only year")
else:
    print("only year")'''

#12  PRIME NUMBER yes
'''num=int(input())
for i in range(2,num//2+1):
    if num%i==0:
        print("SIMPLE NUM")
        break
else:
    print("PRIME NUMBER")'''
#13 REVERSE NUM yes
'''num=67892
lst=[]
for i in range(1,(num)+1):
    if num>=1:
        reminder = num % 10
        num=int(num/10)
        print(reminder,end="")'''
#OR
'''print(num[::-1])'''
#14 REVERSE A STRING WITHOUT USE ANY INBUILT FUN yes
#15 GCD  yes
'''a,b,c=map(int,(input().split()))

for i in range(a,1,-1):
    if a%i==0 and b%i==0 and c%i==0:
        print(i)
        break'''
#16 SECOND MAX NUMBER yes
'''lst=[1,2,3,7,8,4,2,1,8,8]
lst.sort()
delete=lst.pop()
for i in range(len(lst)):
    if delete==lst[-1]:
        lst.pop()
print(lst[-1])'''

#17SUM OF PRIME NUM yes
'''n1=int(input())
n2=int(input())
lst=[]
lst2=[]
for num in range(n1,n2+1):
    for i in range(2,num):
        if num%i==0:
            lst2.append(i)
            break
    else:
        lst.append(num)

print(sum(lst))'''
#18--TWO NUMBER SUM IN BINARY yes
'''a,b=map(int,input().split())
sum=a+b
result=bin(sum)
print(result)'''


#19,21- STR TO INT yes
'''num=input()
print(int(num))'''

#20--file question no
#19,21 are same
#22--NUM TO BINARY CONVERSION yes
'''num=int(input())
binary_rep=bin(num)
print(binary_rep[2::])'''
#23-- multiply a num by 8 without using * operater yes
'''num=int(input())
sum=0
for i in range(8):
    sum=sum+num
print(sum)'''

# 24--EFFICIENT MULTIPLY BY 31 yes
'''num=int(input())
print((num<<3))'''
#25--SWAPPING yes
'''a,b=map(int,input().split())
c=a+b
a=c-a
b=c-b
print(a,b)'''
#26 ZEROS TRANSFER TO LAST POSITION
'''arr=[1,0,3,4,0,0,0,2,3,999,0,0,0,0]
for i in range(len(arr)):
    if arr[i]==0:
        arr.remove(arr[i])
        arr.append(0)
print(arr)'''

#27-- FIND PATTERN IN STRING yes
'''str=input()
pattern=input()
if pattern in str:
    print("true")
else:
    print("false")'''
#28--LENNTH OF STRING WITHOUT USING FUNCTION yes
'''str="premmishra"
length=0
for i in str:
    length+=1

print(length)'''

#29 Krh LARGEST NUMBER
'''arr=[10,7,6,3,2,4]
k=int(input())
arr.sort()
print(arr[k-1])'''

## 31,32-- DIVIDE SENTENCE IN STRING MAY BE YES
'''str="prem kumar mishra"
print(str.split())'''

#33 -- ONLY ONE SPACE IN WORDS
'''str="prem   kumar  mishra                vijay kumar       mishra  "
str=str.split()
sum=""
for i in str:
    sum=sum+" "+i
print(sum.strip())'''

#34--
#36--DELETE ALL VOWELS IN STRING yes
'''str=input()
lst=["a","i","e","o","u","A","E","I","O","U"]
for i in range(len(lst)):
    if lst[i] in str:
        ind_ex=str.index(lst[i])
        
        str=str.replace(str[ind_ex],"")
print(str)'''
#38-- SUM OF INTEGERyes
'''arr=[1,2,3,4,1,6]
sum=0
for i in arr:
    sum+=i
print(sum)'''

#40 SUMMING FIVE INTEGERS no



# for i in range(len(num)):
#     for j in range(len(num)-1):
#         add=num[i]+num[j+1]
#         print(add)

#43 BIRDS SIGHTING

