import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import trim_mean

def median_absolute_deviation(data):
    """
    [중앙값의 절대 편차(Median Absolute Deviation, MAD) 계산]

    - MAD는 이상치에 민감하지 않고, 데이터의 퍼짐 정도를 측정
    - mean, std가 이상치에 영향을 크게 받는 경우 유용
    """
    median_value = np.median(data)
    mad_value = np.median(np.abs(data - median_value))
    return mad_value

def trimmed_mean(data, proportiontocut=0.1):
    """
    [절사평균 계산]
    - 일정 비율(proportiontocut)로  데이터의 양 끝을 제외하고 남은 값들의 평균을 계산
    """
    trimmed_mean_value = trim_mean(data, proportiontocut=proportiontocut)
    return trimmed_mean_value

def log_mean(data):
    """
    [로그평균 계산]
    - 데이터가 비대칭적이거나 분포가 왜곡(= 특히, 큰 값들이 존재하는 경우)될 경우 사용
    
    - 주로 양수로 이루어진 데이터에서 활용
    - 양수 분포를 로그 분포로 가져오면서 정규분포에 가깝게 만들어줌
    
    - 데이터의 상대적 크기 차이(이상치에 대한 값의 영향)을 줄여줌 -> 분산 줄임
    
    - 비선형적인 변화 존재 시, 보정에 사용
    - ex. 지수적으로 증가(Y = a * exp(bX)) ->선형적인 관계로 변환(log(Y) = log(a) + bX)
    
    - ex. 금융 데이터(수익률, 주가 등 큰 편향을 가진 데이터가 많음)
    - ex. 생물학적 데이터(세포 성장률, 유전자 발현량 등 주로 사용)
    - ex. 마케팅 및 판매 데이터(판매수익, 고객 수 등)
    """
    log_data = np.log1p(data)  # 0이나 음수가 아닌 값을 가지는 데이터에 대해 로그를 취함
    log_mean_value = np.mean(log_data)
    return log_mean_value

# Load the 'tips' dataset in Seaborn
tips_data = sns.load_dataset('tips')

# Visualization
sns.histplot(tips_data['total_bill'], bins='auto', kde=True)
plt.title('Distribution of Total Bill Amounts')
plt.xlabel('Total Bill Amount')
plt.ylabel('Frequency')
plt.show()


tips_data = tips_data['total_bill']
# Calculate each metric
mean_value = np.mean(tips_data)
median_value = np.median(tips_data)
mad_value = median_absolute_deviation(tips_data)
trimmed_mean_value = trimmed_mean(tips_data)
log_mean_value = log_mean(tips_data)

# Results ------------
print(f"Original Mean: {mean_value}")
print(f"Median: {median_value}")
print(f"MAD: {mad_value}")
print(f"Trimmed Mean: {trimmed_mean_value}")
print(f"Log Mean: {log_mean_value}")

