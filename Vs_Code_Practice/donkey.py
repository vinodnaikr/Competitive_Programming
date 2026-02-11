import os
filename="donkey.txt"

censored_words=["donkey","badword","stubborn","animal"]

with open(filename,"w") as f:
    f.write("donkey is a great animal\n")
    f.write("donkeys are known for their strength\n")
    f.write(" a donkey has vaer long neck\n")

with open(filename,"r") as f:
    data=f.read()

for word in censored_words:
    data=data.replace(word,"#####")

with open(filename,"w") as f:
    f.write(data)

print("updated content")
print(data)





