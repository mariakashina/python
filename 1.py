def odd_num_gen(n):
    for odd_num in range(1, n + 1):
        if odd_num % 2 == 1:
            yield odd_num


odd_to_n = odd_num_gen(15)
print(next(odd_to_n))
print(next(odd_to_n))
