from array import array
a=array("d",[1.5,2.5,3.5,4.5])

arr2=array(a.typecode,(a*3 for a in a))

print("the array elements are:")

for i in arr2:
    print(i,end=" ")