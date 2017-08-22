import numpy as np
import matplotlib.pyplot as plt
from scipy.misc import comb

m = 64
k = 4
def eval_point(n):
    if n <m:
        return(0)
    else:
        return((k-1)/m *comb(m,k)/comb(n, k))

def posterior(n):
    list_eval_points = []
    for m in n:
        eval = eval_point(m)
        list_eval_points.append(eval)
    out = np.array(list_eval_points)
    return(out)    

def prior(n):
    diff = n.max() - n.min()
    out = np.repeat(1/diff, len(n))
    return(out)

def posterior_mean(M=m, K=k):
    numer = (M-1)*(K-1)
    denom = K-2
    return(numer/denom)
    
def posterior_stdev(M=m, K=k):
    numer = (m-1)*(k-1)*(m-k+1)
    denom = (k-3)*(k-2)**2
    var = numer/denom
    std_dev = np.sqrt(var)
    return(std_dev)
    
N = np.array(range(1,201))

plt.plot(N,prior(N))
plt.xlabel("N")
plt.ylabel(r'$\pi(N)$')
plt.title("Prior Distribtuion")
plt.show()

fig, ax = plt.subplots()
ax.stem(N, prior(N))
plt.show()

plt.plot(N,posterior(N))
plt.xlabel("N")
plt.ylabel(r'$\pi(N | x)$')
plt.title("Posterior Distribtuion")
plt.show()


fig, ax = plt.subplots()
ax.stem(N, posterior(N))
plt.xlabel("N")
plt.ylabel(r'$\pi(N | x)$')
plt.title("Posterior Distribtuion")
plt.show()


