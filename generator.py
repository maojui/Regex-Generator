import random
from parser import *
from genetic import genotype, crossover, mutation, nextGeneration

def generator(target, POPULATION, GENERATION):
    g = 1
    result = []
    MAX_FITNESS = -1e9
    BEST_GENE = None
    BEST_REGEX = ""
    gene_count = len(genotype)
    pop = [random.sample(range(0,gene_count), gene_count) for _ in range(POPULATION)] 
    for i in range(GENERATION) :
        
        # Get result
        current_generation = []
        for idx, gene in enumerate(pop):
            g_res, fitness = parser(target, gene)
            result.append((fitness, ''.join(g_res)))
            current_generation.append((fitness, ''.join(g_res)))
            if fitness > MAX_FITNESS:
                MAX_FITNESS = fitness
                BEST_GENE = gene
                BEST_REGEX = ''.join(g_res)

        print(f'{i} Generation :')
        print(f'{MAX_FITNESS} {BEST_REGEX}')
        
        # Next generation
        total = sum([g[0] for g in current_generation])
        prob = [g[0]/total for g in current_generation]
        pop = nextGeneration(pop, prob)

    return result