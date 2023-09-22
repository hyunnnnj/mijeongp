import math
import random as rd

# 입력받은 수 제곱근 계산 : sqrt
def sq(n):
    return math.sqrt(n)


# 삼각함수 계산 sin * pi / 2
def sinpi():
    return math.sin(math.pi / 2)


# 자연로그 x=y, x=e^y = log(e)
def e():
    return math.log(math.e)


# 지수계산 ln(x) = y, x= e^y, x=exp(y) 즉, exp(x)
def exp(n):
    return math.exp(n)

# 파이계산 pi
def pi():
    return math.pi


#랜덤
# 1 ~ 10 랜덤으로 선택
def rd_int(x,y):
    return rd.randint(x,y)


# 리스트[apple, banana, cherry] 중 랜덤 선택
def rd_list(l):
    return rd.choice(l)


# 0.0 ~ 1.0 랜덤 실수 생성
def rd_rd():
    return rd.random()

# 정규 분포에 따르는 랜덤 실수 생성
def rd_nv():
    return rd.normalvariate(0,1)



