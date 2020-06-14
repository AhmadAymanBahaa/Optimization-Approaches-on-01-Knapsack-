from itertools import combinations

def brute_force(number, capacity, weight_value):
    """Brute force algorithm to solve 01 Knapsack
    :param number: number of items to available
    :param capacity: the capacity of the knapsack
    :param weight_value: list of tuples that have this format: [(weight, value), (weight, value), ...]
    :return: tuple of: (best value, best combination list(contains 1 and 0))
    """
    best_value = None
    best_combination = []
    # generating combinations by all ways: C by 1 from n, C by 2 from n, ...
    for way in range(number):
        for comb in combinations(weight_value, way + 1):
            weight = sum([wc[0] for wc in comb])
            value = sum([wc[1] for wc in comb])
            if (best_value is None or best_value < value) and weight <= capacity:
                best_value = value
                best_combination = [0] * number
                for wc in comb:
                    best_combination[weight_value.index(wc)] = 1
    return best_value, best_combination

