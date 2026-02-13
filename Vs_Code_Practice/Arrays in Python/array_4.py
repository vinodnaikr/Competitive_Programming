from array import array

#accept marks as a string
n=int(input("Enter the number of subjects:"))

i=0
marks=array("i",[])
while i<n:
    marks.append(int(input("Enter marks:")))
    i=i+1

sum=0
for i in marks:
    print(i,end=" ")
    sum=sum+i

print("Total marks:",sum)

n=len(marks)
average=sum/n
print("Average marks:",average)

percentage=(sum/(n*100))*100
print("Percentage:",percentage)

