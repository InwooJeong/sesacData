# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.15.1
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# # CH01

# Q0. 데이터 분석에 가장 기초적으로 필요한 라이브러리 두 가지 호출(Numpy, Pandas)

import numpy as np
import pandas as pd

# Q1. 어떤 회원이 생년월일 입력란에 930913를 입력하였을 때, 해당 문자을 연/월/일로 각각 나누어 출력하기.

# +
data = '930913'
date = data[-2:]
month = data[-4:-2]
year = '19' + data[:2]

# print(date)
# print(month)
# print(year)
year, month, date
# -

# 괄호
# - [] : 대괄호 -> 인덱싱 혹은 슬라이싱과 같이 변수로부터 특정 값 추출, 리스트
# - {} : 중괄호 -> 딕셔너리, 셋
# - () : 소괄호 -> 함수, 튜플

# Q2. 매장의 물품 명단 중 하나가 'DAILY ESSENTIALS REFRESHING TONER REVIEWS' 로 되어있을 때, 해당 품명을 소문자로 바꾸기.

name = "DAILY ESSENTAILS REFRESHING TONER REVIEWS"
name.lower()

# Q3. 간단한 영한 사전 만들기  
# - 1부터 10까지 영어를 입력하면 한글로 출력되는 프로그램  
# - input 함수를 이용해서 값을 입력 받을 수 있음
# - key-value pair 형태로 프로그램을 제작해볼 것

word = input('단어를 입력해주세요 : ')
dic = {'ten':'열'}
print(dic[word])

# Q4. 아래의 리스트(list)를 선언하고, 중복 값을 제거하여 출력해보기.
# - sample_list = [1,1,1,1,1,1,2,3,4,5,6,7,7,8,9,10]

sample_list = [1,1,1,1,1,1,2,3,4,5,6,7,7,8,9,10]
s1 = set(sample_list)
print(s1)

# Q5. 값을 입력 받아 원의 넓이를 구하는 프로그램 만들기
# - input 함수를 이용해서 값을 입력 받을 수 있음
# - 입력 받은 변수를 활용해서 계산식을 세우기

a = int(input('값을 입력하시오'))
result = (3.14)*(a**2)
print(result)

# Q6. 금액을 입력했을 때, 상품 가격에 따른 잔돈을 반환하는 자판기 프로그램 만들기
# - 금액과 상품가격을 input 함수로 선언
# - 잔돈은 500,100,50,10원 단위로 반환
# - 잔돈은 가장 큰 금액부터 반환

# +
price = int(input('상품 가격'))
payment = int(input('지불 금액'))

# 거스름돈
charge = payment - price
ch1 = charge//500
charge2 = charge - ch1*500
ch2 = charge2//100
charge3 = charge2 - ch2*100
ch3 = charge3//50
charge4 = charge3 - ch3*50
cht = charge4 // 10
print("거스름",charge,"원",ch1,ch2,ch3,cht)
# -

# # CH02

# Q1. 값을 입력 받아 홀수인지 짝수인지 판별하는 프로그램 만들기

num = int(input('정수'))
"홀"if num % 2==1 else "짝"

# Q2. A부서의 월 매출이 아래와 같을 때, for문을 이용하여, A부서의 평균 월 매출 계산
# - list와 for문을 이용해서 계산
# - 1월: 5500, 2월: 5300, 3월: 6700, 4월: 5500, 5월: 5800

# +
sales_amount = [5500,5300,6700,5500,5800]
total = 0
avg = 0

for i in sales_amount:
    total += i

avg = total/len(sales_amount)    

print(total)
print(avg)
# -

# Q3. for문과 if문을 이용하여, 아래의 리스트의 최댓값을 구하는 프로그램 제작
# - sample = [10,20,4,3,6,8,44,2,50,4,1,0]

# +
sample = [10,20,4,3,6,8,44,2,50,4,1,0]
max = 0

for i in sample:
    if i > max:
        max = i

print(max)


# -

# Q4. 입력하는 모든 수의 평균을 계산하는 함수 만들기
# - 입력 개수에 상관없이 사용하기 위해, 함수 입력 값 자리에, *args를 사용함(ex. def mean(*args))

# +
def avg_amount(*args) :
    result = 0
    for i in args:
        result += i
    return result/len(args)

avg_amount(1,2,3,4,5)
# -

# Q5. Series를 이용하여 아래와 같은 성적표를 만들고, 만들어진 성적표를 for 문을 이용해 성적만 차례대로 출력하기

grade = pd.Series([70,30,80,90],name='성적표',index=['국어','영어','수학','과학'])
grade

for i in grade:
    print(i)

# Q6. Series를 이용하여 만든 위의 성적표 활용하기
# - 각 과목의 합격/불합격 여부 출력하기(50점 이상, 합격)
# - 과목의 전체 평균을 계산하여, 70점 기준으로 합격, 불합격 여부 판별

for i in grade:
    if i>=50:
        print('합격')
    else:
        print('불합격')

if grade.mean() >= 70:
    print('합')
else:
    print('불')

grade.mean()

# # CH03 & CH04

# Q0. 시각화 라이브러리 불러오기

# +
import pandas as pd
import numpy as np

data = pd.read_csv('data/data/store_market_data.csv',encoding='UTF-8-SIG')
print(data.shape)
data.head()
# -

# Q1. Pandas 라이브러리를 호출하고 예제 데이터 (store_market_data.csv)를 불러와 상위 10개와 하위 10개 데이터를 확인하기

data.head(10)
data.tail(10)



# Q2. 예제 데이터의 '물품대분류'의 카테고리 수와 '물품대분류'에 따른 '구매금액'의 합을 Pivot table을 이용해 구하기

# data.columns
data['물품대분류'].value_counts()

pd.pivot_table(data=data,index='물품대분류',values='구매금액',aggfunc=np.mean)

pd.pivot_table(data=data,index='요일',values='구매금액',aggfunc='mean')

pd.pivot_table(data=data,index='물품대분류',values='구매금액',aggfunc='sum')

# Q3. 예제 데이터의 성별을 1과 0으로 라벨 처리 하기.(남성=1, 여성=0)





# Q4. 예제 데이터에서 '요일'별로 '물품대분류'의 '구매금액'의 합을 계산하고, 판매량이 가장 높은 요일과 해당 요일에 가장 많이 판매된 품목을 확인하기



# Q5. 예제 데이터에서 일자별로 '구매금액'의 총합을 계산하고, 가장 적게 팔린 날을 확인하기



# Q6. 예제 데이터의 '성별'에 따른 '연령'을 Box Plot 하기





# Q7. 예제 데이터의 '구매금액'에 대한 요약통계량을 확인하고, 25-75% 사이의 데이터를 추출하고 그 데이터로 Dist plot 생성하기







# Q8. 예제 데이터의 구매시각에서 시간 단위만 추출하여, 새로운 Column을 만들고, 시간에 따른 구매금액의 합을 Pivot table로 구하기.  
#     더불어, '시간'에 따른 '구매금액'을 Bar plot 해보기


