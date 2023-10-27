""" import socket
from select import select
import sys
import time

HOST = "127.0.0.1"
#HOST = "localhost"
PORT = 8080

BUFSIZE = 1024
ADDR = (HOST,PORT)

#1.소켓 생성.
srvSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#2.주소 정보 할당
srvSock.bind(ADDR) 
print('bind')

#3.수신 대기 상태
srvSock.listen(100) 
print('listen')

#4.연결수락
cltSocket, addr_info = srvSock.accept() 
print('accept')

time.sleep(10)

#연결 종료
cltSocket.close() 

#소켓 종료
srvSock.close()

print('close') """

#--------------------------------

#채팅 프로그래밍
""" import socket
from select import select
import time

HOST = "127.0.0.1"
#HOST = "localhost"
PORT = 8080

BUFSIZE = 1024
ADDR = (HOST,PORT)

srvSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
srvSock.bind(('', PORT))
srvSock.listen()

cltSocket, addr = srvSock.accept()

while True:
    response = cltSocket.recv(1024)
    print ('client : ', response.decode('utf-8'))

    message = input('server : ')
    cltSocket.send(message.encode('utf-8'))
    message = "/0"
cltSocket.close() """


#UDP
""" import socket

HOST = "127.0.0.1"
PORT = 1234

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((HOST, PORT))

while True:
    data, addr = sock.recvfrom(1024)
    print("msg: ", data)

    rsp = data.decode("utf-8").upper()
    sock.sendto(rsp.encode("utf-8"), addr)

sock.close() """

#==========================================================
#7-2

#클래스 & 메서드
""" class Person :
	name = "python"
	age = 23
	number = "01012345678" """
 
""" class Person :
    name = "python"
    age = 23
    number = "01012345678"

    def getIntroduce(self):
        return f"My name is {self.name}" 
        
p=Person()
print(p.name)
print(p.age)
print(p.number)
print(p.getIntroduce())

p1=Person()
print(p1.name)
print(p1.age)
print(p1.number)
print(p1.getIntroduce())
"""


#생성자
""" class Person :
	def __init__(self, name, age, number):
		self.name = name
		self.age = age
		self.number = number
  

p = Person("lee",23,1)
p1 = Person("Park",12,2)
p2 = Person("Kim",25,3)

print(p.name)
print(p1.name)
print(p2.name) """


#클래스 변수
""" class Person :
	count = 0
	
	def __init__(self, name, age,number):
		self.name = name
		self.age = age
		self.number = number
		Person.count +=1
  

p = Person("lee",23,1)
print(p.name)
print(p.count)
p1 = Person("Park",12,2)
print(p1.name)
print(p1.count)
p2 = Person("Kim",25,3)
print(p2.name)
print(p2.count)

print(p.count)
print(p1.count)
print(p2.count) """


#클래스 메서드
class Person :
	count = 0

	def __init__(self, name, age, number):
		self.name = name
		self.age = age
		self.nmuber = number
		Person.count += 1

	@classmethod
	def getCount(cls) : 
		return cls.count

p = Person("lee",23,1)
print(p.name)
print(p.getCount())

p1 = Person("Park",21,2)
print(p1.name)
print(p1.getCount())

p2 = Person("Ju",13,3)
print(p2.name)
print(p2.getCount())