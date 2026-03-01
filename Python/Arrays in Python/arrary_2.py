from array import array
x=array("i",[10,20,30,40,50])
n=len(x)
print("the array X elements are:")

i=0
while i<n:
    print(x[i],end=" ")
    i=i+1

y=x[1:4]
print(y)

y=x[0:2]
print(y)

y=x[:4]
print(y)

y=x[-4:-1]
print(y)

y=x[0:7:2]
print(y)

