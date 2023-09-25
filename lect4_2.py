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

#모듈화
""" import mod.utils as mu

print(mu.rd_int(1, 100))

my_list = ["apple", "banana", "cherry"]
print(mu.rd_list(my_list))

print(mu.rd_rd())

print(mu.rd_nv) """


#-------------datetime--------------
#from datetime import datetime as dt

#현재 시간 출력
#print(dt.now())

#특정 시간대의 현재 시간 출력
""" import timezone
tz = timezone('UTC')
print("timezon : ",dt.now(tz)) """

#문자열을 날짜로 변환
""" date_string = '2021-07-08'
date_object = dt.strptime(date_string, "%Y-%m-%d")
print(date_object)
 """
#날짜를 문자열로 변환
""" date_object = dt.now()
date_string = date_object.strftime('%Y-%m-%d')
print(date_string) """


#
""" import mod.utils as mu
#현재 시간 출력
dtnow = mu.get_dtnow()
print(dtnow)

#문자열을 날짜로 변환
ret = mu.cvt_time2str("2023-09-25")
print(ret)

#날짜를 문자열로 변환
res = mu.cvt_str2time()
print(res) """

#-------------os--------------
""" import os
#현재 작업 디렉토리 출력
print(os.getcwd())

#디렉토리 변경
os.chdir('../') #상위 폴더로 올라감(== cd../)

#변경된 디렉토리 출력
print(os.getcwd())

#파일 목록 출력
print(os.listdir())


#디렉토리 삭제
os.rmdir('new_directory')
print(os.listdir())

#디렉토리 생성
os.mkdir('new_directory')
print(os.listdir())
 """
 
#
""" import os
import mod.utils as mu
 
os.chdir('../') 

print(mu.get_curdir())
 
mu.os_mkdir('pypypypy')
print(os.listdir())

os.rmdir('pypypypy')
print(os.listdir()) """

#----------------sys-----------------
""" import sys

print(sys.version)
print(sys.argv) """

#-------------서드파티 모듈--------------









