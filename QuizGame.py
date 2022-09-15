print(" Welcome To My Quiz Game \n\r Interesting Game to Play")
Player = input(" Do you want to play the game? \n\rPlease Enter \'Yes\' or \'No\' \n\r")
if Player.casefold() != 'yes':
    print("Good Bye")
    quit()

name_player = input("Please Enter Your Name: ")

print("Let's Start the Game :) ", name_player)

score = 0

answer = input(' What is CPU stands for? \n\r ')
if answer.lower() == 'central processing unit':
    print("Correct")
    score += 1
else:
    print('Wrong')

answer = input(' What is GPU stands for? \n ')
if answer.lower() == 'graphical processing unit':
    print("Correct")
    score += 1
else:
    print('Wrong')

answer = input(' What is RAM stands for? \n ')
if answer.lower() == 'random access memory':
    print("Correct")
    score += 1
else:
    print('Wrong')

answer = input(' What is ROM stands for? \n ')
if answer.lower() == 'read only memory':
    print("Correct")
    score += 1
else:
    print('Wrong')

answer = input(' Mouse is an input device or output device? \n ')
if answer.lower() == 'input device':
    print("Correct")
    score += 1
else:
    print('Wrong')

print("You got the " + str(score) + " correct answers")
print("You got the " + str((score / 5) * 100) + " correct answers")