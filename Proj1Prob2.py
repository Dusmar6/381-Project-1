import numpy as np
import matplotlib.pyplot as plt 

def plot(results, p, N): #function to plot the results
    b = range(1, len(p)+2)
    sb = np.size(b)
    h1, bin_edges = np.histogram(results,bins = b)
    b1 = bin_edges[0:sb-1]
    plt.close('all')
    prob = h1/N
    plt.stem(b1, prob)
    plt.title('PMF for rolls needed to get a sum of 7 between two fair die', fontsize = 14, fontweight = 'bold')
    plt.xlabel('Number of rolls',fontsize=14)
    plt.ylabel('Probability',fontsize=14,) 
    plt.xticks(b1) 
    
    
def main():
    rolls = 100000 #number of times to repeat the experiment
    
    successes = []
    for num in range(rolls): # runs the experiment N amount of times
        sum = 0
        count = 0
        while sum !=7: #checks if the dice sum is 7
            sum = np.random.randint(1,7) + np.random.randint(1,7) #rolls the die and checks the sum
            count+=1 #counts how many rolls
        successes.append(count) # records the number of rolls
    y=[]
    for num in range(30):
        y.append(num)
        
    plot(successes, y, rolls ) # plots the results
    
    
main()