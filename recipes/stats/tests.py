from math import sqrt
from scipy.stats import norm


def wald_proportion_compare(count1, nobs1, count2, nobs2):
    '''Perform wald binomial proportion test

    H0: p1 = p2
    H1: p1 != p2

    If statistics is low, and p-value is high, then we cannot reject the null hypothesis.
    If statistics is high, and p-value is low, then we can reject the null hypothesis.

    :param count1: Number of successes in first sample
    :param nobs1: Number of trials in first sample
    :param count2: Number of successes in second sample
    :param nobs2: Number of trials in second sample
    :return: (z, p-value)
    '''

    p1_hat, p2_hat, p_hat = count1 / nobs1, count2 / nobs2, (count1 + count2) / (nobs1 + nobs2)
    z = (p1_hat - p2_hat) / sqrt(p_hat * (1 - p_hat) * (1 / nobs1 + 1 / nobs2))
    return z, norm.cdf(-1 * abs(z)) * 2
