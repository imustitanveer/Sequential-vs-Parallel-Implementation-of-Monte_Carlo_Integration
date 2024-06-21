# Monte Carlo Integration Performance Comparison

This repository presents the findings and code implementations of a study comparing the performance of sequential and parallel Monte Carlo integration methods. The study focuses on execution times, speedup, and the accuracy of the estimated integrals.

## Overview

Monte Carlo integration is a technique for estimating definite integrals using random sampling. This study explores two approaches:

- **Sequential Monte Carlo Integration**
- **Parallel Monte Carlo Integration** using Message Passing Interface (MPI)

## Key Findings

1. **Performance**: Parallel Monte Carlo integration generally outperforms sequential integration in terms of execution times.
2. **Speedup**: The best speedup is observed with 2 parallel processes. Adding more processes can introduce overhead that degrades performance.
3. **Accuracy**: There is no statistically significant difference in the accuracy of the estimated integrals between sequential and parallel implementations.

## Repository Contents

- **Report**: Detailed analysis and findings of the performance comparison.
- **Code**: Implementations of both sequential and parallel Monte Carlo integration methods.

## Getting Started

### Prerequisites

- Python 3.x
- `numpy` library
- `matplotlib` library
- `mpi4py` library (for parallel implementation)

### Installing Dependencies

To install the necessary dependencies, run:

```bash
pip install -r requirements.txt
```

### Running the Code

#### Sequential Implementation

To run the sequential Monte Carlo integration, execute:

```bash
python sequential_monte_carlo.py
```

#### Parallel Implementation

To run the parallel Monte Carlo integration using MPI, execute:

```bash
mpiexec -n <number_of_processes> python parallel_monte_carlo.py
```

Replace `<number_of_processes>` with the desired number of parallel processes.

## Appendix

### Execution Times Table

| Sequential Execution Time (s) | Parallel Execution Time (s) |
|-------------------------------|-----------------------------|
| 0.016993                      | 0.000781                    |
| 0.014776                      | 0.001783                    |
| 0.015001                      | 0.000999                    |
| 0.015594                      | 0.000999                    |
| 0.014987                      | 0.000999                    |
| 0.014998                      | 0.000999                    |

### Estimated Integrals Table

| Sequential Estimated Integral | Parallel Estimated Integral |
|-------------------------------|-----------------------------|
| 0.333373                      | 0.315372                    |
| 0.333455                      | 0.335515                    |
| 0.333430                      | 0.335481                    |
| 0.333735                      | 0.342350                    |
| 0.332486                      | 0.323946                    |
| 0.333125                      | 0.328341                    |

Feel free to explore the code and the report to gain deeper insights into the performance comparison of sequential and parallel Monte Carlo integration methods.
