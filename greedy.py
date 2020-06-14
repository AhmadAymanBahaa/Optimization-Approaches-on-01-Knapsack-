def greedy_values(number, capacity, weight_value):
    """Greedy on Values function for solving 01 knapsack problem
    :param number: number of items to available
    :param capacity: the capacity of the knapsack
    :param weight_value: list of tuples that have this format: [(weight, value), (weight, value), ...]
    :return: tuple of: (best value, best combination list(contains 1 and 0))
    """
    weight_value_= list(weight_value)
    weight_value_.sort(key=lambda x:x[1],reverse=True)

    best_combination = [0] * number
    best_value = 0
    weight = 0

    for i in range(number-1):
        weight += weight_value_[i][0]
        if (weight < capacity):
            best_value += weight_value_[i][1]
            original_index = weight_value.index(weight_value_[i])
            best_combination[original_index] = 1
        else:
            weight -= weight_value_[i][0]
    return best_value, best_combination