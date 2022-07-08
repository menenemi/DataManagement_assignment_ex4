import random
import time

user = input("Who are you? \n> ")
print(f'Hello, {user}!', end="\n\n")

print("Tossing a coin...")
time.sleep(1)
headcount = 0
tailcount = 0

for i in range(1,4):
    n = random.randint(0, 1)
    if n == 0:
        print(f'Round {i}: Heads')
        headcount += 1
    else:
        print(f'Round {i}: Tails')
        tailcount += 1
    time.sleep(1)

print(f'Heads: {headcount}, Tails: {tailcount}')
if headcount > tailcount:
    print(f'{user} won!')
else:
    print(f'{user} lost.')