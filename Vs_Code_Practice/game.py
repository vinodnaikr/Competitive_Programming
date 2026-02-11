def game():
    inp=input("Enter your score: ")
    return int(inp)

# 1. Call the game function to get the current score
score = game()

# 2. Read the previous high score from the file
try:
    with open("Hi-score.txt", "r") as f:
        hi_score_str = f.read()
        
    # Check if the file is blank
    if hi_score_str == "":
        hi_score = 0
    else:
        hi_score = int(hi_score_str)
except FileNotFoundError:
    # If the file doesn't exist, treat the high score as 0
    hi_score = 0

# 3. Compare and update the file if the current score is higher
print(f"Your Score: {score}")
print(f"Previous High Score: {hi_score}")

if score > hi_score:
    print("New High Score Achieved!")
    with open("Hi-score.txt", "w") as f:
        f.write(str(score))
else:
    print("Better luck next time!")