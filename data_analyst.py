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

# # Numpy

import numpy as np

# 3 x 3 
data = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
data
data[0][0]

matrix = np.array(data)
print(type(matrix))
print(matrix)

print(matrix.shape)  # 행렬 구조 출력
matrix[0]

# +
arr1 = np.arange(10)  # np.arrange(n): 0부터 n까지 값을 갖는 배열을 생성
print(arr1)

arr2 = np.arange(1,6)  # 1부터 6-1
print(arr2)

arr3 = np.arange(1,10,2)
print(arr3)

arr4 = np.random.randn(10)  # 평균이 0이고 표준편차가 1인 10개의 무작위 데이터
print(arr4)

arr5 = np.random.randn(10,5)  # 평균이 0이고 표준편차가 1인 (10 X 5) 형태 행렬로 생성
print(arr5)
# -

# 2D indexing
arr5[0,0]

# 행 또는 열 형태로 출력
arr5[0:2,:]

arr5[0,0] = 100
arr5

arr6 = np.zeros((2,2))
arr6

arr7 = np.ones((2,2))
arr7

# # Pandas

import chardet

with open('data/data/health.csv','rb') as f:
    byte_content = f.read()
    encoding = chardet.detect(byte_content)['encoding']
    print(f"Encoding: {encoding}")

import pandas as pd
df = pd.read_csv('data/data/health.csv',encoding = 'euc-kr')
df.head()

df = pd.read_excel('data/data/grade.xlsx',sheet_name='Sheet1')
print(df.shape)
df.head()


# +
table = {
    "일자":['2019-01-01','2019-01-04','2019-01-07','2019-01-10','2019-01-13'],
    "가격":[1000,15000,2000,2500,3000],
    "구매여부":['False','True','True','True','False'],
    "제품":['gum','snack','beverage','dongas','alcohoal']
}
df = pd.DataFrame(table)
print(df.shape)
df.head()

df.to_csv("product_profile.csv",encoding='euc-kr',index=False)
# -

df = pd.read_csv("data/data/auto_mpg.csv")
print(df.shape)
df.head()

df.tail()

df.head(10)

df.info()

df.dtypes

df.describe()  # 수치형 데이터에 대해서만 기초통계량을 보여줌

df.describe(include='object')

df.describe(include='all')

df_sample = df[['mpg','horsepower','weight']]
df_sample

# +
# loc 함수 : 이름을 이용한 선택
# iloc 함수 : 위치를 이용한 선택

df.loc[0:5,["horsepower","weight"]]  # [행,열] 순서로 입력
# -

df.iloc[0:6,3:5]

df.describe()

# mpg 데이터 23 이상인 데이터들만
df[df['mpg']>23]

df1 = pd.read_csv('data/data/data_con1.csv')
df2 = pd.read_csv('data/data/data_con2.csv')
df3 = pd.read_csv('data/data/data_con3.csv')

df1

df2

df3

result = pd.concat([df1,df2,df3],ignore_index=True)
result


