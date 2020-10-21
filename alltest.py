
import random

def produce_rpop(pop, pop_size, interval):
    # 产生实数编码种群
    for i in range(pop_size):
        pop.append(random.randint(interval[0], interval[-1]))
    return pop
pop = []
pop_size = 10
interval = [-10, 10]
pop = produce_rpop(pop, pop_size, interval)
print(pop)