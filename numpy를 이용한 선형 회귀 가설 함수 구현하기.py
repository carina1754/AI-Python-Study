import numpy as np

def prediction(theta_0, theta_1, x):
    """주어진 학습 데이터 벡터 x에 대해서 예측 값을 리턴하는 함수"""
    return theta_0 + theta_1 * x


# 테스트 코드

# 입력 변수(집 크기) 초기화 (모든 집 평수 데이터를 1/10 크기로 줄임)
house_size = np.array([0.9, 1.4, 2, 2.1, 2.6, 3.3, 3.35, 3.9, 4.4, 4.7, 5.2, 5.75, 6.7, 6.9])
theta_0 = -3
theta_1 = 2

prediction(theta_0, theta_1, house_size)