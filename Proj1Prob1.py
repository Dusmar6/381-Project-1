import numpy as np
import matplotlib.pyplot as plt 


def nSidedDie(p):
    n = len(p)
    cs = np.cumsum(p)
    cp = np.append(0,cs)
    r = np.random.rand()
    for k in range(0,n):
        if r>cp[k] and r<=cp[k+1]:
            d=k+1   
    return d


def plot(results, p, N):
    b = range(1, len(p)+2)
    sb = np.size(b)
    h1, bin_edges = np.histogram(results,bins = b)
    b1 = bin_edges[0:sb-1]
    plt.close('all')
    prob = h1/N
    plt.stem(b1, prob)
    plt.title('PMF for an unfair N-sided die', fontsize = 14, fontweight = 'bold')
    plt.xlabel('Number on the face of the die',fontsize=14)
    plt.ylabel('Probability',fontsize=14,) 
    plt.xticks(b1) 


def main():
    
    N = 10000 #rolls
        
    p = np.array ([0.10,  0.15,  0.20,  0.35, 0.20])
    
    results = []
    for num in range(N):
        results.append(nSidedDie(p))
    
    plot(results, p, N)
    

main()