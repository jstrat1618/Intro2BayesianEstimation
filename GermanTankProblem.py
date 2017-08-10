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
        
        
    
x = np.array(range(1,500))
y = posterior(x)

plt.plot(x,y)
plt.xlabel("N")
plt.ylabel(r'$\pi(N | x)$')
plt.title("Posterior Distribtuion")
plt.show()

