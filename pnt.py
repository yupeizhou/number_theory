import numpy as np
import math
import matplotlib.pyplot as plt


def sieve(n):
    """
    Return primes up to n using an elementary sieve method.
    @param n: The number of primes to generate.
    @return: A list of prime numbers up to n.
    """

    n = math.floor(n)
    primes = [True for i in range(n + 1)]
    p = 2
    while p * p <= n:
        if primes[p] == True:
            for i in range(p * 2, n + 1, p):
                primes[i] = False
        p += 1
    primes[0], primes[1] = False, False
    return [num for num in range(n + 1) if primes[num]]


def visualize_prime_thm(N, step_size):
    """
    Visualize the behavior of the quantity in question given an upper limit N and step size. The dashed line is the expected limit.
    @param N: The number of terms to use in the visualization.
    @param step_size: The step_size to use in the visualization.
    """

    primes = sieve(N)
    steps = np.linspace(2, N, step_size)
    result = [len([y for y in primes if y <= x]) / (x / np.log(x)) for x in steps]
    plt.plot(steps, result)
    plt.axhline(1, color='black', ls = '--')
    plt.show()
