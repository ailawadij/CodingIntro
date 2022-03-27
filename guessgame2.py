word = "yo"
guess = ""
guess_limit = int(input("Enter the maximum number of guesses: "))
guess_number = 0
out_of_guesses = False
while guess != word and not(out_of_guesses):
    if guess_number < guess_limit:
        guess = input("Enter guess: ")
        guess_number += 1
    else:
        out_of_guesses = True
if out_of_guesses:
    print("You suck!!")
else:
    print("Winnr!")


#CRUD
# Creates Word
# Reading yo
# Updating guesses
# Not deleting
