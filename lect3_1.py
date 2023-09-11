#-----------------연산자-----------------
#산술연산자

#사칙연산
""" a = 10
b = 3
print(a + b)    
print(a - b)    
print(a * b)    
print(a / b)    
print(a % b)    
print(a // b)   
print(a ** b)    """

#할당 연산자 , 연산자 축약
""" a=0
print(a)

a+=2
print(a)

a-=1
print(a)

a*=4
print(a)

a/=2
print(a)

a**=3
print(a) """

#비교,관계 연산자
""" a=10
b=4
print(a > b)    
print(a < b)    
print(a >= b)   
print(a <= b)   
print(a == b)   
print(a != b)   """

#논리 연산자
""" a=1
b=0

print(a and b)  #둘 다 1이어야 1 
print(a or b)   #한쪽이 1이면 무조건 1
print(not a)    #1010 >> 0101 (반대로 됨)
print(not b)   

x = True
y = False

print(x and y)  # 둘 다 t나 f면 True, 하나라도 다르면 False
print(x or y)   # 하나라도 t면 True
print(not x)    
print(not y)    """ 

#비트연산자
""" a=10
b=3

print(a & b)   
print(a | b)   
print(a ^ b)   
print(~a)      
print(a << 2) #2번 자리 옮기기 (노션 교재 참고하기) """

#멤버 연산자
""" my_list = [9, 4, 3, 7, 8, 'hi']
print(4 in my_list)

print(2 in my_list)

print(2 not in my_list)

my_dic = {"key1" : "v1", "k2" : "v2"}
print("k2" in my_dic) """

#식별 연산
""" x = [1, 2, 3]
y = [1, 2, 3]
z = x

print(x is y)  #주소가 다르기 때문에 false == 서로 다른 객체
print(x is z)  #x,y는 같은 객체이기 때문에 true
print(x is not y)   """



