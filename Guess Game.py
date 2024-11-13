# GUESSING GAME:

answer = int(input("Enter the number: "))
no_of_guess = 3
count_guess=0
for i in range(no_of_guess):
    guess = int(input("Enter the guess: "))
    if guess == answer:
        print("You Win")
        break
    elif count_guess<2:
        count_guess+=1
        print("Try again")
else:
    print("You lost")
