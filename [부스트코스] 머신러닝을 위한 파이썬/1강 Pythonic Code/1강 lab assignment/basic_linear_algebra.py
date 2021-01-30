def vector_size_check(*vector_variables):
    return all(len(vector_variables[0]) == x for x in [len(vector) for vector in vector_variables[1:]])

print(vector_size_check([1,2,3], [2,3,4], [5,6,7]))

def vector_addition(*vector_variables):
    if vector_size_check(*vector_variables) == False:
        raise ArithmeticError
    return [sum(elements) for elements in zip(*vector_variables)]

print(vector_addition([1,3], [2,4], [6,7]))
print(vector_addition([1,5], [10,4], [4,7]))
print(vector_addition([1,3,4], [4], [6,7]))

def vector_subtraction(*vector_variables):
    if vector_size_check(*vector_variables) == False:
        raise ArithmeticError
    return [elements[0]*2-sum(elements) for elements in zip(*vector_variables)]

print(vector_subtraction([1,3], [2,4]))
print(vector_subtraction([1,5], [10,4], [4,7]))

def scalar_vector_product(alpha, vector_variable):
    return [alpha*element for element in vector_variable]

print(scalar_vector_product(5,[1,2,3]))
print(scalar_vector_product(3,[2,2]))

def matrix_size_check(*matrix_variables):
    return all([len(set(len(matrix[0]) for matrix in matrix_variables)) == 1]) and all(
        [len(set(len(matrix[0]) == len(matrix) for matrix in matrix_variables))])

matrix_x = [[2,2], [2,2], [2,2]]
matrix_y = [[2,5], [2,1]]
matrix_z = [[2,4], [5,3]]
matrix_w = [[2,5], [1,1], [2,2]]

print(matrix_size_check(matrix_x, matrix_y, matrix_z))
print(matrix_size_check(matrix_y, matrix_z))
print(matrix_size_check(matrix_x, matrix_w))

def is_matrix_equal(*matrix_variables):
    return None


def matrix_addition(*matrix_variables):
    if matrix_size_check(*matrix_variables) == False:
        raise ArithmeticError
    return None


def matrix_subtraction(*matrix_variables):
    if matrix_size_check(*matrix_variables) == False:
        raise ArithmeticError
    return None


def matrix_transpose(matrix_variable):
    return None


def scalar_matrix_product(alpha, matrix_variable):
    return None


def is_product_availability_matrix(matrix_a, matrix_b):
    return None


def matrix_product(matrix_a, matrix_b):
    if is_product_availability_matrix(matrix_a, matrix_b) == False:
        raise ArithmeticError
    return None
