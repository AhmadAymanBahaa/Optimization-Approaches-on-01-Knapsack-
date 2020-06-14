from collections import deque

class SimpleQueue(object):
    def __init__(self):
        self.buffer = deque()
    def push(self, value):
        self.buffer.appendleft(value)
    def pop(self):
        return self.buffer.pop()
    def __len__(self):
        return len(self.buffer)

class Node(object):
    def __init__(self, level, selected_items, value, weight, bound):
        self.level = level
        self.selected_items = selected_items
        self.value = value
        self.weight = weight
        self.bound = bound

def branch_and_bound(number, capacity, weight_value):
    """Branch and bound function for solving 01 knapsack problem
    :param number: number of items to available
    :param capacity: the capacity of the knapsack
    :param weight_value: list of tuples that have this format: [(weight, value), (weight, value), ...]
    :return: tuple of: (best value, best combination list(contains 1 and 0))
    """
    priority_queue = SimpleQueue()

    #sort items in non-increasing order by benefit/value
    ratios = [(index, item[1] / float(item[0])) for index, item in enumerate(weight_value)]
    ratios = sorted(ratios, key=lambda x: x[1], reverse=True)

    best_so_far = Node(0, [], 0.0, 0.0, 0.0)
    a_node = Node(0, [], 0.0, 0.0, calculate_bound(best_so_far, number, capacity, weight_value, ratios))
    priority_queue.push(a_node)

    while len(priority_queue) > 0:
        current_node = priority_queue.pop()
        if current_node.bound > best_so_far.value:
            curr_node_index = ratios[current_node.level][0]
            next_item_value = weight_value[curr_node_index][1]
            next_item_weight = weight_value[curr_node_index][0]
            next_added = Node(
                current_node.level + 1,
                current_node.selected_items + [curr_node_index],
                current_node.value + next_item_value,
                current_node.weight + next_item_weight,
                current_node.bound
            )

            if next_added.weight <= capacity:
                if next_added.value > best_so_far.value:
                    best_so_far = next_added

                if next_added.bound > best_so_far.value:
                    priority_queue.push(next_added)

            next_not_added = Node(current_node.level + 1, current_node.selected_items, current_node.value,
                                  current_node.weight, current_node.bound)
            next_not_added.bound = calculate_bound(next_not_added, number, capacity, weight_value, ratios)
            if next_not_added.bound > best_so_far.value:
                priority_queue.push(next_not_added)

    best_combination = [0] * number
    for wc in best_so_far.selected_items:
        best_combination[wc] = 1
    return int(best_so_far.value), best_combination


def calculate_bound(node, number, capacity, weight_value, ratios):
    if node.weight >= capacity:
        return 0
    else:
        upper_bound = node.value
        total_weight = node.weight
        current_level = node.level

        while current_level < number:
            current_index = ratios[current_level][0]

            if total_weight + weight_value[current_index][0] > capacity:
                value = weight_value[current_index][1]
                weight = weight_value[current_index][0]
                upper_bound += (capacity - total_weight) * value/weight
                break

            upper_bound += weight_value[current_index][1]
            total_weight += weight_value[current_index][0]
            current_level += 1

        return upper_bound

