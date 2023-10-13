#1
""" for j in range(6,1,-1):
    print("*"*j) """
    
#2
""" for i in range(1,6):
    print("*"*i) """
    
#3
""" for i in range(1,6):
    spaces = " " * (6-i)
    stars = "*" *(2 * i-1)
    print(spaces+stars)
 """
#4
""" for i in range(6,0,-1):
    spaces = " " * (6-i)
    stars = "*" * (2*i-1)
    print(spaces + stars) """

#5*5
""" num = 0
line = []

for i in range(5):
    for j in range(5):
        num += 1
        line.append(num)
    print(line)
    line = [] """
    
#세로출력
""" line = []

for i in range(1,6):
    num = i
    for j in range(5):
        line.append(num)
        num += 5
    print(line)
    line = []
    num = 0 """

##교수님 예시
""" line = []
for i in range(1,6):
    for j in range(1,6):
        num = ((j-1)*5)+i
        line.append(num)
    print(line)
    line = [] """
   
    
#역순출
""" num = 25
line = []

for i in range(5):
    for j in range(5):
        line.append(num)
        num -= 1
    print(line)
    line = [] """

#가위바위보    
""" import random as rd

def com_choice():
    com = rd.randint(1,3)
    return com
    
def game(user_choice):
    user_choice = int(user_choice)
    pcnum = com_choice()
    print(user_choice, pcnum)
    
    if user_choice == pcnum:
        print("무승부")
    elif(
        (user_choice == 1 and pcnum == 3) or
        (user_choice == 2 and pcnum == 1) or
        (user_choice == 3 and pcnum == 2)
    ):
        print("승")
    else:
        print("패") 
    
print("1 : 가위")   
print("2 : 바위")   
print("3 : 보")   

chnum = input("1~3 숫자를 입력하세요! ")
game(chnum) """