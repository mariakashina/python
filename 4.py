src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result = [el for i, el in enumerate(src[1:], 1) if el > src[i-1]]
print(result)
