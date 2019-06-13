# 한 줄 문자열 정리
s = ''
str1 = 'Hello World'
print(type(s), type(str1))
print(isinstance(str1, str))


# 여러 줄 문자열
str2 = '''abc
1234
가나다라
'''
print(str2)

'''
여기는 주석 입니다.
여러 라인 주석을 대체할 수 있습니다.
'''

print("\n헬로\t11")

# 문자열 연산
# 1. 인덱싱
str1 = 'First String'
str2 = 'Second String'
print(str1[0], str1[1], str2[2])
print(str1[-1], str1[-2], str2[-3])     # slicing 에서 유용

# 2. Slicing
# s[start:stop:step]
str3 = str2[2:5]
print(str3)
print(str2[2:len(str2)])
print(str2[2:])

s = "Python"
print(s[-1])        # last
print(s[-2:])       # 마지막 2개 문자
print(s[:-2])       # 마지막 2개 문자 제외한 나머지 문자들

print(s[::-1])      # reverse
print(s[1::-1])     # 첫번째, 두번째 문자. s[1:0:-1]
print(s[:-3:-1])    # 마지막 2개의 문자를 가져옴
print(s[-3::-1])    # 마지막 2개의 문자를 제외한 나머지 문자들


# 연결(+)
print(str1 + ' ' + str2)
# 리터럴 연결 시 + 생략 가능
# str3 = '1st' + ' ' + '2nd'
str3 = '1st' ' ' '2nd'
print(str3)

# 문자열 객체 연결은 문자열끼리만 할 수 있다.
name = '둘리'
age = 10
# print(name + age)
print(name + str(10))

# 반복
print(str1 * 3)

# len() 함수
print(len(str1))

# in, not in 연산
print('F' in str1)
print('S' not in str1)

# str 객체는 immutable 이다.
# str1[0] = 'f'

# 서식(formatting) = format 함수
print(format(name, "s"), format(age, "d"))

# 서식: 튜플을 이용한 방식
f = "name: %s, age: %d"
print(f % (name, age))

# 서식: 딕셔너리를 이용한 방식
f = "name: %(n)s, age: %(a)d"
print(f % {'n': name, 'a': 10})

print('Name: {0}, Age: {1}'.format(name, age))




