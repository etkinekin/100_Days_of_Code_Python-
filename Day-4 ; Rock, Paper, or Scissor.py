rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random

ch = input('Press 0 for Rock, 1 for Paper or 2 Scissor ?')
ch = int(ch)
if ch == 0 :
    print(rock)
elif ch == 1 :
    print(paper)
elif ch == 2 :
    print(scissors)
else :
    print('You entered wrong number.')

ch1 = random.randint(0,2)

if ch1 == 0 :
    print(rock)
elif ch1 == 1 :
    print(paper)
else :
    print(scissors)""


if ch1 == 2 and ch == 1 :
    print('Computer won!')
elif ch1 == 2 and ch == 0 :
    print('Player won!')
elif ch1 == 1 and ch == 2 :
    print('Player won!')
elif ch1 == 1 and ch == 0 :
    print('Computer won!')
elif ch1 == 0 and ch == 1 :
    print('Player won!')
elif ch1 == 0 and ch == 2 :
    print('Computer won!')
else :
    print('It is a draw!')