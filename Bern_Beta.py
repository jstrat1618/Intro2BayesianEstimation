import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import beta

#Define hyperparameters
prior_alpha, prior_beta = 1,1


xgrid = np.arange(-0.02,1.02,0.01)
#Evaluate the prior over the grid
prior_of_xgrid = beta.pdf(xgrid, a = prior_alpha, b = prior_beta)


#Plot the prior distribution
plt.plot(xgrid, prior_of_xgrid)
plt.xlabel(r'$\theta$')
plt.ylabel(r'$\pi(\theta)$')
plt.title("Prior Distribtuion")
plt.show()


#Define parameter and sample size
theta , n = 0.75, 100

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

#Create functions to compute posterior mean and standard deviation
def beta_mean(a, b):
    return(a/(a + b))

def beta_stdv(a, b):
    denom = (a + b)**2 *(a + b + 1)
    vrnc = a*b/denom
    return(np.sqrt(vrnc))

post_mean = beta_mean(posterior_alpha, posterior_beta)
post_stdv = beta_stdv(posterior_alpha, posterior_beta)

#Compute Credible set
level = 0.05
lower, upper = beta.ppf(level / 2, a=posterior_alpha, b=posterior_beta), beta.ppf(1 - level / 2, a=posterior_alpha, b=posterior_beta)

#Evaluate the postior over the grid
posterior_of_xgrid = beta.pdf(xgrid, a = posterior_alpha, b = posterior_beta)
#Plot the posterior
plt.plot(xgrid, posterior_of_xgrid)
plt.axvline(x=post_mean, color='orange', linestyle='--')
plt.xlabel(r'$\theta$')
plt.ylabel(r'$\pi(\theta | x)$')
plt.title("Posterior Distribtuion")
plt.show()

print("The posterior mean is "+ str(post_mean) + 
" and the posterior standard deviation is " + str(post_stdv ))

print("For our credible set, our lower bound is  "+ str(lower) + 
" and our upper bound is " + str(upper))

