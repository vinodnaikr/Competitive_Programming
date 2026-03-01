# mathematical operations on arrays
#import all from numpy module
from numpy import*

#create a numpy array using array() function
arr=array([10,20,30.5,-40])
print("Original array:",arr)

#doing arthimetic operations on array
print("After adding 5",arr+5)
print("After subtracting 5",arr-5)
print("After multiplying with 5",arr*5)
print("After didviding with 5",arr/5)
print("After modulud with 5",arr%5)

#using math functions on array
print("sine values:",sin(arr))
print("cos values:",cos(arr))
print("tan values:",tan(arr))
print("Biggest element",max(arr))
print("Smallest element",min(arr))
print("Sum of all elements",sum(arr))
print("Average of alla elements",mean(arr))
print("Median of all the elements",median(arr))
