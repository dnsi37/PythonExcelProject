print("hello python")
#기본적으로 출력은 print(), 입력은 input()을 사용한다.
#input()은 기본적으로 str 형태로 값을 받으며, 특정 자료형 함수를 이용하면 다른 형으로 값을 받을 수 있다. 만약 그 형으로 값이 나오지 않으면 예외 오류가 일어난다.
a = input("input")
b = int(input("input"))
c = float(input("input"))
import sys
from typing import Dict, List, Tuple
a = sys.stdin.readline()
b = int(sys.stdin.readline())
c = float(sys.stdin.readline())
a = 50
if a < 100:
    print(1)
elif a > 90:
    print(2)
else:
    print(3)
    
l = [1, 2, 3] #일차원 리스트
t = tuple(l) #튜플로 변환
li = list(t) #리스트로 변환
l = [[1, 2, 3], [1, 2, 3]] #이차원 리스트
li = l[0][2] #li = 3
# 파이썬의 딕셔너리는 키/값 구조로 이뤄진 딕셔너리를 말한다. 파이썬 3.7 이상에서는 입력 순서 또한 유지되며, 내부적으로는 해시 테이블(Hash Table)로 구현되어 있다. 3.6 이하에서는 입력 순서를 보장하지 않으므로 유의해야 한다. 중괄호를 사용해서 선언한다.
# Dictionary
a = {}
a = {'key1':'value1', 'key2':'value2'} 
a['key3'] = 'value3'
a = {'key1':[1, 2, 3], 'key2': (4, 5, 6)}
a=list(map(int,input().split()))
# f string example
name = "Paul"
age = 23
height = 175.324
introduction = f"My name is {name}. My age is {age}. My height is {height:.1f}"
# 문자열 합칠때 조인 사용
''.join(str(x) for x in range(10))
# 반복문
mylist = [10, 20, 30, 40]
# 이렇게 하지 말고,
for i, value in enumerate(mylist):
    print(mylist[i])
full_name : List[int] | Tuple[str,int,float] | str | int | Dict[int] |bool
    
def get_first_name(f : str) -> str:
    return full_name.split("")[0]

fallback_name : Dict[str,str] = {
    "firstname" : "UserName",
    1 : "hi"
}

setInt : int|str 
my_data : Tuple[str,int,float]
def hi(param : my_data):
    return param
data :my_data = ('hi',1,1.0)
hi(data)    
def func1():
    print('BlockDMask')
    return "hi"
# default parameter
def func1(a, b=5, c=10):
    return a + b + c
# 복수형 arg
def func6(*args):
    a = 0
    for i in args:
        a = a + i
    return a
c = func6(2, 3, 4, 5)
print(c)

d = func6(1, 2, 3, 4, 5, 4, 3, 2, 1)
print(d)

