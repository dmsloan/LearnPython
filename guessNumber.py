low = 0
high = 100
guess = int((high-low)/2)
ans = ""

def guessNumber(ans):
    global guess
    global low
    global high
    if ans == "l":
        low = guess
        guess = int((high+low)/2)
    elif ans == "h":
        high = guess
        guess = int((high+low)/2)
    elif ans == "c":
        print("Game over. Your secret number was: ", guess)
    else:
        print("Sorry, I did not understand your input.")

    

print("Please think of a number between 0 and 100!")

while ans != "c":
    print("Is your secret number ", guess, "?")
    ans= input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    guessNumber(ans)