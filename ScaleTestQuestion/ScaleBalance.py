# Select the largest number which makes the running total smaller than the goal
def getGreedyPick(runningTotal, weights, goal):
    maxValue = 0
    selected = 0
    for item in weights:
        tempTotal = runningTotal + item
        if (tempTotal <= goal) and (tempTotal > maxValue):
            maxValue = tempTotal
            selected = item
    return selected


def main():
    weights = input("Input list of weights as follows x,x,x,...\n").split(',')
    weights = [int(i) for i in weights]
    goal = int(input("Input a goal weight.\n"))

    solutions = []
    for item in weights:
        solution = []
        runningTotal = item
        solution.append(item)
        while(runningTotal < goal): # Keep greedily selecting weights until we hit the goal or over shoot it
            greed = getGreedyPick(runningTotal, weights, goal)
            if (greed == 0): # All of the greedily selectable options were invalid
                break
            runningTotal += greed
            solution.append(greed)
        solutions.append(solution)
    
    minSolution = solutions[0]
    for sol in solutions:
        if (len(sol) != 0) and (len(sol) < len((minSolution))):
            minSolution = sol
    
    return minSolution
    

if __name__ == '__main__':
    print(main())