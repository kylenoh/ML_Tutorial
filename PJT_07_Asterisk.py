
#1은 a에 들어가고 나머지는 args에 들어간다.
def asterisk_test(a, *args):
    print(a, args)
    print(type(args))

asterisk_test(1,2,3,4,5,6)

# 키워드를 포함한다면 **뒤게를씀으로써 넘어간다.
def asterisk_test(a, **kargs):
    print(a, kargs)
    print(type(kargs))

asterisk_test(1, b=2, c=3, d=4, e=5, f=6)

# tuple 타입으로 들어가고 0번지를 지정하지않는다면 괄호가 2개생
def asterisk_test(a, *args):
    print(a, args[0])
    print(type(args))
asterisk_test(1, (2, 3, 4, 5, 6))

def asterisk_test(a, args):
# print에 *붙임으로써 unpacking하게 보여준다.
    print(a, *args)
    print(type(args))
asterisk_test(1, (2,3,4,5,6))

a, b, c = ([1, 2], [3, 4], [5, 6])
print(a, b, c)

data = ([1, 2], [3, 4], [5, 6])
print(*data)

for data in zip(*([1, 2], [3, 4], [5, 6])):
    print(sum(data))

def asterisk_test(a, b, c, d, e=0):
    print(a, b, c, d, e)
# dict타입을 뜯어서 하나씩 넣어준다.(근데 왜 안될까..)
data = {"d":1 , "c":2, "b":3, "e":56}
    asterisk_test(10, **data)
