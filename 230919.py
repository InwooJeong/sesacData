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

# # 데이터 분석 절차

# 1. DDA(Descriptive Data Analysis) : 묘사적 데이터 분석
#     - 데이터의 설명 변수(x)와 목표 변수(y)
# 2. EDA(Exploartory Data Analysis) : 탐색적 데이터 분석
#     - 데이터 시각화
# 3. CDA(Confirmatory Data Analysis) : 확증적 데이터 분석
#     - 통계적 데이터 검증
#     - 가설 설정 단계
# 4. PDA(Predictive Data Analysis) : 예측적 데이터 분석
#     - 모델을 통해 새로운 데이터가 들어왔을 때 예측 수행

# y = ax1 + bx2 + cx3 + d (y:몸무게 / x: x1(키), x2(나이), x3(성별))

# 선형회귀분석, 로지스틱회귀분석 -> 전통통계방식 /
# 랜덤포레스트, XG부스트 등 -> 머신러닝

# +
# 이항분포
from scipy import stats

n = 3
for i in range(n+1):
    prop = stats.binom.pmf(k=i,n=n,p=0.4)
    print("P(X={0})={1:.3f}".format(i,prop))
# -

# # 1 서울시 종합병원 분포

# 데이터 출저 : https://data.go.kr

# +
# 라이브러리 호출
import pandas as pd
import numpy as np

# 시각화
import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns

# 시각화 폰트 설정
plt.rc('font',family='Malgun Gothic')
plt.rc('axes',unicode_minus=False)
# -

df = pd.read_csv('data/data/소상공인시장진흥공단_상가업소정보_의료기관_201909.csv', low_memory=False)
print(df.shape)
df.head()

df.info()

# 결측치 데이터
df.isnull().sum()

# 결측치 Barplot 확인
null_count = df.isnull().sum()
null_count.plot.barh(figsize = (5,8))

df_null_count = null_count.reset_index()
df_null_count.columns = ['컬럼명','결측치 수']
df_null_count.head()

# 결측치가 많은 상위 10개 컬럼
df_null_count_top = df_null_count.sort_values(by = '결측치 수', ascending = False).head(10)
df_null_count_top

df['지점명'].head()  # NaN : Not a Number

# 결측치가 많은 상위 10개 컬럼 제거
drop_columns = df_null_count_top['컬럼명'].tolist()

drop_columns

print(df.shape)
df = df.drop(drop_columns, axis = 1)  # axis = 1(열), axis = 0(행)
print(df.shape)

# describe() 요약 통계량 확인
df.describe()

df.describe(include = 'object')

df['상권업종중분류명'].unique()

df['상권업종소분류명'].nunique()

df['시도명'].unique()

city = df['시도명'].value_counts()
city.plot.barh(figsize = (8,5))

# seaborn 라이브러리
sns.countplot(data = df, y='시도명')
plt.show()

# 상권업종중분류명 빈도수 시각화
typeByName = df['상권업종중분류명'].value_counts()
typeByName.plot.barh(figsize=(5,4), grid=True)

sns.countplot(data = df, y='상권업종중분류명')
plt.show()

# +
# 데이터 색인하기
# 상권업종중분류명이 "약국/한약방" 데이터를 추출

df_medical = df[df['상권업종중분류명']=='약국/한약방']
df_medical.head()
# -

# 여러 조건으로 색인하기 - 상원업종소분류명이 약국, 시도명이 서울시
df_seoul_drug = df[(df['상권업종소분류명']=='약국')&(df['시도명']=='서울특별시')]  # 논리 연산자 : &(and) |(or)
print(df_seoul_drug.shape)
df_seoul_drug.head()

df_seoul_hospital = df[(df['시도명']=='서울특별시') & (df['상권업종소분류명']=='종합병원')]
df_seoul_hospital

df_seoul_hospital['상호명']

# 텍스트에서 데이터 색인
df_seoul_hospital.loc[~df_seoul_hospital['상호명'].str.contains('종합병원'),'상호명'].unique()  # ~ : 제외

# 꽃배달
df_seoul_hospital.loc[df_seoul_hospital['상호명'].str.contains('꽃배달')]

# 의료기
df_seoul_hospital.loc[df_seoul_hospital['상호명'].str.contains('의료기')]

# +
# 꽃배달, 의료기, 장례식장, 상담소, 어린이집은 종합병원과 무관 -> 전처리 필요
# 제거할 데이터들의 인덱스 -> drop_row에 담고 list 형태 반환
# -

drop_row1 = df_seoul_hospital.loc[df_seoul_hospital['상호명'].str.contains('의료기|꽃배달|장례식장|상담소|어린이집')].index.tolist()
drop_row1

# 의원으로 끝나는 데이터들도 종합 병원으로 볼 수 없음 -> 해당 데이터들 인덱스를 drop_row2
drop_row2 = df_seoul_hospital.loc[df_seoul_hospital['상호명'].str.contains('의원')].index.tolist()
drop_row2

drop_row = drop_row1 + drop_row2
len(drop_row)

print(df_seoul_hospital.shape)
df_seoul_hospital = df_seoul_hospital.drop(drop_row, axis=0)
print(df_seoul_hospital.shape)

# 서울시 종합병원 분포
plt.figure(figsize=(15,4))
sns.countplot(data=df_seoul_hospital,x='시군구명',order=df_seoul_hospital['시군구명'].value_counts().index)

df_seoul_hospital.columns

plt.figure(figsize=(12,12))
sns.scatterplot(data =  df, x = '경도', y = '위도')

# !pip install folium

# +
import folium

folium.Map()
# -

# 경기도 종합병원 분포
df_ggd_hospital = df[(df['시도명']=='경기도') & (df['상권업종소분류명']=='종합병원')]
df_ggd_hospital

drop_ggd_row = df_ggd_hospital.loc[df_ggd_hospital['상호명'].str.contains('의료기|꽃배달|장례식장|상담소|어린이집|의원')].index.tolist()
len(drop_ggd_row)

print(df_ggd_hospital.shape)
df_ggd_hospital = df_ggd_hospital.drop(drop_ggd_row, axis=0)
print(df_ggd_hospital.shape)

# 경기도 종합병원 분포
plt.figure(figsize=(4,15))
sns.countplot(data=df_ggd_hospital,y='시군구명',order=df_ggd_hospital['시군구명'].value_counts().index)

df_ggd_hospital.head()

map = folium.Map(location=[df_ggd_hospital['위도'].mean(),df_ggd_hospital['경도'].mean()],zoom_start=10)
# map

df_ggd_hospital.위도.iloc[0]
df_ggd_hospital.head()

# +
from folium import Marker
from folium.plugins import MarkerCluster

for i in range(0,len(df_ggd_hospital)):
    Marker([df_ggd_hospital.위도.iloc[i],df_ggd_hospital.경도.iloc[i]],
           popup=df_ggd_hospital.상호명.iloc[i]).add_to(map)

map

# +
seoul_map = folium.Map(location=[df_seoul_hospital['위도'].mean(),df_seoul_hospital['경도'].mean()])

for n in df_seoul_hospital.index:
    name=df_seoul_hospital.loc[n,'상호명']
    address = df_seoul_hospital.loc[n,'도로명주소']
    popup = f"{name}-{address}"
    location = [df_seoul_hospital.loc[n,'위도'],df_seoul_hospital.loc[n,'경도']]
    folium.Marker(location=location,popup=popup).add_to(seoul_map)
    
seoul_map
