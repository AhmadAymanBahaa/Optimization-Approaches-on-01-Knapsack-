import collections
import functools

class memoize(object):
    """This function caches the values of the best values of subproblems
        So, if a similar problem is encountered, it is returned instead of
        Reevaluation
    """
    def __init__(self, func):
        self.func = func
        self.cache = {}

    def __call__(self, *args):
        if not isinstance(args, collections.Hashable):
            # uncacheable. a list, for instance.
            # better to not cache than blow up.
            return self.func(*args)
        if args in self.cache:
            return self.cache[args]
        else:
            value = self.func(*args)
            self.cache[args] = value
            return value

    def __repr__(self):
        """Return the function's docstring."""
        return self.func.__doc__

    def __get__(self, obj, objtype):
        """Support instance methods."""
        return functools.partial(self.__call__, obj)

def dynamic_programming(number, capacity, weight_value):
    """
    Solve the knapsack problem by finding the most valuable
    subsequence of `weight_value` subject that weighs no more than
    `capacity`.
    :param number: number of items to available
    :param capacity: the capacity of the knapsack
    :param weight_value: list of tuples that have this format: [(weight, value), (weight, value), ...]
    :return: a pair whose first element is the sum of values in the best combination,
    and whose second element is the combination.
    """

    # Return the value of the most valuable subsequence of the first i
    # elements in items whose weights sum to no more than j.
    @memoize
    def bestvalue(i, j):
        if i == 0:
            return 0
        weight, value = weight_value[i - 1]
        if weight > j:
            return bestvalue(i - 1, j)
        else:
            # maximizing the value
            return max(bestvalue(i - 1, j), bestvalue(i - 1, j - weight) + value)

    j = capacity
    result = [0] * number
    for i in range(len(weight_value), 0, -1):
        if bestvalue(i, j) != bestvalue(i - 1, j):
            result[i - 1] = 1
            j -= weight_value[i - 1][0]
    return bestvalue(len(weight_value), capacity), result
