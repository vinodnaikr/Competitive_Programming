#sorting an array using bubblesort technique

from array import array

#create an empty array to store integers
x=array("i",[])

#store elements into the array x
n=int(input("Enter thr number of elements:"))
for i in range(n):
    print("Enter Element:",end=" ")
    x.append(int(input()))

print("Original array:",x)

#bubble sort
flag=False
for i in range(n-1):
    for j in range(n-1-i):
        if x[j]>x[j+1]:
            t=x[j]
            x[j]=x[j+1]
            x[j+1]=t
            flag=True
    if flag==False:
        break
    else:
        flag=False

print("sorted array:",x)