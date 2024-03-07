import random
computer_choice=random.choice(['rock','paper','scissor'])
user_choice=input("rock,paper or scissor?\n")
print('This was the computer choice'+' '+computer_choice)
if computer_choice==user_choice:
    print('TIE')
elif user_choice=='rock' and computer_choice=='scissor':
    print('You win')
elif user_choice=='scissor' and computer_choice=='paper':
    print('You win')
elif user_choice=='paper' and computer_choice=='rock':
    print('You win')
else:
    print('Better luck next time.')