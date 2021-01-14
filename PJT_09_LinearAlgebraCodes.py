#Vector 를 파이썬으로 표시할때
vector_a = [1,2,10] #List 로 표현
vector_b = (1,2,10) #Tuple 로 표현
vector_c = {'x':1,'y':2,'z':10] #dict 로 표현
print(vector_a,vector_b,vector_c)

# Vector 계산###########################
#아름답지 못한 코드
u = [2, 2]
v = [2, 3]
z = [3, 5]

result=[]
for i in range(len(u)):
    result.append(u[i]+v[i]+z[i])
print(result)
#Python다운 코드
u = [2, 2]
v = [2, 3]
z = [3, 5]

result = [sum(t) for t in zip(u, v, z)]
print (result)
# Scalar-Vector (alpha가 Scalar)
u = [1, 2, 3]
v = [4, 4, 4]

alpha = 2
result = [2*sum(t) for t in zip(u, v)]
print(result)
###############################

# Matrix addition###########################
matrix_a  = [[3, 6], [4, 5]]
matrix_b  = [[5, 8], [3, 7]]

result = [[sum(row) for row in zip(*t)] for t in zip(matrix_a, matrix_b)]
print(result)
# Scalar-Matrix (alpha가 Scalar)
matrix_a = [[3, 6], [4, 5]]
alpha = 4

result = [[alpha * element for element in t] for t in matrix_a]
print(result)

# Matrix Transpose
matrix_a = [[1, 2, 3], [4, 5, 6]]
result = [[element for element in t] for t in zip(*matrix_a)]
print(result)
###############################
matrix_a = [[1, 2, 3], [4, 5, 6]]
matrix_b = [[1, 4], [2, 5], [3, 6]]
result = [[sum(a * b for a, b in zip(row_a, column_b))
          for column_b in zip(*matrix_b)] for row_a in matrix_a]
print(result)
