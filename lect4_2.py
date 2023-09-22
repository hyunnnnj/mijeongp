""" import cl
print(dir(calc)) """

""" import calc
print(calc.add(8,4))
print(calc.sub(8,4))
print(calc.mul(8,4))
print(calc.div(8,4)) """

""" import calc as cl
print(cl.add(8,4))
print(cl.sub(8,4))
print(cl.mul(8,4))
print(cl.div(8,4)) """


""" import mod.circle_mod as cm
print(cm.pi)
print(cm.cc_area(4))
print(cm.cc_len(5)) """

""" def cutstr(st, wd, idx) : 
    tmp = st.split(wd)
    res = tmp[idx]
    return res

url = "https://www.notion.so/test/4-1/a1fe5ef0df1/41f7a1aa9ec01/3a859a"
rs = cutstr(url, "/", 3)
print(rs) """

""" import mod.str_util as smod

url = "https://www.notion.so/test/4-1/a1fe5ef0df1/41f7a1aa9ec01/3a859a"
res = smod.cutstr(url, "/", 3)
print(res) """

#표준라이브러리, 내장모듈

""" import math
# 입력받은 수 제곱근 계산 : sqrt
sq_res = math.sqrt(6)
print(sq_res)

# 삼각함수 계산 sin * pi / 2
sp_res = math.sin(math.pi / 2)
print(sp_res)

# 자연로그 x=y, x=e^y = log(e)
e_res = math.log(math.e)
print(e_res)

# 지수계산 ln(x) = y, x= e^y, x=exp(y) 즉, exp(x)
exp_res = math.exp(3)
print(exp_res)

# 파이계산 pi
pi_res = math.pi
print(pi_res)

#팩토리얼
fc_res = math.factorial(4)
print(fc_res)

 """
 
""" import mod.utils as mu

res = mu.sq(7)
print(res) 

res = mu.sinpi()
print(res)

res = mu.e()
print(res)

res = mu.exp(3)
print(res)

res = mu.pi()
print(res)
 """
 
#랜덤
""" import random as rd
# 1 ~ 10 랜덤으로 선택
res = rd.randint(1, 100)
print(res)

# 리스트[apple, banana, cherry] 중 랜덤 선택
my_list = ["apple", "banana", "cherry"]
lres = rd.choice(my_list)
print(lres)

# 0.0 ~ 1.0 랜덤 실수 생성
fres = rd.random()
print(fres)

# 정규 분포에 따르는 랜덤 실수 생성
nvres = rd.normalvariate(0,1)
print(nvres) """


""" import mod.utils as mu

print(mu.rd_int(1, 100))

my_list = ["apple", "banana", "cherry"]
print(mu.rd_list(my_list))

print(mu.rd_rd())

print(mu.rd_nv) """