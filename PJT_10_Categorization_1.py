# 동일한 내용으로 모을 수 있는 방법이 무었이있을까

# - 유사한가? 피타고라스를 만들어서 두 점사이의 거리가 가까운가를 확인
# - 유사한가? 두점사이의 각도를 측정한다.

#   프로세스
#   단어별로 Index 만들기
#   만들어진 Index로 문서별 Bag of words vector 생성
#   비교하고자하는 문서 비교하기
#   얼마나 맞는지 측정

import os

#   1.  해당경로에 파일 리스트 추출(파일불러오기)
def get_file_list(dir_name):
    return os.listdir(dir_name)

#   2.  파일 읽어서 단어사전 만들기(0은 야구 , 1은 축구)
def get_conetents(file_list):
    y_class = []
    X_text = []
    class_dict = {1: "0", 2: "0", 3:"0", 4:"0", 5:"1", 6:"1", 7:"1", 8:"1"}

    for file_name in file_list:
        try:
            f = open(file_name, "r",  encoding="cp949")
            category = int(file_name.split(os.sep)[1].split("_")[0])
            y_class.append(class_dict[category])
            X_text.append(f.read())
            f.close()
        except UnicodeDecodeError as e:
            print(e)
            print(file_name)
    return X_text, y_class

#   3.  Corpus 만들기
def get_corpus_dict(text):
    # 파일안에담긴 문장을 가져와서 나눠서 다시 담아줌
    text = [sentence.split() for sentence in text]
    clenad_words = [get_cleaned_text(word) for words in text for word in words]

    from collections import OrderedDict
    corpus_dict = OrderedDict()
    for i, v in enumerate(set(clenad_words)):
        corpus_dict[v] = i
    return corpus_dict

#   3-1.    단어가 들어오면 문장부호 제거 및 소문자 반환
def get_cleaned_text(text):
    import re
    text = re.sub('\W+','', text.lower() )
    return text
#   print(get_cleaned_text("I'm your energy")) 함수 테스트

#   4.  전처리방식이 동일한 단어를뽑아서
def get_count_vector(text, corpus):
    text = [sentence.split() for sentence in text]
    word_number_list = [[corpus[get_cleaned_text(word)] for word in words] for words in text]
#    print(word_number_list)    첫번째 문서의 첫 단어가 Copus Dict 어디에 담겼을까?
#   for문에 _는 이변수는 사용하지 않는다는 의미 in range(len(text)) == 80
    X_vector = [[0 for _ in range(len(corpus))] for x in range(len(text))]

    for i, text in enumerate(word_number_list):
        for word_number in text:
            X_vector[i][word_number] += 1
    return X_vector

#   5.  비교하기
import math
def get_cosine_similarity(v1,v2):
    "compute cosine similarity of v1 to v2: (v1 dot v2)/{||v1||*||v2||)"
    sumxx, sumxy, sumyy = 0, 0, 0
    for i in range(len(v1)):
        x = v1[i]; y = v2[i]
        sumxx += x*x
        sumyy += y*y
        sumxy += x*y
    return sumxy/math.sqrt(sumxx*sumyy)

#   5-1.    비교 결과확인
def get_similarity_score(X_vector, source):
    source_vector = X_vector[source]
    similarity_list = []
    for target_vector in X_vector:
        similarity_list.append(
            get_cosine_similarity(source_vector, target_vector))
    return similarity_list


def get_top_n_similarity_news(similarity_score, n):
    import operator
    x = {i:v for i, v in enumerate(similarity_score)}
    sorted_x = sorted(x.items(), key=operator.itemgetter(1))

    return list(reversed(sorted_x))[1:n+1]

def get_accuracy(similarity_list, y_class, source_news):
    source_class = y_class[source_news]

    return sum([source_class == y_class[i[0]] for i in similarity_list]) / len(similarity_list)


#   Main
if __name__ == "__main__":
    dir_name = "news_data"
    file_list = get_file_list(dir_name)
    file_list = [os.path.join(dir_name,file_name) for file_name in file_list]
#    print(file_list)   해당경로에 파일명 출력
#    print(len(file_list))  파일의 갯수 출력

    X_text, y_class = get_conetents(file_list)
#    print(X_text)  파일안에있는 문서 가져오기
#    print(y_class) 야구(0),축구(1)분류인덱스만들기

    corpus = get_corpus_dict(X_text)
#    print(corpus)  띄어쓰기 마다 중복되지 않게 만듬
#    print("Number of words : {0}".format(len(corpus))) 중복되지않은 단어의 갯수

    X_vector = get_count_vector(X_text, corpus)
#   print(X_vector[0])  어떤 위치에 몇개나 있는지 확인해줄 수 있다

    source_number = 10
    result = []
    for i in range(80):
        source_number = i

        similarity_score = get_similarity_score(X_vector, source_number)
        similarity_news = get_top_n_similarity_news(similarity_score, 10)
        accuracy_score = get_accuracy(similarity_news, y_class, source_number)
        result.append(accuracy_score)
    print(sum(result) / 80)
#    similarity_score   80개의 문서들이 얼마나 비슷한지
#    similarity_news    10개중 가장 유사한 값 10개를 비교
#    accuracy_score     정확도는 얼마인가
