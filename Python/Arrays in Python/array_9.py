#creating an array using linespace()
from numpy import*

#divide 0 to 10 into 5 parts ans take those points in the array
a=linspace(0,10,5)
print("a=",a)

#creating an array using logspace()
#divide the range : 10 power 1 to 10 power 4 into 5 equal parts
#take those points in the array

a=logspace(1,4,5)
n=len(a)
for i in range(n):
    print("%.1f"%a[i],end=" ")

#creating an array using arange() function
a=arange(2,11,2)
print(a)

#creating arrays using zeros() and ones()
a=zeros(5,int)
print(a)
b=ones(5)
print(b)