sides = [2,3,5,7]

import itertools
sides_r = [max(0, x - 2) for x in sides]
product = lambda lst: 1 if not lst else lst[0] * product(lst[1:])

tot = 0
for i in range(1,len(sides)+1):
    count = 2**i*sum(product(comb) for comb in itertools.combinations(sides_r, len(sides) - i))
    print(str(i)+"c pieces: ", count)
    tot += count
print("Total pieces: ", tot)