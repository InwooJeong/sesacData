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

# # 결측치, Scaler
#
# - 분석에 필요한 데이터 구성
# - 결측치 확인 및 처리 - 범주형/ 연속형
# - 이상치 확인 및 처리
# - 연속형 변수 Scale 변환 - scale/ minmax/ robust

import pandas as pd
import numpy as np
from sklearn.preprocessing import scale, minmax_scale, robust_scale

# 시각화 환경 설정
import matplotlib as mp
mp.rc('font',family='Malgun Gothic')
mp.rc('axes',unicode_minus=False)

# +
df_raw = pd.read_csv('data/data/health_결측.csv' ,encoding = 'euc-kr')

df_raw.head()
# -

# 결측치 확인
df_raw.isnull().head()

# 결측치(True) 현황 요약
df_raw.isnull().sum()

df_raw["GENDER"].value_counts()

# 범주형(문자) 변수 격측치 처리 : Gender 변수 결측치에 여성
df_raw["GENDER"].fillna("여성",inplace=True)
df_raw.head()

# 연속형(숫자) 변수 결측치 처리 : GENDER별 WEIGHT 평균 계싼
df_raw.groupby("GENDER")["WEIGHT"].agg("mean")

pd.pivot_table(data=df_raw,index='GENDER',values='WEIGHT',aggfunc=np.mean)

# 연속형(숫자) 변수 결측치 처리 : WEIGHT 변수 결측치를 성별 평균으로 - transform('집계함수')
df_raw["WEIGHT"] = \
    df_raw["WEIGHT"].fillna(df_raw.groupby("GENDER")["WEIGHT"].transform("mean")).round(3)
df_raw.head()

# +
# 이상치 확인 및 처리 : 상자 수염도표를 이용한 이상치 확인
# boxplot: 상자수염도, figsize: 그래프 크기(x,y)
df_raw.boxplot(figsize=(10,4))

import matplotlib.pyplot as plt
plt.show()
# RSTPULSE 변수에 이상치!
# -

# 이상치 확인 및 처리 : 조건에 해당하는 자료 직접 확인
df_raw[(df_raw["RSTPULSE"]>=100)]

# 이상치 확인 및 처리 : 이상치 제거
# RSTPULSE 변수에서 이상치 제외(100 이하만 보관)
df_fitness = df_raw[df_raw["RSTPULSE"]<100]
df_fitness

# 자료 index reset : index 번호 재부여
df_fitness.reset_index(drop = True, inplace = True)
df_fitness

df_fitness.isnull().sum()

df_fitness.head()

df_fitness.dtypes

df_fitness.describe()

# +
# Scale 변환 : scale 변환 대상 변수 = 숫자형 변수(문자형 변수는 적용 안됨)

# select_dtypes 조건으로 변수 유형 선택 : 숫자형 변수 선택 ("object" 제외)
df_fitness_num = df_fitness.select_dtypes(exclude="object")
df_fitness_num.head()
# -

# 문자형 변수 선택 : select_dtypes="object" 선택
df_fitness_char = df_fitness.select_dtypes(include="object")
df_fitness_char.head()

# +
# Scale 변환(평균, 표준편차) : 평균 = 0, 표준편차 = 1 기준 변환

# scale 변환 : 표준정규분포 기준
df_scale_std = scale(df_fitness_num)
# scale 변환하면 numpy의 행렬 형태로 저장 -> DataFrame으로 변환
df_scale_std = pd.DataFrame(df_scale_std,columns = df_fitness_num.columns)
df_scale_std.head()
# -

# scale 변환 결과 확인 : 요약통계량
df_scale_desc = df_scale_std.describe()
df_scale_desc.round(3)

# +
# Scale 변환(최소-최대) : 최소 = 0, 최대 = 1 변환

# scale 변환 : 최소, 최대값 기준
df_scale_minmax = minmax_scale(df_fitness_num)

# scale 변환하면 numpy의 행렬 형태로 저장 -> DataFrame으로 변환
df_scale_minmax = pd.DataFrame(df_scale_minmax,columns=df_fitness_num.columns)
df_scale_minmax.head()
# -

# scale 변환 결과 확인 : 요약통계량
df_scale_desc = df_scale_minmax.describe()
df_scale_desc.round(3)

# +
# Scale 변환(로버스트) : 중앙값 = 0 변환(이상치 영향 감소)
# scale 변환 : 로버스트 기준
df_scale_robust = robust_scale(df_fitness_num)

#scale 변환 -> DataFrame
df_scale_robust = pd.DataFrame(df_scale_robust,columns = df_fitness_num.columns)
df_scale_robust.head()
# -

# scale 변환 결과 확인 : 요약통계량
df_scale_desc = df_scale_robust.describe()
df_scale_desc.round(3)

# Scale 변환 결과 비교 : 예시로 RSTPULSE 변수 비교
df_rstpulse = pd.DataFrame()
df_rstpulse["Raw"] = df_fitness_num["RSTPULSE"]
df_rstpulse["Standard"] = df_scale_std["RSTPULSE"]
df_rstpulse["MinMax"] = df_scale_minmax["RSTPULSE"]
df_rstpulse["Robust"] = df_scale_robust["RSTPULSE"]
df_rstpulse.head().round(3)

df_rstpulse.describe().round(3)

# pandas의 DataFramse.hist 이용
# df_rstpulse.hist(figsize=(10,5))
plt.show()
