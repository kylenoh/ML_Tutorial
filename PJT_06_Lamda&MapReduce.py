# Lamda 함수 이름없이 함수처럼 쓸 수 있는 익명함수

def f(x, y):
    return x + y
print(f(1,4))


f = lambda x, y: x + y
print(f(1,4))

#Map function - python 2에서는 map만쓰면 작동되지만 python3에서는 list를 붙여주어야한다.
## Sequence 자료형에 동일한 function을 적용

ex = [1,2,3,4,5]
f = lambda x : x**2
print(list(map(f,ex)))
ex = [1,2,3,4,5]
f = lambda x,y : x+y
print(list(map(f,ex,ex)))

# 조건을 넣을 수 있지만 실패했을때도 반드시 넣어주어야함
list(map(
    lambda x: x ** 2 if x %2 == 0 else x,
    ex))

#Reduce function
from functools import reduce
print(reduce(lambda x, y: x+y, [1 ,2 ,3, 4, 5]))

def factorial(n):
        return reduce(
            lambda x,y : x*y, range(1,n+1)
        )
