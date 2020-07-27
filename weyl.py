import numpy as np
import math
import matplotlib.pyplot as plt
import pandas


def first_N_terms_weyl(gamma, N):
    """
    Generate first N terms of the sequence in Weyl's equidistribution theorem (Theorem 1.3).
    @param gamma: The gamma parameter of the sequence in Weyl's Equidistribution Theorem.
    @param N: The number of terms to generate.
    @return: Generated sequence as a list.
    """

    result = []
    for i in np.arange(1, N + 1):
        result.append(i * gamma - math.floor(i * gamma))
    return result


def first_N_terms_golden_ratio(N):
    """
    Generate first N terms of the sequence in Proposition 1.4.
    @param N: The number of terms to generate.
    @return: Generated sequence as a list.
    """

    result = []
    golden_ratio = (1 + np.sqrt(5)) / 2
    for i in np.arange(1, N+1):
        result.append(golden_ratio**i - math.floor(golden_ratio**i))
    return result


def first_N_terms_log(a, N):
    """
    Generate first N terms of the sequence in Proposition 1.5.
    @param a: The a parameter of the sequence.
    @param N: The number of terms to generate.
    @return: Generated sequence as a list.
    """

    result = []
    for i in np.arange(1, N + 1):
        result.append(a * np.log(i) - math.floor(a * np.log(i)))
    return result


def first_N_terms_sigma(a, sigma, N):
    """
    Generate first N terms of the sequence in Proposition 1.6.
    @param a: The a parameter of the sequence.
    @param sigma: The sigma parameter of the sequence.
    @param N: The number of terms to generate.
    @return: Generated sequence as a list.
    """

    result = []
    for i in np.arange(1, N + 1):
        result.append(a * (i ** sigma) - math.floor(a * (i ** sigma)))
    return result


def first_N_terms_weyl_squared(gamma, N):
    """
    Generate first N terms of the sequence in Propoistion 1.7.
    @param gamma: The gamma parameter of the sequence.
    @param N: The number of terms to generate.
    @return: Generated sequence as a list.
    """

    result = []
    for i in np.arange(1, N + 1):
        result.append((i ** 2) * gamma - math.floor((i ** 2) * gamma))
    return result


def within_interval(sequence, a, b):
    """
    Determine how many terms in a sequence is within the interval (a, b).
    @param a: The lower bound of the interval.
    @param b: The upper bound of the interval.
    @return: The interval represented as a tuple (keep 4 decimal places), number of terms of a sequence in (a, b), and the value of b - a.
    """

    within = []
    for num in sequence:
        if (a < num) and (b > num):
            within.append(num)
    return (round(a, 4), round(b, 4)), len(within), b - a


def sample_interval(num_interval):
    """
    Generate num_interval - 1 random numbers in (0, 1) and use them to construct num_interval subintervals of (0, 1).
    @param num_interval: The number of subintervals.
    @return: A list of num_interval - 1 random numbers to construct the subintervals.
    """

    sample = np.random.rand(num_interval - 1)
    sample = sorted(sample)
    return [0] + list(sample) + [1]


def visualize_equidistribution(sequence, num_interval, step_size):
    """
    Main visualization function. Give a scatter plot of the sequence. Also give the behavior of the quantity in question over
    a given number of random subintervals of (0, 1). The dashed line is the expected limit.
    @param sequence: The sequence to visualize.
    @param num_interval: The number of intervals.
    @param step_size: The step size to use in the visualization.
    """

    plt.figure()
    plt.scatter(sequence, list(range(len(sequence))))
    plt.yticks([])

    sample = sample_interval(num_interval)
    result = dict()

    steps = list(range(0, len(sequence), step_size))
    if len(sequence) % step_size != 1:
        steps.append(len(sequence) - 1)

    for i in range(len(steps) - 1):
        for j in range(len(sample) - 1):
            interval, actual, expected = within_interval(sequence[steps[i]:steps[i + 1]], sample[j], sample[j + 1])
            if j in result.keys():
                result[j][1].append((steps[i] * result[j][1][-1] + actual) / min(steps[i + 1], len(sequence)))
            else:
                result[j] = interval, [actual / min(step_size, len(sequence))], expected

    num_plots = len(sample) - 1
    fig, ax = plt.subplots(nrows = math.ceil(num_interval / 3), ncols = 3, figsize=(15,15))
    for j in range(num_plots):
        row_id, col_id = j // 3, j % 3
        ax[row_id, col_id].plot(steps[1:], result[j][1])
        ax[row_id, col_id].axhline(result[j][2], color='black', ls = '--')
        ax[row_id, col_id].title.set_text(result[j][0])

    for j in range(num_plots, math.ceil(num_interval / 3) * 3):
        fig.delaxes(ax[j // 3][j % 3])

    plt.show()
