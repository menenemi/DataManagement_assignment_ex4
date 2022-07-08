import random
import time

print("Tossing a coin...")
time.sleep(1)
headcount = 0
tailcount = 0

for i in range(0,3):
    n = random.randint(0, 1)
    if n == 0:
        print(f'Round {i}: Heads')
        headcount += 1
    else:
        print(f'Round {i}: Tails')
        tailcount += 1
    time.sleep(1)

print(f'Heads: {headcount}, Tails: {tailcount}')