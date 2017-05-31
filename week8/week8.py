import numpy as np
import matplotlib.pyplot as plt

from scipy import optimize


# Plotting
x = np.linspace(-2, 2)
x2 = x**2
absx = np.abs(x)

plt.clf()
plt.plot(x, x2, label="x^2")
plt.plot(x, absx, label="abs(x)")
plt.title("Graphs in Python")
plt.xlabel("x")
plt.ylabel("y")
plt.legend(loc="best")

plt.savefig("xsquared.pdf")


# Numerical Optimization

f = lambda x: x**2

opt = optimize.minimize(f, 1.7)

f2 = lambda x: x

opt2 = optimize.minimize(f2, 1.7)



# Decision Trees
