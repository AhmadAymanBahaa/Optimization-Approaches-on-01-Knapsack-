from time import time

def parse_line(line):
    """Line parser method
    :param line: line from input file
    :return: tuple like: (instance id, number of items, knapsack capacity,
                            list of tuples like: [(weight, value), (weight, value), ...])
    """
    parts = [int(value) for value in line.split()]
    inst_id, number, capacity = parts[0:3]
    weight_value = [(parts[i], parts[i + 1]) for i in range(3, len(parts), 2)]
    return inst_id, number, capacity, weight_value


def solve(method, sol_file):
    """Main method that solves knapsack problem using one of the existing methods
    :param method: knapsack problem solving method
    :param inst_file_path: path to file with input instances
    :param solution_file_path: path to file where solver should write output data
    """
    t_start = time()
    inst_file = open("testdata.txt", "r")
    sol_file.write(method.__name__ + "\n")
    timings = []
    total_value=0
    for line in inst_file:
        t_inital = time()
        inst_id, number, capacity, weight_value = parse_line(line)
        # get best value and variables combination
        try:
            best_value, best_combination = method(number, capacity, weight_value)
        except Exception:
            print("Exception Occured During {}".format(method.__name__), type(Exception))
        best_combination_str = " ".join("%s" % i for i in best_combination)
        t_final = time()
        # write best result to file
        sol_file.write("%s %s $%s  %s\n" % (inst_id, number,best_value, best_combination_str))
        timings.append(t_final-t_inital)
        total_value+= best_value
    inst_file.close()

    total_time = 0
    t_finish = time()
    total_time += (t_finish - t_start)

#print("Average solving time: %ss (repetitions count %s)" % (solving_time / repeat, repeat))
    print("{:>20}:\t\t TotalTime:{:>6}(s)\t\tTotalValue: {:>6}$".format(method.__name__, total_time.__round__(4),total_value))
    sol_file.write("{}: \t\t\t\tTotalTime: {}\t\tTotalValue: ${} \n".format(method.__name__, total_time.__round__(4),total_value))
    return timings,total_value