from mpi4py import MPI
import numpy as np
from numpy import random
import matplotlib.pyplot as plt
import time


# Limits of integration
a = 0
b = 1
N = 1000

# Function to calculate x^2
def f(x):
    return x**2

# Initialize MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

start_time = None
if rank == 0:
    start_time = time.time()

# Each process generates a subset of random points
local_N = N // size
local_ar = random.uniform(a, b, local_N)
local_integral = np.sum(f(local_ar)) * (b - a) / local_N
integrals = comm.gather(local_integral, root=0)

if rank == 0:
    end_time = time.time()
    execution_time = end_time - start_time
    integral = np.sum(integrals)
    print(f"Parallel Execution Time: {execution_time} seconds")
    print(f"Estimated integral: {integral}")
    plt_vals = integrals
    plt.title("Distributions of Areas Calculated")
    plt.hist(plt_vals, bins=30, ec="black")
    plt.xlabel("Areas")
    plt.show()
