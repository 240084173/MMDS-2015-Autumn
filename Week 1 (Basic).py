import numpy as np
from collections import defaultdict

#question 1-3
def iteraction (N, bet, M, n_iter=50, sumPageRanks=1):
    A = bet * M + (1 - bet) * 1/N * np.ones((N,N))
    r_i = sumPageRanks/N * np.ones(N)
    print "Matrix A \n",A
    eps = 0.0001
    for i in range(n_iter):
        r_i = np.dot(A,r_i.T)
    
    return r_i
    
#question4
input_list = [15,21,24,30,49] 

def primes(n):
    divisors = [d for d in range(2,n/2+1) if n % d ==0 ]
    return [ d for d in divisors if all (d % od !=0 for od in divisors if od !=d)]
    

#MAP
def prime_divisors(i):
    result = []
    divisors = [d for d in range(2,i/2+1) if i%d ==0]
    #print divisors
    
    def isprime(d):
        return all(d %od !=0 for od in divisors if od!=d) #not equal to other divisors
    
    for d in divisors:
        if isprime(d):
            result.append((d,i))
    
    print result
    return result

#reduce
def _reduce(map_list):
    result = defaultdict(list)
    for _list in map_list:
        for k,v in _list:
            result[k].append(v)
    
    #out_reduce = {k:sum(v) for k in result.keys() for v in result.values()}        
    out_reduce = {}
    for key in result.keys():
        out_reduce[key] = sum(result[key])
        
    return out_reduce

if __name__ == "__main__":
    ###########################################
    #question 1
    print ("This is the solution to question 1")
    N = 3  # number of nodes"
    bet = 0.7
    M = np.array([[0,0,0],
                 [0.5,0,0],
                 [0.5,1,1]])
    r = iteraction(N,bet,M,n_iter=10, sumPageRanks=3)
    print 'Rank vector r:\n', r
    ###########################################

    ###########################################
    #question 2
    print ("\nThis is the solution to question 2")
    N=3
    bet = 0.85
    M = np.array([[0,0,1],[0.5,0,0],[0.5,1,0]])
    r = iteraction(N, bet, M, 50, 100) 
    print 'Rank vector r:\n', r
    ###########################################
    
    ###########################################
    #question 3
    print ("\nThis is the solution to question 3")
    N=3
    bet = 1
    M = np.array([[0,0,1],[0.5,0,0],[0.5,1,0]])
    r = iteraction(N, bet, M, 4, 3) 
    print 'Rank vector r:\n', r
    ###########################################
    
    ###########################################
    #question 4
    print ("\nThis is the solution to question 4")
    output_map_list = list(map(prime_divisors, input_list))
    print(_reduce(output_map_list))
