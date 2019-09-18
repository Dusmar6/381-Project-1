import random

my_word = 66

m = 70000
k = 7
N = 1000 # number of trials

def run(a, b, c):
    successes = 0
    for num in range(a):
        for k in range(b*c):
            if my_word == random.randint(0,26**4):
                successes+=1
                break
    return successes/N
      
p1 = run(N, 1, m)
print(p1)

p2 = run(N, k, m)
print(p2)

p3 = 0
i = 0
while p3 <= 0.5:
    i+=1
    current = i*m
    p3 = run(N, i, m)
    
print(current)

    
    



    
        



