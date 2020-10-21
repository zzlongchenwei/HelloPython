import random
m = 3
pop = [0,1,2,3]
temp = pop
new_pop = []
while True:
    n = random.randint(0, m)
    print(n)
    new_pop = temp.pop(n)
    print(new_pop)
    m -= 1
    if m == -1 :break