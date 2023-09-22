#input
""" num = input("숫자를 입력하세요!!")
print("number ",num) #int가 아니라 string형으로 입력 받아 출력함
print("number ", int(num)) #string으로 받은 걸 int형으로 바꿔 출력해줌
 """
 
#type
""" a = 12
print(type(a)) #a가 무슨 타입인지 출력

a = 12.012
print(type(a))

a = "a"
print(type(a))

a = "abcd"
print(type(a))

a = [1,4,5]
print(type(a)) """

#형변환
""" a = 65
#a = '65'
print(int(a))
print(str(a))
print(hex(a))
print(oct(a))
print(chr(a)) #아스키코드 65) A
print(ord("A")) """

#거듭제곱 pow
""" print(pow(2,2))
print(pow(2,6))
print(pow(3,4))
 """
#divmod 몫,나머지 반환
#print(divmod(10,3)) >>(3,1)

#반올림 round
# print(round(3.14))

#리스트, 튜플 반환
""" a=(3,5,7)
b=list(a)
c=tuple(b)

print(type(a)) #>>()
print(type(b)) #>>[]
print(type(c)) #>>() """

#range
""" for i in range(2,7):
    print(i)
    
for i in range(6):
    print(i)
    
for i in range(1,20,3):
    print(i) """
    
#max, min, sum
""" a = [3, 5, 6, 9]
print(max(a))
print(min(a))
print(sum(a)) """

#abs
""" print(abs(-3))
print(abs(3.0))
print(abs(-3.0)) """

#sorted
""" a = [5,3,1,9,4]
print(sorted(a)) #오름차순 정렬
print(sorted(a,reverse=True)) #내림차순 정렬 """

#enumereate
""" a = [5, 3.14, False, 9, "string"]
print(enumerate(a)) #a의 객체에 대한 주소만 출력
print(*enumerate(a)) #a내 요소 인덱스와 값 반환 """

#zip
""" a = [1,2,3]
b = [4,5,6]
print(*zip(a,b)) #짝지어서 출력 >> (1, 4) (2, 5) (3, 6)
 """
 
#any(==or), all(==and)
""" a=[True, True, False]
b=[True,True,True]
print(any(a))
print(all(a))
print(all(b)) """

#format
""" a = 20
b = 23
c = "a는 {}, b는 {}".format(a,b)
print(c) """

#globals(전역>>보안 취약), locals(지역)
#a = 3
""" print(globals()) 
print(locals())  """

#dir
#print(dir(a))

#callable
#print(callable(a))

#람다 함수
""" add = lambda a, b : a + b
sub = lambda a, b : a - b
mul = lambda a, b : a * b
div = lambda a, b : a / b
print(add(2, 3))
print(sub(2, 3))
print(mul(2, 3))
print(div(2, 3)) """

#사용자 정의 함수
from argparse import REMAINDER


def add_numbers(x, y):
    return x + y

# 함수 호출
""" result = add_numbers(4, 5)
print(result)
 """

""" def greet(name):
    print("Hello, " + name + ". How are you?")

greet('주현')

# name = input("이름 입력 ")
# result = greet(name) """


""" def add(a, b) : 
	print(a + b)

def sub(a, b) :
	return a - b

def mul() :
	return 2 * 4

def div() :
	print(4 / 2)

add(3, 5)
print(sub(3, 5))
print(mul())
div() """

#1
""" def one(n):
    if(n%2==0):
        return "짝수"
    else:
        return "홀수"
    
num = input("정수를 입력해주세요: ")
result=one(int(num))
print(result) """

#2
""" def two(m):
    return m[::-1]
    
msg = input("문자열을 입력하세요: ")
print(two(msg))     """

#3
# 이게 더 좋은 구조 >> 한 함수에서는 한 역할만 하는게 좋음
""" def add(a,b):
    return a + b

def sub(a,b):
    return a - b
    
def mul(a,b):
    return a*b

def div(a,b):
    return a/b

a = int(input("a 입력: "))
b = int(input("b 입력: "))

print("더하기: ", add(a,b))
print("빼기: ", sub(a,b))
print("곱하기: ", mul(a,b))
print("나누기: ", div(a,b)) """

#
""" def cals(a,b):
    print(a+b)
    print(a-b)
    print(a*b)
    print(a/b)
    
a = int(input("a 입력: "))
b = int(input("b 입력: "))
cals(a,b) """

#4
""" def sums(n):
    return sum(n)
    
nums = []

for i in range(5): #list nums에 값 넣기
    n= int(input(f"{i+1}번째 숫자 입력: "))
    nums.append(n)

print(sums(nums)) """


#0922 수업

#콜백 함수
""" def prt_func(n) :
     print("hello",n)
    

def callfunc(fx) :
    for i in range(0,5):
        fx(i)

callfunc(prt_func) """

#타입 힌트
""" list = []

def update_msg(name:str) -> list:
    msg = []
    msg.append("Hello, " + name)
    msg.append("Bye, " + name)
    return msg

def greeting(in_name: str) -> list:
    gt_msg = None
    gt_msg = update_msg(in_name)
    return gt_msg 

res = greeting("python")

for message in res:
    print(message) """
    
#재귀함수
""" def fun(n) :
    if n == 5 :
        return
    
    print(1, n)
    fun(n+1)
    
fun(1) """

""" def ploop(n) :
    if n == 0 :
        print("end")
        return 1
    else: 
        print(n,n-1,"=",n+n-1)
        return n * ploop(n-1)
 
print(ploop(3)) """

#피보나치 수열
""" def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        print(n)
        return fibonacci(n-1) + fibonacci(n-2)
    
res = fibonacci(4)
print("res = ", res) """