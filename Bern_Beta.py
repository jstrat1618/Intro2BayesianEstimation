import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import beta

#Define parametere and sample size
theta , n = 0.5, 10

#Generate Data
x = np.random.binomial(1, theta, n)

#Define hyperparameters
prior_alpha, prior_beta = 1,1


#Define Posterior hyperparameters
posterior_alpha = prior_alpha + x.sum()
posterior_beta = prior_beta + n - x.sum()

xgrid = np.arange(-0.1,1.1,0.01)
#Evaluate the prior over the grid
prior_of_xgrid = beta.pdf(xgrid, a = prior_alpha, b = prior_beta)

#Plot the prior distribution
plt.plot(xgrid, prior_of_xgrid)
plt.xlabel(r'$\theta$')
plt.ylabel(r'$\pi(\theta)$')
plt.title("Prior Distribtuion")
plt.show()

#Evaluate the postior over the grid
posterior_of_xgrid = beta.pdf(xgrid, a = posterior_alpha, b = posterior_beta)
#Plot the posterior
plt.plot(xgrid, posterior_of_xgrid)
plt.xlabel(r'$\theta$')
plt.ylabel(r'$\pi(\theta | x)$')
plt.title("Posterior Distribtuion")
plt.show()

