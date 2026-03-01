import os
filename='log.txt'
found=False
line_number=0

try:
    with open(filename,"w") as f:
        f.write("python is a very easy language")
    
    with open(filename,"r") as f:
        data=f.read()
            
        if "python" in data:
                print(f"Match found on {line_number}:{data.strip()}")
                found = True
    if not found:
     print("The word python is not found in the log.txt")
except FileNotFoundError:
  print("File not found please check the file name")