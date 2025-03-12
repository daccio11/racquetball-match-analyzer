
from itertools import combinations
# source for intertools: https://stackoverflow.com/questions/8371887/making-all-possible-combinations-of-a-list

def fair(problemDifficulties):
    difficulties = sorted(problemDifficulties)
    for i in range(2, len(difficulties)):
        if difficulties[i] > difficulties[i - 1] + difficulties[i - 2]:
            return False
    return True

def countFair(difficulties, numProblems):
    problem = list(combinations(difficulties, numProblems))

    fairCount = sum(fair(problem) for problem in problem)

    return fairCount

def validInput(n, k, problemDiff):
    if not (3 <= n <= 50):
        return False
    if not (3 <= k <= 18):
        return False
    if k >= n:
        return False
    for num in problemDiff:
        if num < 1 or num > 109:
            return False
    return True

input = input("Enter file name: ")

with open(input, 'r') as file:
    n, k = map(int, file.readline().split())
    problemDiff = [int(file.readline()) for _ in range(n)]

    if validInput(n, k, problemDiff):
        result = countFair(problemDiff, k)
        print(result)
    else:
        print("Invalid input numbers.")
