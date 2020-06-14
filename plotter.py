from matplotlib import pyplot
from scipy.interpolate import make_interp_spline, BSpline
import numpy as np
import solver
import generator
import sys

from bruteforce import brute_force
from divideandconquer import divide_and_conquer
from greedy import greedy_values

from dynamicprogramming import dynamic_programming
from branchandbound import branch_and_bound
from simulatedannealing import simulated_annealing
from genetic import genetic_algorithm

def run(numberofknapsacks):
    sys.setrecursionlimit(2147483647)
    generator.GenerateInstances(numberofknapsacks)
    runexisting(numberofknapsacks)

def runexisting(numberofknapsacks):
    sol_file = open("solution.txt", "w")
    print("Now Running On {} Knapsacks".format(numberofknapsacks))
    print("Max Number of Items in this Run: {}".format(numberofknapsacks * 5 * 10))
    print("-----------------------------------------------------------------------------")
    # bruteforce_timing,bruteforce_total_value = solver.solve(brute_force,sol_file)
    # plotData(bruteforce_timing,numberofknapsacks)
    # divideandconquer_timing,divideandconquer_total_value = solver.solve(divide_and_conquer, sol_file)
    # plotData(divideandconquer_timing,numberofknapsacks)

    greedy_timing,greedy_total_value = solver.solve(greedy_values,sol_file)
    plotData(greedy_timing,numberofknapsacks)

    dynamicprogramming_timing,dynamicprogramming_total_value = solver.solve(dynamic_programming, sol_file)
    plotData(dynamicprogramming_timing,numberofknapsacks)
    # branchandbound_timing,branchandbound_total_value = solver.solve(branch_and_bound, sol_file)
    # plotData(branchandbound_timing, numberofknapsacks)
    geneticalgorithm_timing,geneticalgorithm_total_value = solver.solve(genetic_algorithm, sol_file)
    plotData(geneticalgorithm_timing, numberofknapsacks)
    simulatedannealing_timing,simulatedannealing_total_value = solver.solve(simulated_annealing, sol_file)
    plotData(simulatedannealing_timing, numberofknapsacks)

    values =[]
    # values.append(bruteforce_total_value)
    # values.append(divideandconquer_total_value)
    values.append(greedy_total_value)
    values.append(dynamicprogramming_total_value)
    # values.append(branchandbound_total_value)
    values.append(geneticalgorithm_total_value)
    values.append(simulatedannealing_total_value)
    plotValues(values)
    sol_file.close()


def plotData(timing,numberofknapsacks):
    numbers = []
    for i in range(numberofknapsacks):
        numbers.append((i + 1)*5*10)

    # 300 represents number of points to make between T.min and T.max
    numbers_new = np.linspace(1, 50*(numberofknapsacks), 300)
    spl = make_interp_spline(numbers, timing, k=3)  # type: BSpline
    timing_smooth = spl(numbers_new)
    timing_smooth = [(i > 0) * i for i in timing_smooth]

    pyplot.plot(numbers_new, timing_smooth)
    pyplot.ylabel('Time (s)')
    pyplot.xlabel('Number of Items')
    pyplot.title('CSE224: AhmadAymanM.BahaaElDIn 17P6053')
    pyplot.legend([#'Brute Force','Divide & Conquer',
                    'Greedy', 'Dynamic Programming',
                    # 'Branch & Bound',
                   'Genetic Algorithm','Simulated Annealing',
        ],loc='upper left')
    pyplot.grid(False)

def plotValues(values):
    pyplot.figure(2)
    pyplot.title('CSE224: AhmadAymanM.BahaaElDIn 17P6053')
    pyplot.bar([
        #'Brute Force','Divide & Conquer',
                'Greedy','dynamic',
                # 'Branch & Bound',
                'genetic','simannealing'
    ], height=values)
    pyplot.ylabel('Values ($)')
    pyplot.xlabel('Approach')

def regressionrun():
    for i in range(5,30,5):
        print("Now Running On {} Knapsacks".format(i))
        print("Max Number of Items in this Run: {}".format(i*5*10))
        pyplot.figure(i/5)
        run(i)