#coin flip simulator


import random

total_heads = 0
total_tails = 0
count = 0

while count < 100:
    coin = random.randint(1, 2) #50 50 probability

    if coin == 1:
        print("Heads!\n")
        total_heads += 1   #counts number of times heads is flipped
        count += 1  #counts the total number of coin flips to figure out when to break the loop

    elif coin == 2:
        print("Tails!\n")
        total_tails += 1  #counts total number of tails
        count += 1

print("Ok you flipped heads", total_heads, " times")
print("And you flipped tails", total_tails," times")
