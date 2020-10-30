import random
range_list = list(range(14))
print(range_list)
# random.shuffle(range_list)
# print(range_list)
print(random.sample(range_list, k=len(range_list)))
