import numpy as np

def prediction(theta_0, theta_1, x):
    """주어진 학습 데이터 벡터 x에 대해서 모든 예측 값을 벡터로 리턴하는 함수"""
    return theta_0 + theta_1 * x
    

def prediction_difference(theta_0, theta_1, x, y):
    """모든 예측 값들과 목표 변수들의 오차를 벡터로 리턴해주는 함수"""
    return prediction(theta_0, theta_1, x) - y
    
    
# 입력 변수(집 크기) 초기화 (모든 집 평수 데이터를 1/10 크기로 줄임)
house_size = np.array([0.9, 1.4, 2, 2.1, 2.6, 3.3, 3.35, 3.9, 4.4, 4.7, 5.2, 5.75, 6.7, 6.9])

# 목표 변수(집 가격) 초기화 (모든 집 값 데이터를 1/10 크기로 줄임)
house_price = np.array([0.3, 0.75, 0.45, 1.1, 1.45, 0.9, 1.8, 0.9, 1.5, 2.2, 1.75, 2.3, 2.49, 2.6])

theta_0 = -3
theta_1 = 2

prediction_difference(-3, 2, house_size, house_price)