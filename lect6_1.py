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

##1023수업

""" #file exist
import os

fp = "mod/calc.py"
#fp = "temp1.txt"

#file = open(fp,"w")
if os.path.exists(fp) :
	print("ok")
    file = open("temp.txt","a")  
else :
	print("error")
    file = open("temp.txt","w")
    
#file.close() """


""" import os
fp = "temp.txt"

if os.path.exists(fp):
    f = open(fp,"r")
    for line in f:
        print(line)
else:
    f = open(fp,"w")
    for i in range(100):
        f.write(str(i)+"\n")
    #print("error")

f.close() """

#파일 삭제
#import os

#fp = "new.txt"

""" f = open(fp,"w")
f.close() """

""" os.remove(fp)
print ("complete") """



""" def dir_print(p) :
	files = os.listdir(p)
	for f in files :
		print(f)
  
fp = "new.txt"

f = open(fp,"w")
f.close() 

dir_print("./")

os.remove(fp)
print("------------------------\n\n") """

#파일명 변경
""" import os

fp = "new.txt"

f = open(fp,"w")
f.close() 

os.rename(fp, "new1.txt")
print("complete") """

#재변경 예외처리
""" import os

fp = "new.txt"
tp = "new1.txt"

f = open(fp,"w")
f.close() 

if os.path.exists(tp):
    print("exist, same name file")
    os.remove(tp)
else:
    os.rename(fp,"new1.txt")
    print("complete") """
    
#파일명 변경 확인

""" import os

def dir_print(p) :
	files = os.listdir(p)
	for f in files :
		print(f)
  
fp = "new.txt"
tp = "new1.txt"

f = open(fp,"w")
f.close()

dir_print("./")
print("\n==========================")

if os.path.exists(tp):
    print("exist, same name file")
    os.remove(tp)
else:
    os.rename(fp,"new1.txt")
    print("complete") """


#with 파일 자동 close
""" with open("temp.txt","r") as f:
    print(f.read()) """