import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import beta

#Define hyperparameters
prior_alpha, prior_beta = 1,1


xgrid = np.arange(0,1,0.01)
#Evaluate the prior over the grid
prior_of_xgrid = beta.pdf(xgrid, a = prior_alpha, b = prior_beta)


#Plot the prior distribution
plt.plot(xgrid, prior_of_xgrid)
plt.xlabel(r'$\theta$')
plt.ylabel(r'$\pi(\theta)$')
plt.title("Prior Distribtuion")
plt.show()


#Define parameter and sample size
theta , n = 0.5, 10

#Generate Data
x = np.random.binomial(1, theta, n)
y = x.sum()


#Define the Likelihood
def Lhood_bern(theta):
    out = theta**y *(1-theta)**(n - y)
    return(out)


#Plot the Likelihood
plt.plot(xgrid, Lhood_bern(xgrid))
plt.axvline(x.mean(), color='orange')
plt.xlabel(r'$\theta$')
plt.ylabel(r'$L(\theta | x)$')
plt.title("Likelihood")
plt.show() 
    
#Define Posterior hyperparameters
posterior_alpha = prior_alpha + x.sum()
posterior_beta = prior_beta + n - x.sum()

#Evaluate the postior over the grid
posterior_of_xgrid = beta.pdf(xgrid, a = posterior_alpha, b = posterior_beta)
#Plot the posterior
plt.plot(xgrid, posterior_of_xgrid)
plt.xlabel(r'$\theta$')
plt.ylabel(r'$\pi(\theta | x)$')
plt.title("Posterior Distribtuion")
plt.show()

