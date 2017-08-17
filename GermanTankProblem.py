import numpy as np
import matplotlib.pyplot as plt
from scipy.misc import comb

m = 60
k = 3
def eval_point(n):
    if n <m:
        return(0)
    else:
        return((k-1)/k *comb(m-1,k-1)/comb(n, k))

def posterior(N):
    list_eval_points = []
    for n in N:
        eval = eval_point(n)
        list_eval_points.append(eval)
    out = np.array(list_eval_points)
    return(out)    

def prior(x):
    diff = x.max() - x.min()
    out = np.repeat(1/diff, len(x))
    return(out)
    
x = np.array(range(1,501))

plt.plot(x,prior(x))
plt.xlabel("N")
plt.ylabel(r'$\pi(N)$')
plt.title("Prior Distribtuion")
plt.show()


plt.plot(x,posterior(x))
plt.xlabel("N")
plt.ylabel(r'$\pi(N | x)$')
plt.title("Posterior Distribtuion")
plt.show()


