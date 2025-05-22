import math
import random
from typing import List, Tuple
from pair import *
from mainUtils import *


# TAHAP 1 
def RandomPopulation(n: int, populationCount: int) -> List[str]:
    population = []
    for _ in range(n):
        individual = ''.join(random.choice(['0', '1']) for _ in range(populationCount))
        population.append(individual)
    return population

def Decode(binary_str: str) -> float:
    rMin = -10
    rMax = 10
    N = len(binary_str)
    denominator = 0
    
    denominator = 0.0
    for i in range(1, N + 1):
        denominator += math.pow(2, -i)
        
    binaryValue = 0.0
    for i in range(N):
        bit = int(binary_str[i])
        binaryValue += bit * math.pow(2, -(i + 1))
        
    x = rMin + ((rMax - rMin) / denominator) * binaryValue
    return x

def tournamentSelection(population: List[str], k: int) -> str:
    best = None
    for _ in range(k):
        individual = random.choice(population)
        if best is None or Fitness(individual) > Fitness(best):
            best = individual
    return best

def selectParents(population: List[str], k: int = 3) -> Tuple[str, str]:
    parent1 = tournamentSelection(population, k)
    parent2 = tournamentSelection(population, k)

    while parent2 == parent1:
        parent2 = tournamentSelection(population, k)

    return parent1, parent2

def Fitness(individual: str) -> float:
    x1, x2 = Decode(individual[:BIT_PER_GEN]), Decode(individual[BIT_PER_GEN:])
    return -(Objective(x1, x2))
    
# Fungsi crossover titik tunggal (Single-Point Crossover)
def singlePointCrossover(parent1, parent2: str, crossoverRate: float) -> Tuple[str, str]:  
    randomNumber = round(random.uniform(0, 1), 1)
    
    if randomNumber < crossoverRate:
        point = random.randint(1, len(parent1) - 1)  # Hindari titik di awal/akhir
        print(f"CrossOver pada titik {point}")
        offSpring1 = parent1[:point] + parent2[point:]
        offSpring2 = parent2[:point] + parent1[point:]
    else:
        print("CrossOver tidak terjadi.")
        offSpring1 = parent1
        offSpring2 = parent2 
    return offSpring1, offSpring2

def Mutation(individual: str, mutationCount) -> str:
    length = len(individual)

    individual = list(individual)
    mutationIndices = random.sample(range(length), mutationCount)

    for idx in mutationIndices:
        individual[idx] = '1' if individual[idx] == '0' else '0'

    return ''.join(individual)

def Objective(x1, x2: float) -> float:
    # result = -(math.sin(x1) * math.cos(x2) * math.tanh(x1 + x2) + (0.75) * math.exp(1 - abs(x1 + 1.6)))
    # return result

    result = -(math.sin(x1) * math.cos(x2) * math.tanh(x1 + x2) + (0.75) * math.exp(1 - abs(x1)))
    return result

 