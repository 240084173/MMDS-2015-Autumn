import numpy as np

def iteraction (N, bet, M, n_iter=50, sumPageRanks=1):
    A = bet * M + (1 - bet) * 1/N * np.ones((N,N))
    r_i = sumPageRanks/N * np.ones(N)
    print('Matrix A \\n',A,'\\n')
    eps = 0.0001
    for i in range(n_iter):
        r_i = np.dot(A,r_i.T)
    
    return r_i


if __name__ == "__main__":
    ###########################################
    #question 1
    N = 3  # number of nodes"
    bet = 0.7
    M = np.array([[0,0,0],
                 [1/2,0,0],
                 [1/2,1,1]])
    r = iteraction(N,bet,M,n_iter=10, sumPageRanks=3)
    print('Rank vector r:', r)
    ###########################################

    ###########################################
    #question 2
    N=3
    bet = 0.85
    M = np.array([[0,0,1],[0.5,0,0],[0.5,1,0]])
    r = iteraction(N, bet, M, 10, 1) 
    print(r)
    ###########################################
    
    ###########################################
    #question 3
    N=3
    bet = 1
    M = np.array([[0,0,1],[0.5,0,0],[0.5,1,0]])
    r = iteraction(N, bet, M, 4, 3) 
    print(r)
    ###########################################
