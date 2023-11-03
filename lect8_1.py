#cls, self
""" 
class MyClass:
    count = 0

    def __init__(self, num):
        self.count = num

    @classmethod
    def clsMethod(cls):
        cls.count += 1 
        print(f"cls count = {cls.count}")

    def instMethod(self):
        self.count += 1 
        print(f"instance = {self.count}")

MyClass.clsMethod()

obj = MyClass(10)

obj.instMethod()
print(obj.count)

print(MyClass.count)
print(MyClass.count) """


""" class champion:
    lv = 1
    movSpd = 0
    basicMovSpd = 325
    atkSpd = 0.658
    
    def __init__(self, name, speed):
        self.hp = 100
        self.name = name
        self.lv = 1
        self.setSpeed(speed)
        self.setAtkSpd()
        self.setMovSpd()

    def setAtkSpd(self):
        self.atkSpd = 0.658*((1.9134)**(champion.lv - 1))
     
    def beAtk(self, dem):
        print("be attack", dem, 1-100.0/(100.0+100))   
        self.dem = dem*(100.0/(100.0+100))
        print(self.dem)
        self.hp = self.hp - self.dem
        
    def setSpeed(self, sp):
        if (sp == 1):
            self.speed = 50
        else:
            self.speed = 0
            
    def setMovSpd(self):
        print("set Mov Spd")
        self.movSpd = (20 + self.speed)*(1.09)*(100)
        
    def printStatus(self):
        print("champion: %s, hp: %f, lv: %d, movSpd:%f, atkSpd: %f"%(self.name,self.hp,self.lv,self.atkSpd, self.atkSpd))

ash = champion("ash",140)
mipo = champion("mipo",220)

ash.printStatus()
mipo.printStatus()

mipo.beAtk(63.0)
mipo.printStatus() """


#상속, 부모-자식 클래스
""" class Champion :
    def __init__(self, name) :
        self.name = name
        self.level = 1

class Yasuo(Champion) :
    def getName(self) :
        print(self.name)
        
    def attck(self, key) :
        print(f"attack = {key}")
    
    def levelup(self) :
        self.level += 1
    
    def getLevel(self) :
        print(self.name, self.level)
        
class Garem(Champion):
    def getName(self) :
        print(self.name)
        
    def attck(self, key) :
        print(f"attack = {key}")
    
    def levelup(self) :
        self.level += 1
    
    def getLevel(self) :
        print(self.name,self.level)
        

user1 = Yasuo("python")
user2 = Garem("hello")

user1.getName()
user1.getLevel()
user1.attck(5)

user2.getName()
user2.getLevel()
user2.levelup()
user2.getLevel() """


""" class Champion :
    def __init__(self, name) :
        self.name = name
        self.level = 1
    
    def attck(self, key) :
        print(f"attack = {key}")
    
    def levelup(self) :
        self.level += 1
    
    def getLevel(self) :
        print(self.level)


class Yasuo(Champion) :
    def attck(self, key):
        print(f"attack - {key} steel tempest")
        return


class Garen(Champion) :
    def attck(self, key):
        print(f"attack - {key} demacian justice")
        return
    
user1 = Yasuo("python")
user2 = Garen("hello")

user1.getLevel()
user2.getLevel()

user1.attck("q")
user2.attck("r")
    
user1.levelup()
user2.levelup()

user1.getLevel()
user2.getLevel() """


#추상화
""" from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


circ = Circle(5)
rect = Rectangle(4, 6)

#각각 출력
print(circ.area())
print(rect.area())

#for문으로 출력 
sett = [circ,rect]
for st in sett :
    print(st.area()) """
    
#정보은닉
""" class Person:
    def __init__(self, name, age, num):
        self._name = name
        self._age = age
        self._number = num

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    def number(self):
        return self._number

    @name.setter
    def name(self, new):
        self._number = new

    @age.setter
    def age(self, nAge):
        self._age = nAge
        
user1 = Person("Alice", 30, "01088882221")
print(user1.age)
print(user1._age)
print(user1.name)
print(user1._name)
print(user1.number)
print(user1._number)

user1._age = 21
user1.age = 23
print(user1.age) """

#다형성
"""class Person :
    def __init__(self, name, age, num) :
        self.name = name
        self.age = age
        self.number = num
    
    def getName(self) :
        return self.name
    
    def getAge(self) :
        return self.age
    
    def getNumber(self) :
        return self.number

class Student(Person) : ()

class Teacher(Person) : ()

def getPersonName(person) :
    return person.getName()

user1 = Student("park",20,"01022229999")
user2 = Student("Kim",24,"01077774444")

print(getPersonName(user1))
print(getPersonName(user2)) """

#캡슐화
""" class Person : 
    def __init__(self, name, age, num) :
        self.name = name
        self.age = age
        self.number = num
  
    def getName(self) :
        return self.name
    
    def setName(self, new) :
        self.name = new
        return 
    
    def getNumber(self) :
        return self.number
    
    def setNumber(self, newNum) :
        self.number = newNum
        return 

p1 = Person("park",20,"01083332222")
p2 = Person("kim",24,"01022229999")

print(p1.getName())
print(p2.getName())
print(p1.getNumber())
print(p2.getNumber())

p1.setName("A")
p2.setName("B")

p1.setNumber("11111111111")
p1.setNumber("22222222222")

print(p1.getName())
print(p2.getName())
print(p1.getNumber())
print(p2.getNumber()) """

#==========================================================================
##1103수업   << 오류 수정
""" import mod.calc as cm

cl = cm.Calc()

print(cl.add(1,2)) """


##텍스트 줄이기
""" import textwrap as tw

target = "To be or not to be, That is a question!"
res = tw.shorten(target, width=20)

print(res) """

##줄바꿈 처리
""" import textwrap as tw

target = "To be or not to be, That is a question!"
longTarget = target * 100

print(longTarget)
print("\n========================================\n")

res = tw.wrap(longTarget, width=50)
print(res)
## 원본과 차이 >> 타입이 list로 변경

print("\n========================================\n")
#join() 함수
print('\n'.join(res))
##list가 for문을 돌면서 \n을 넣음

print("\n========================================\n")
#fill() 함수
rs = tw.fill(longTarget,width=50)
print(rs)
#두단계를 한번에 수행함 """


##문자열 치환
""" line = "홍길동의 주민번호는 012345-1234567 입니다. "
word_result = []
for word in line.split(" "):
    if len(word) == 14 and word[:6].isdigit() and word[7:].isdigit():
            word = word[:6] + "-" + "*******"
    word_result.append(word)
print(" ".join(word_result)) """


##정규표현식
""" import re
line = "홍길동의 주민번호는 012345-1234567 입니다. "
res = re.compile("(\d{6})[-]\d{7}")
print(res.sub("\g<1>-*******", line)) """


##날짜처리
""" import datetime as dt

day1 = dt.date(2023, 11, 3)
print(day1)

day2 = dt.date(2003, 1, 23)
print(day2)

#날짜계산
diff = day1 - day2
print(diff) """


#날짜 객체1
""" import datetime as dt

res = dt.datetime(2023, 11, 1, 12, 30, 40)
tHour = res.hour
tMin = res.minute
tSec = res.second

print(res, tHour, " ", tMin, " ",tSec) """


#날짜 객체2
""" import datetime as dt

day = dt.date(2023, 11, 1)
time = dt.time(12, 30, 40)
res = dt.datetime.combine(day, time)

print(res, res.hour, res.minute)
 """
 
 
#요일 판별
""" import datetime as dt

day = dt.date(2023, 11, 1)
print(day.weekday()) # 0 - Mon ~~ 6 - Sun

yesterday = dt.date(2023,10,31)
print(yesterday.weekday()) """


#날짜 계산
""" import datetime as dt
today = dt.date.today()
print(today)

difday = dt.timedelta(days = 50)
#difday = dt.timedelta(hours = 200)
#difday = dt.timedelta(minutes = 2000)

print(difday)
print(today + difday) """


#단어 세기
""" import collections as cl
import re

poem = '''
내가 그의 이름을 불러 주기 전에는
그는 다만
하나의 몸짓에 지나지 않았다.
내가 그의 이름을 불러 주었을 때
그는 나에게로 와서
꽃이 되었다.
내가 그의 이름을 불러 준 것처럼
나의 이 빛깔과 향기에 알맞은
누가 나의 이름을 불러 다오.
그에게로 가서 나도
그의 꽃이 되고 싶다.
우리들은 모두
무엇이 되고 싶다.
너는 나에게 나는 너에게
잊혀지지 않는 하나의 눈짓이 되고 싶다.'''

wd = re.findall(r"\w+", poem)
print(wd)
print(len(wd))

cnt = cl.Counter(wd)
print(cnt.most_common(1)) #가장 많이 사용된 단어 & 사용횟수 출력
#print(cnt.most_common(2)) #2번째로 가장 많이 사용된 단어 출력 """


#정렬 출력
""" import pprint

data = {"month": "9", "num": 642, "link": "", "year": "2009", "news": "", "safe_title": "Creepy", "transcript": "[[Two people are sitting on chairs.]]\nMan: Hey, cute netbook.\nWoman: \nWhat.\n\n\nMan: Your laptop. I just --\nWoman: No, why are you talking to me.\n\nWoman: Who do you think you are? If I were even slightly interested, I'd have shown it.\n\nWoman: Hey everyone, this dude's hitting on me.\nVoice #1: Haha\nVoice #2: Creepy\nVoice #3: Let's get his picture for Facebook to warn others.\n\n((This panel fades into a thought bubble of the actual man.))\n[[The girl is typing on her laptop.]]\nDear blog,\nCute boy on train still ignoring me.\n\n{{Title text: And I even got out my adorable new netbook!}}", "alt": "And I even got out my adorable new netbook!", "img": "https://imgs.xkcd.com/comics/creepy.png", "title": "Creepy", "day": "28"}
pprint.pprint(data) """


#최대공약수
""" import math

res = math.gcd(60, 100, 80)
print(res)

#최소공배수
res2 = math.lcm(15, 25)
print(res2) """


#로또 번호 생성
""" import random

res = []
while len(res) < 6:
    num = random.randint(1, 45)
    if num not in res:
        res.append(num)

print(res) """


#통계
""" import statistics as st

#평균값
data = [48, 92, 57, 59, 63, 83, 56, 91, 82, 74, 63, 72]
res = st.mean(data)
print(res)

#중간값
res = st.median(data)
print(res) """


#압축
""" import zlib

data = "To be or not to be, That is a question!"
longData = data * 1000

print(len(longData))
print("\n======================================\n")

cmp = zlib.compress(longData.encode(encoding="utf-8"))
print(cmp)
print("\n======================================\n")
print(len(cmp))

#압축해제
decmp = zlib.decompress(cmp).decode("utf-8")
print(decmp)

print("\n======================================\n")
print(len(decmp)) """


#파일 압축 저장
""" import gzip

data = "To be or not to be, That is a question!" * 10000
print(len(data))

with gzip.open('data.txt.gz', 'wb') as fp:
    fp.write(data.encode('utf-8'))
    
#압축 읽기
with gzip.open('data.txt.gz', 'rb') as fp:
    read_data = fp.read().decode('utf-8')
    print(read_data) """
    
    
#압축 bz2
""" import bz2

data = "To be or not to be, That is a question!" * 10000
cmp = bz2.compress(data.encode(encoding="utf-8"))

print(cmp)
print("\n==============================\n")
print(len(cmp))

decmp = bz2.decompress(cmp).decode("utf-8")
print(decmp)
print("\n==============================\n")
print(len(decmp)) """

    
#파일 압축하기
import zipfile as zf
""" 
data = "To be or not to be, That is a question!" * 10000
fp1 = open("a.txt","w")
fp1.write(data)
fp1.close()

fp2 = open("b.txt","w")
fp2.write(data)
fp2.close()

fp3 = open("c.txt","w")
fp3.write(data)
fp3.close()

with zf.ZipFile('txt.zip', 'w') as myzip:
    myzip.write('a.txt')
    myzip.write('b.txt')
    myzip.write('c.txt') """
    
""" with zf.ZipFile('txt.zip') as myzip:
    myzip.extractall() """
    
#tar 파일 압축
import tarfile

""" data = "To be or not to be, That is a question!" * 10000
fp1 = open("atar.txt","w")
fp1.write(data)
fp1.close()

fp2 = open("btar.txt","w")
fp2.write(data)
fp2.close()

fp3 = open("ctar.txt","w")
fp3.write(data)
fp3.close()

with tarfile.open('txt.tar', 'w') as mytar:
    mytar.add('atar.txt')
    mytar.add('btar.txt')
    mytar.add('ctar.txt') """
    
""" with tarfile.open('txt.tar') as mytar:
    mytar.extractall() """
    

#실행 아규먼트
""" import argparse
import functools

parser = argparse.ArgumentParser()
parser.add_argument('-a', '--add', type=int, nargs='+', metavar='N', help='더할 숫자')
parser.add_argument('-m', '--mul', type=int, nargs='+', metavar='N', help='곱할 숫자')
parser.add_argument('-s', '--sub', type=int, nargs='+', metavar='N', help='곱할 숫자')

args = parser.parse_args()

if args.add:
    print("총합 %d입니다." % functools.reduce(lambda x, y: x + y, args.add))
if args.mul:
    print("총곱 %d입니다." % functools.reduce(lambda x, y: x * y, args.mul))
if args.mul:
    print("결과 %d입니다." % functools.reduce(lambda x, y: x - y, args.sub)) """