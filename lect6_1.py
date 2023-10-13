#파일 생성 >> 파일 없으면 자동으로 생성
""" file = open("temp.txt", "w")
file.close() """

#파일 쓰기>> file이 있어야 읽을 수 ㅇ
""" file = open("temp.txt", "w")

file.write("hello")
file.write("world")

file.close() """

#
""" f = open("/Users/python/mijeongp/temp.txt","w")

for i in range(101):
    f.write(f"{i}\n")
    
f.close()   
 """
#추가 쓰기
""" f = open("/Users/python/mijeongp/temp.txt","a")
f.write("hello\n")
f.write("world")
f.close() """

#파일 읽기
""" f = open("temp.txt","r")
res = f.read()
print(res)
f.close() """

#다른 경로 파일 읽기
""" f = open("/Users/python/mijeongp/temp.txt","r")
res = f.read()
print(res)
f.close() """

#readline 한 라인만 출력 >> 알아서 개행문자를 붙여서 한칸씩 더 떨어지
""" f =  open("temp.txt","r")

for l in range(110):
    res = f.readline()
    print(res)

f.close() """

 
""" f =  open("temp.txt","r")
line = f.readlines()
for l in line:
    print(l)

f.close() """

