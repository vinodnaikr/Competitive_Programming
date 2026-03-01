import random

n=random.randint(1,100)
a=-1
guesses=0

print('-----Welcome to the project Guess Number Game!')

while(a!=n):
    guesses+=1
    a=int(input("Guess the Number:"))

    if(a>n):
        print("Lower Number Please")
    elif(a<n):
        print("Higher Number Please")

print(f"BINGO! You Guessed the Number{n} correctly in {guesses} attempts")