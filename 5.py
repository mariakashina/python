from time import perf_counter

start = perf_counter()
src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
unique = []
unique_set = set()
repeat = set()
for el in src:
    if el not in repeat:
        unique.append(el)
        unique_set.add(el)
    else:
        unique_set.discard(el)
    repeat.add(el)
result = [el for el in unique if el in unique_set]
print(result)
print(perf_counter() - start)
