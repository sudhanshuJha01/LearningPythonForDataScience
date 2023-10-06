import random
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

num=int(input("What you want to choose, choose 0 for rock choose 1 for Paper Choose 2 for Scissors ==>"))

print("Your choice")

if num==0:
    print(rock)
elif num==1:
    print(paper)
else:
    print(scissors)

print("Computer choice")

comp_choice=random.randint(0,2)

if comp_choice==0:
    print(rock)
elif comp_choice==1:
    print(paper)
else:
    print(scissors)

if num==comp_choice:
    print("You won")
else:
    print("You lost")
