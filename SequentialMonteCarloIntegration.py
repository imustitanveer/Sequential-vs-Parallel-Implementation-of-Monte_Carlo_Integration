# Importing the modules
from numpy import random
import numpy as np
import matplotlib.pyplot as plt
import time


# Limits of integration
a = 0
b = 1
N = 1000

# Function to calculate x^2
def f(x):
    return x**2

# List to store all the values for plotting
plt_vals = []

start_time = time.time()

# Iterate through all the values to generate multiple results
for _ in range(N):
    # Generate random points between a and b
    ar = random.uniform(a, b, N)
    integral = np.sum(f(ar))
    ans = (b - a) / N * integral
    plt_vals.append(ans)

end_time = time.time()
execution_time = end_time - start_time
print(f"Sequential Execution Time: {execution_time} seconds")

# Print the estimated integral
estimated_integral = np.mean(plt_vals)
print(f"Estimated integral: {estimated_integral}")

# Plot the distribution of calculated areas
plt.title("Distributions of Areas Calculated")
plt.hist(plt_vals, bins=30, ec="black")
plt.xlabel("Areas")
plt.show()