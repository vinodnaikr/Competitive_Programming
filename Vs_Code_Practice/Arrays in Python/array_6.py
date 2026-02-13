#searching an array for an element
from array import array

#create an empty  array to store integers
x=array("i",[])
print("How may elements?",end=" ")
n=int(input())
for i in range(n):
    print("Enter elment:",end=" ")
    x.append(int(input()))

print("Original Elements are:",x)
print("Enter the element to search:",end=" ")
s=int(input())

#linear search or sequential search
found=False
for i in range(n):
    if s==x[i]:
        found=True
        print(f"Element {s} found at position {i+1}")
    if found==False:
        print(f"Element {s} not found in the array")
