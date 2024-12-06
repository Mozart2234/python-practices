# Lists like a matrix

the_matrix = [[1, 2, 3], 
              [4, 5, 6], 
              [7, 8, 9]]

print(the_matrix)

print(the_matrix[0])
print(the_matrix[1][2])

# Las tuplas son inmmutables

numbers = (1, 2, 3, 4, 5)
print(numbers)
print(type(numbers))

# Por eso aqui va a dar error
# numbers[1] = 10

tuplas_of_tuples = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
print(tuplas_of_tuples)
