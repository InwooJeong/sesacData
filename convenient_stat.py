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

# +
# %matplotlib inline
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
import seaborn as sns

plt.rc('font',family='Malgun Gothic')
plt.rc('axes',unicode_minus=False)

# +
##1. csv 파일 불러오기 (convenient_store.csv)
# -

data = pd.read_csv('convenient_store.csv')
data.head(5)

# +
##2. 전체 컬럼 정보, null 값 유무 확인
# -

data.info()

data.isnull().sum()

#

# +
##3. 개수, 평균, 편차, 최소, 최대값 확인
# -

data.describe()

# +
##4. 지역에 대한 통계, 개수, 유니크한 정보, 제일 빈도가 높은 지역
# -

data['area'].describe()

# +
##5. 시간 당 급여가 6500원 이상인 지역의 편의점 정보 출력 (상위 10개만)
# -

data[data['hourly_wage'] >= 6500].head(10)

# +
##6. 시간 당 급여가 높은 순서로 정렬 (sort_value() 함수 사용, 상위 10개만 출력)
# -

data[data['hourly_wage'] >= 6500].sort_values('hourly_wage',ascending=False).head(10)

# +
##7. 영등포구에서 시간 당 급여가 6000원 이상인 편의점 검색
# -

data[(data['hourly_wage'] >= 6000)&(data['area1']=='영등포구')].sort_values('hourly_wage',ascending=False).head(10)

# +
##8. CU 편이점만 출력 (상위 10개만)
# -

data[data['name'].str.contains('CU')].head(10)

# +
##9. 지역 컬럼(location)을 추가한 다음, in Seoul 이라는 값 저장, 상위 5개 출력
# -

data['location'] = 'in Seoul'
data.head(5)

# +
##10. 6000원 이상 컬럼 추가(more_than_6000) -> True, False 값 저장 (상위 20개 출력)
# -

data['more_than_6000'] = data['hourly_wage']>=6000
data.head(20)

# +
##11. more_than_6000 컬럼에서 True인 데이터들의 평균, 개수, 편차 등의 정보 출력
# -

data[data['more_than_6000']==True].describe()


# +
##12. more_than_6000 이름의 함수를 생성하고, 6000원이상인 경우 A group, 아니면 B group을 반환하는 함수 생성
# -

def more_than_6000(x):
    if x >= 6000:
        return 'A group'
    else:
        return 'B group'


# +
##13. more_than_6000_f 컬럼 생성하고 more_than_6000 함수의 결과를 저장
# -

data['more_than_600_f'] = data['hourly_wage'].apply(more_than_6000)

# +
##14. 지금까지의 결과 상위 10개를 출력
# -

data.head(10)

# +
##15-1. more_than_6000가 True인 데이터의 지역과 시간당 급여를 가진 새로운 데이터프레임 생성(data2)
##15-2. data2 데이터를 시간당 급여 순으로 정렬 (높은순)
# -

data2 = data[data["more_than_6000"]==True][['area','hourly_wage','area1','area2']]
# data2.head()

data2.sort_values('hourly_wage',ascending=False).head(10)

##16. data2를 darta2.csv 파일로 저장
data2.to_csv("data2.csv",index=False)
data3 = pd.read_csv('data2.csv')
data3.head(10)

# +
##17. 시간당 급여를 histogram 으로 표시 (matplotlib hist() 사용)
# -

plt.hist(data.hourly_wage)
plt.show()

# +
##18. 시간당 급여를 box 차트로 표시 
# -

plt.boxplot(data.hourly_wage)
plt.show()


# +
##19. 시간당 급여를 box 차트로 표시(이름순으로)

# +
def chk_name(x):
    if x == '7/11':
        return 'Seven Eleven'
    else:
        return x

wagesByName = data.sort_values('name')[['hourly_wage','name']]
# wagesByName
wagesByName['name2'] = wagesByName['name'].apply(chk_name)
wagesByName

plt.figure(figsize = ([10,5]))
sns.boxplot(data = wagesByName, x='name2', y = 'hourly_wage')
plt.show()

# +
##19. 시간당 급여를 box 차트로 표시(지역순으로)

# +
wegesByAres = data.sort_values('area1')[['hourly_wage','area1']]

plt.figure(figsize = ([20,5]))
sns.boxplot(data = wegesByAres, x='area1', y = 'hourly_wage')
plt.show()

# +
##20. 한글 표시되게 matplotlib 지정
# -

plt.rc('font',family='Malgun Gothic')

# +
##21. 시간당 급여를 box 차트로 표시(지역순으로) <- 다시 실행
# -

plt.figure(figsize = ([20,5]))
sns.boxplot(data = wegesByAres, x='area1', y = 'hourly_wage')
plt.show()

# +
##22-1. 지역구별 box 차트(플롯) 
##22-2. 폰트 사이즈 6
# -

plt.figure(figsize = ([13,5]))
sns.boxplot(data = wegesByAres, x='area1', y = 'hourly_wage')
plt.rc('font',size=6)
#plt.pyplot.xticks(fontsize=6)
plt.show()

# +
##23-1. 지역구별 box 차트(플롯), 지역구가 세로로 표시
##23-2. 폰트 사이즈 6
# -

plt.figure(figsize = ([13,5]))
sns.boxplot(data = wegesByAres, x='hourly_wage', y = 'area1')
plt.rc('font',size=6)
plt.show()
