#Enumerate 란 List에서 값을 추출할떄 Index도 함께 추출하는것

alist = ['a1', 'a2', 'a3']
blist = ['b1', 'b2', 'b3']

for i, v in enumerate(['tic','tac','toe']):
    print(i,v)

mylist = ['a','b','c','d']
l = list(enumerate(mylist))
print(l)

# ZIP 두개의 List 값을 병렬적으로 추출함
for a, b in zip(alist, blist):
    print(a, b)


a, b, c = zip((1, 2, 3), (10, 20, 30), (100, 200, 300))
print(a, b, c)

# 튜플형태로 저장됨
print([sum(x) for x in zip((1, 2, 3), (10, 20, 30), (100, 200, 300))])

alist = ['a1', 'a2', 'a3']
blist = ['b1', 'b2', 'b3']

for i, (a, b) in enumerate(zip(alist, blist)):
    print(i, a, b)
