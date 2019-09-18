import numpy as np



c = 100 #number of coins flipped
succ = 50 #number of heads deemed a 'success'
N = 100000 #number of repeats

successes = 0
for i in range(N):
    headcount = 0
    for k in range(c):
        flip = np.random.randint(0,2) #0=heads, 1=tails
        if flip == 0:
            headcount+=1
    if headcount == succ:
        successes+=1

print("The probability of getting exactly ", succ, " heads is: ", successes/N)
    
    
