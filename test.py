#-----------------집합-----------------
#생성
""" my_set = set([5,8,3,7,1,"h"]) #순서대로 정렬되어 출력됨
print(my_set)

set_tmp = set("hello")
print(set_tmp) """

#합집합
""" my_set = {5,8,3,7,1,"h"}
set_item = {7,8,4,2,"h"}
#print(my_set | set_item)

print(my_set.union(set_item)) # == my_set | set_item
 """
#차집합
""" my_set = {5,8,3,7,1,"h"}
set_item = {7,8,4,2,"h"}
#print(my_set | set_item)#합
print(my_set - set_item)#차
print(my_set.difference(set_item)) #== my_set - set_item
 """
#교집합
""" my_set = {5,8,3,7,1,"h"}
set_item = {7,8,4,2,"h"}

print(my_set | set_item)
print(my_set & set_item)
print(my_set.intersection(set_item)) #== my_set & set_item
 """
#추가
""" my_set = {5,8,3,7,1,"h"}
print(my_set)
my_set.add(9)
print(my_set)

my_set = {5,8,3,7,1,"h"}
print(my_set)
my_set.update([5,8,7,4]) #중복 안 되는 거 업뎃
print(my_set)
 """
#삭제
""" my_set = {5,8,3,7,1,"h"}
print(my_set)
my_set.clear()

my_set = {5,8,3,7,1,"h"}
print(my_set)
my_set.remove(5) #없는 요소를 삭제하면 프로그램 다운(error)
print(my_set)

my_set = {5,8,3,7,1,"h"}
print(my_set)
my_set.discard(2) #없는 요소를 삭제하면 무시
print(my_set)

my_set = {5,8,3,7,1,"h"}
set_item = {7,8,4,2,"h"}

print(my_set)

my_set.difference_update(set_item) #공통요소 삭제
print(my_set) """

#-----------------타입 변환-----------------
""" my_int = 10
my_str = str(my_int) #my_int 타입이 int >> string 변환

#1
my_int = 10
print(my_int)
print(my_str)

#2
my_int = 10
print(my_int)
print(my_int+10)

#3
my_int = 10
print(my_int)
print(my_int+10)
my_str = str(my_int)
print(my_str)
#print(my_str+10) # 타입 달라서 error

#4
my_int = 10
print(my_int)
print(my_int+10)
my_str = str(my_int)
print(my_str)
print(my_str + "hello") #같은 str형이라 Error 안 남 """

#----------------------------------
""" my_str = '10'
my_int = int(my_str)

#1
my_str = '10'
print(my_str)
my_int = int(my_str)
print(my_int)

#2
my_str = '10'
print(my_str)
my_int = int(my_str)
print(my_int)
print(my_int + 10)

#3
my_str = '10'
print(my_str)
my_int = int(my_str)
print(my_int) #str >> int로 바꿨으니깐 10출력
print(my_int+10)
my_int2 = int("ten") #이렇게는 불가능
print(my_int2) 
 """
