try:
    with open("log.txt","r") as f:
        data_1=f.read()
    
    with open("log_copy.txt","r") as f:
        data_2=f.read()

    if data_1==data_2:
        print(f"files{"log.txt"} and {"log_copy.txt"} are same")
    else:
        print(f"files{"log.txt"} and {"log_copy.txt"} are not same")
except FileNotFoundError:
    print(f"Please check the files")