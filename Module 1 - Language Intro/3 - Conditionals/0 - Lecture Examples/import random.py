import random
import string 
# Generates one random letter (a-z, A-Z)
random_letter = random.choice(string.ascii_letters)
print(random_letter) 
if random_letter.islower():
    print("This letter wouldn't work at the start of the sentence.")
    if random_letter == 'a':
        print("This letter is used for apple'.")
    elif random_letter == 'b':
        print("This letter is used for banana'.")
    else:
        print(" you didn't get my first two, and they don't work at the start of a sentence :(")
        