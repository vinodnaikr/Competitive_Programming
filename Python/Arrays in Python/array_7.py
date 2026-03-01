#searching for an element in an array using indexing method
from array import array 

#create an empty array to store integers
x=array("i",[])

#store elements into array
print("How many elements :\n")
n=int(input())
for i in range(n):
    print("Enter element:\n")
    x.append(int(input()))
print("Original array:",x)
print("Enter element to search:\n")
s=int(input())

#index method gives the location of the element in an array
try:
    pos=x.index(s)
    print("Found at ;position ",pos+1)
except ValueError:
    print("Element not found")
