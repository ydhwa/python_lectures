# 변수 이름은 문자, 숫자, _로 구성된다.
import keyword

friend = 1
a = 10
my_name = '양동화'
myName = '양동화'
_yourname = '둘리'
member1 = '도우넛'

# 에러

# friend$ = 1
# a! = 10
# @myName = '양동화'
# 1abc = 10
# def = 10

# module의 namespace를 명시하고 호출한다.
print(keyword.kwlist)
print(len(keyword.kwlist))

# 한글이름의 변수도 사용이 가능하다.
가격1 = 10000
print(가격1 - 3000)

'''
    여러 줄 주석을 씁니다.
    안녕하세요.
'''

