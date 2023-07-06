from typing import List
import math

def mean(xs: List[float]) -> float:
    return sum(xs) / len(xs)
assert mean([1,2,3,4,5]) == 3

def _median_odd(xs: List[float]) -> float:
    """If len(xs) is odd, the median is the middle element"""
    return sorted(xs)[len(xs) // 2]
def _median_even(xs: List[float]) -> float:
    """If len(xs) is even, it's the average of the middle two elements"""
    sorted_xs = sorted(xs)
    hi_midpoint = len(xs) // 2  # e.g. length 4 => hi_midpoint 2
    return (sorted_xs[hi_midpoint - 1] + sorted_xs[hi_midpoint]) / 2
def median(v: List[float]) -> float:
    """Finds the 'middle-most' value of v"""
    return _median_even(v) if len(v) % 2 == 0 else _median_odd(v)
assert median([1, 10, 2, 9, 5]) == 5
assert median([1, 9, 2, 10]) == (2 + 9) / 2

def data_range(xs: List[float]) -> float:
    return max(xs) - min(xs)
assert data_range([1,2,3,4,5]) == 4

def de_mean(xs: List[float]) -> List[float]:
    """Translate xs by subtracting its mean (so the result has mean 0)"""
    x_bar = mean(xs)
    return [x - x_bar for x in xs]
def variance(xs: List[float]) -> float:
    """Almost the average squared deviation from the mean"""
    assert len(xs) >= 2, "variance requires at least two elements"
    n = len(xs)
    deviations = de_mean(xs)
    return sum(d*d for d in deviations) / (n - 1) # sum of squares
assert variance([1,2,3,4,5]) == 2.5
def standard_deviation(xs: List[float]) -> float:
    """The standard deviation is the square root of the variance"""
    return math.sqrt(variance(xs))
assert 1.58 < standard_deviation([1,2,3,4,5]) < 1.59

from helper.linear_algebra import dot
def covariance(xs: List[float], ys: List[float]) -> float:
    assert len(xs) == len(ys), "xs and ys must have same number of elements"
    return dot(de_mean(xs), de_mean(ys)) / (len(xs) - 1)
def correlation(xs: List[float], ys: List[float]) -> float:
    """Measures how much xs and ys vary in tandem about their means"""
    stdev_x = standard_deviation(xs)
    stdev_y = standard_deviation(ys)
    if stdev_x > 0 and stdev_y > 0:
        return covariance(xs, ys) / stdev_x / stdev_y
    else:
        return 0    # if no variation, correlation is zero

def initial_statistics(xs: List[float]) -> dict:
    """Return a dict with the 'Mean', 'Median' and 'Standard Deviation'"""
    assert len(xs) > 1, "The list must have more then one item"
    return {"Max": max(xs),
            "Min": min(xs),
            "Range": max(xs)-min(xs),
            "Mean": mean(xs),
            "Median": median(xs),
            "Standard Deviation": standard_deviation(xs)}
