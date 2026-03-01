import os

# 1. Create a folder named 'tables' if it doesn't already exist
if not os.path.exists("tables"):
    os.makedirs("tables")

# 2. Loop through numbers 2 to 20
for i in range(2, 21):
    # Create a unique filename for each table
    filename = f"tables/Table_of_{i}.txt"
    
    with open(filename, "w") as f:
        # 3. Generate the multiplication rows (1 to 10)
        for j in range(1, 11):
            line = f"{i} x {j} = {i*j}\n"
            f.write(line)
            
print("Success! Check the 'tables' folder for your files.")