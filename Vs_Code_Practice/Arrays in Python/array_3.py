from array import array

arr=array("i",[10,20,30,40,50])
print("Original array:",arr)

#append 30 to the array arr
arr.append(30)
arr.append(60)
print("after appending 30 and 60:",arr)

#append 99 at the position number 1 in arr
arr.insert(1,99)
print("after inserting 99 at position 1:",arr)

#remove element from arr
arr.remove(20)
print("after removing 20 from arr:",arr)

#remove last elemnt using pop
n=arr.pop()
print("after popping last element:",arr)
print("popped element is:",n)

#finding position of element using index() method
n=arr.index(30)
print("the first occurence of element  30 ia at:",n)

#convert an array into list using list method
l=arr.tolist()
print("List",l)
print("Array:",arr)