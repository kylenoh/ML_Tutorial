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

#   2.  파일 읽어서 단어사전 만들기
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


if __name__ == "__main__":
    dir_name = "news_data"
    file_list = get_file_list(dir_name)
    file_list = [os.path.join(dir_name,file_name) for file_name in file_list]
    print(file_list)
    print(len(file_list))

    X_text, y_class = get_conetents(file_list)
    print(X_text)
    print(y_class)
