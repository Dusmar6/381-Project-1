import random

#my 'word'
my_word = 66

#variables given on beachboard
m = 70000
k = 7

N = 1000 # number of trials

def run(a, b, c):
    successes = 0 #counts the number of successful guesses
    for num in range(a): #number of times to run the experiment (1000)
        for k in range(b*c): #number of 'words' in each list to test
            if my_word == random.randint(0,26**4): #checks if my 'word' matches a word on the list
                successes+=1 
                break
    return successes/N #calculates the probability that the word is on a list of m words
      
p1 = run(N, 1, m) #runs the experiment with m words on the list
print(p1)

p2 = run(N, k, m) #runs the experiment with k*m words on the list
print(p2)

p3 = 0
i = 0
while p3 <= 0.5: #runs the experiment repeatedly, adding words to m until the probability that the word is on the list is at least 0.5
    i+=1
    current = i*m
    p3 = run(N, i, m)
    
print(current) #pirnts approximately the number of words on the list needed

    
    



    
        



