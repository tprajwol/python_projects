import random
roll=random.randint(1,6)
#print('The computer roll'+' '+str(roll))
a=int(input("Guess a number?\n"))
if roll==a:
    print('Correct guess'+' '+'the number is'+' '+str(a))
else:
    print('Wrong Guess'+' '+'rolled number is'+' '+str(roll))