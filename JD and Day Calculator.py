import math
import numpy as np

K = int(input('년도를 입력하세요: '))
M = int(input('월을 입력하세요: '))
I = int(input('일을 입력하세요: '))
UT = float(input('시간을 UT로 입력하세요: '))


# N = 날짜 세기
N = math.floor((275*M)/9) - math.floor((M+9)/12)* (1+math.floor((K-4*math.floor(K/4)+2)/3)) + I -30

# JD = 율리우스 적일 계산
JD = 367*K - math.floor(7*(K+math.floor((M+9)/12))/4) + math.floor((275*M)/9) + I + 1721013.5 + (UT/24) - (0.5 * np.sign(100*K + M -190002.5)) + 0.5

print("그 해의 날 수 :", N)
print("율리우스 적일 :", JD)