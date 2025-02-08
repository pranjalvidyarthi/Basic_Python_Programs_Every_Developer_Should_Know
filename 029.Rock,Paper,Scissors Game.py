# Rock paper scissor game using python
import random
choices = ['rock','paper', 'scissors']
user = input('Choose Rock,paper or Scissors: ').lower()
computer = random.choice(choices)

print(f'Computer choice {computer}')
if user == computer:
    print("It's a tie!")
elif (user == 'rock' and computer == 'scissors') or \
     (user == 'paper' and computer == 'rock') or \
     (user =='scissors' and computer =='paper'):
        print('You win!')

else:
      print('You loose!')