#deque
# - Stack 과 Queue 를 지원하는 모듈
# - List 에 비해 효율적인 자료 저장 방식 지원
# - rotate,reverse 등 Linked List 특성 지원

from collections import deque

deque_list = deque()
for i in range(5):
    deque_list.append(i)
print(deque_list)

deque_list.appendleft(10)
print(deque_list)

deque_list.rotate(2)
print(deque_list)


deque_list.extend([5,6,7])
print(deque_list)

deque_list.extendleft([5,6,7])
print(deque_list)

print(deque_list)
print(deque(reversed(deque_list)))
#defaultdict
#-DictType의 기본값을 지정
from collections import defaultdict
d = defaultdict(object)
d = defaultdict(lambda: 0 )
print(d["first"])

#OrderedDict
#-Dict는 저장한 순서대로 출력하지않음 하지만 입력순서대로 dict반환
from collections import OrderedDict

text = """A press release is the quickest and easiest wa to get.""".lower().split()

print(text)

#word_count 시 defaultdict 미 사용
word_count={}
for word in text:
    if word in word_count.keys():
        word_count[word]+=1
    else:
        word_count[word]=0
print(word_count)

#word_count 시  defaultdict 사용
word_count = defaultdict(object)
word_count = defaultdict(lambda : 0 )
for word in text:
    word_count[word]+=1
for i, v in OrderedDict(sorted(
        word_count.items(), key=lambda t: t[1],
        reverse=True)).items():
    print(i,v)

#Count
# - Sequence Type 의 data element 갯수를 dict 형태로 반환
from collections import Counter
c = Counter()                           # a new, empty counter
c = Counter('gallahad')                 # a new counter from an iterable
print(c)
