import math
import random

ALPHA_RATE = 0.85


def simulated_annealing(number, capacity, weight_cost, init_temp=100, steps=100):
    start_sol = init_solution(weight_cost, capacity)
    best_cost, solution = simulate(start_sol, weight_cost, capacity, init_temp, steps)
    best_combination = [0] * number
    for idx in solution:
        best_combination[idx] = 1
    return best_cost, best_combination


def init_solution(weight_cost, max_weight):
    """For generating initial solution.
    By adding a random item while weight that is less than the max_weight
    """
    solution = []
    allowed_positions = range(len(weight_cost))
    while len(allowed_positions) > 0:
        idx = random.randint(0, len(allowed_positions) - 1)
        selected_position = allowed_positions[idx]
        if get_cost_and_weight_of_knapsack(solution + [selected_position], weight_cost)[1] <= max_weight:
            solution.append(selected_position)
        else:
            break
    return solution


def get_cost_and_weight_of_knapsack(solution, weight_cost):
    """Get the cost and weight of the knapsack - fitness function
        """
    cost, weight = 0, 0
    for item in solution:
        weight += weight_cost[item][0]
        cost += weight_cost[item][1]
    return cost, weight


def moveto(solution, weight_cost, max_weight):
    """All possible moves are generated"""
    moves = []
    for index, _ in enumerate(weight_cost):
        if index not in solution:
            move = solution[:]
            move.append(index)
            if get_cost_and_weight_of_knapsack(move, weight_cost)[1] <= max_weight:
                moves.append(move)
    for index, _ in enumerate(solution):
        move = solution[:]
        del move[index]
        if move not in moves:
            moves.append(move)
    return moves



def simulate(solution, weight_cost, max_weight, initial_temp, steps):
    """Simulated annealing approach for Knapsack problem"""
    temperature = initial_temp

    best = solution
    best_cost = get_cost_and_weight_of_knapsack(solution, weight_cost)[0]

    current_sol = solution
    while True:
        current_cost = get_cost_and_weight_of_knapsack(best, weight_cost)[0]
        for i in range(0, steps):
            moves = moveto(current_sol, weight_cost, max_weight)
            index = random.randint(0, len(moves) - 1)
            random_move = moves[index]
            delta = get_cost_and_weight_of_knapsack(random_move, weight_cost)[0] - best_cost
            if delta > 0:
                best = random_move
                best_cost = get_cost_and_weight_of_knapsack(best, weight_cost)[0]
                current_sol = random_move
            else:
                if math.exp(delta / float(temperature)) > random.random():
                    current_sol = random_move

        temperature *= ALPHA_RATE
        if current_cost >= best_cost or temperature <= 0:
            break
    return best_cost, best