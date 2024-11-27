pows =  [2**x for x in range(1,10)]
print(pows)

evens = [x for x in range(1,10) if x % 2 == 0]
print(evens)

celsius = [0, 10, 20, 30, 40]
fahren = [((9/5)*temp + 32) for temp in celsius]
print(fahren)

matrix = [[1,2,3],[4,5,6],[7,8,9]]
transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]

print(matrix)
print(transposed)

