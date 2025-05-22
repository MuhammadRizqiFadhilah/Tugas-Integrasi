from MathFunction import *
from pair import *
from typing import List
from header import *

MAX_GENERATIONS = 10000
CROSSOVER_RATE = 0.8
MUTATION_RATE = 0.2
POPULATIONS = 10
CHROMOSOME_LENGTH = 16


bestChromosome = None
bestFitness = float("inf")
randomPopulation = RandomPopulation(POPULATIONS, CHROMOSOME_LENGTH)


# for i in range(0, POPULATIONS):
#     print(randomPopulation[i], " ", Fitness(randomPopulation[i]))

for i in range(1, MAX_GENERATIONS):
    # print()
    print(f"======================= GENERASI {i} =======================")
    parent1, parent2 = selectParents(randomPopulation, 3)
    # print(parent1, " ", parent2)
    # print(Decode(parent1[:8]), " ", Decode(parent1[8:]), " ", Decode(parent2[:8]), " ", Decode(parent2[8:]))

    mutationBit = math.floor(MUTATION_RATE * CHROMOSOME_LENGTH)
    child1, child2 = singlePointCrossover(parent1, parent2, CROSSOVER_RATE)
    # print(f"Stelah krosover : {child1} {child2}")
    # print(f"sbelum mutasi : {child1}")
    # print(f"sbelum mutasi : {child2}")
    
    selected1 = Mutation(child1, mutationBit)
    selected2 = Mutation(child2, mutationBit)
    # print(f"stelah mutasi : {selected1}")
    # print(f"stelah mutasi : {selected2}")

    # print(f"objective gen {i} {Objective(Decode(selected1[:8]), Decode(selected1[8:]))}, {Objective(Decode(selected2[:8]), Decode(selected2[8:]))}")

    # Hitung objective untuk semua individu
    fitnessValues = [Objective(Decode(ind[:8]), Decode(ind[8:])) for ind in randomPopulation]

    # Ganti dua terburuk dengan hasil mutasi
    worstIndices = sorted(
        range(len(fitnessValues)), 
        key=lambda k: fitnessValues[k], 
        reverse=True
    )
    randomPopulation[worstIndices[0]] = selected1
    randomPopulation[worstIndices[1]] = selected2

    # Cek kromosom terbaik sejauh ini
    currentBestIndex = min(range(len(fitnessValues)), key=lambda k: fitnessValues[k])
    currentBestFitness = fitnessValues[currentBestIndex]
    if currentBestFitness < bestFitness:
        bestGeneration = i
        bestFitness = currentBestFitness
        bestChromosome = randomPopulation[currentBestIndex]


x = Decode(bestChromosome[:8])
y = Decode(bestChromosome[8:])
print(f"\nKromosom terbaik selama seluruh generasi:")
print(f"{bestChromosome} -> x={x}, y={y}, Objective={bestFitness} pada generasi ke {bestGeneration}")
    


