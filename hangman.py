import random

wrong = 0
rem_words = 0
correct_guess = ''
with open('sowpods.txt') as f:
    words = list(f)
rword = random.choice(words).strip()
print('Welcome to handman!')
print('-' * len(rword))

while wrong < 7 or rem_words == 0:
    guess = input("Guess your letter:")
    guess = guess.strip()
    if guess.lower() in rword.lower():
        correct_guess = correct_guess + guess
        rem_words = 0
        for char in rword.lower():
            if char in correct_guess.lower():
                print(char,end="")
            else:
                print('-',end="")
                rem_words += 1
        print("\n")
    else:
        print("Incorrect!")
        rem_words = 0
        for char in rword.lower():
            if char in correct_guess.lower():
                print(char,end="")
            else:
                print('-',end="")
                rem_words += 1
        print("\n")
        wrong += 1

if rem_words == 0:
    print("You have won!")
else:
    print("The word is ",rword)







