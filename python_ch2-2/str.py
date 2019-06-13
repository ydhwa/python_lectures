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


# 객체함수
# 1. 대소문자 관련
s = 'i like Python'
print(s.upper())
print(s.lower())
print(s.swapcase())     # 소 -> 대, 대 -> 소
print(s.capitalize())
print(s.title())        # 단어 첫자 대문자로

# 2. 검색
s = 'I Like Python. I Like Java Also'
print(s.count('Like'))
print(s.find('Like', 5))
print(s.find('JavaScript'))     # 못찾았으면 -1 반환
print(s.rfind('Like'))      # = lastIndexOf

print(s.index('Like'))      # find와의 차이점: 못찾으면 exception이 뜸
print(s.rindex('Like'))     # rfind와의 차이점: 위와 동일

print(s.startswith('I LIke'))
print(s.startswith('Like', 2))
print(s.endswith('Also'))
print(s.endswith('Java', 0, 26))

# 편집과 치환
s = '      spam ans ham      '
print('------' + s.strip() + '-------')
print('------' + s.rstrip() + '-------')
print('------' + s.lstrip() + '-------')

s = '<><abc><><defg><><>'
print('------' + s.strip('<>') + '------')
print('------' + s.strip('><') + '------')

s = 'Hello Java'
print(s.replace('Java', "Python"))

# 분리 & 결합
s = 'spam and ham'
l = s.split(' and ')
print(l, type(l))

s2 = ':'.join(l)
print(s2)

s3 = 'one:two:three:four:five'
print(s3.split(':'))
print(s3.split(':', 2))
print(s3.rsplit(':', 2))


lines = '''1st line
2nd line
3rd line
4th line
'''
print(lines.split('\n'))
print(lines.splitlines())   # 맨 끝에 있는 빈 스트링은 취급하지 않음

# 판별
print('1234'.isdigit())
print('hello'.isdigit())
print('1234'.isalpha())
print('hello'.isalpha())
print('1234a'.isalnum())
print('abcd'.isupper())
print('abcd'.islower())
print('        '.isspace())
print('\r\n\t'.isspace())     # 컨트롤 문자

# '0' 채우기
print('20'.zfill(5))
print('1234'.zfill(5))

# 서식: 객체함수
print('Name: {}, Age: {}'.format(name, age))
print('Name: {0}, Age: {1}'.format(name, age))
print('Name: {1}, Age: {0}'.format(name, age))
print('{:3}의 제곱근은 {:.7}'.format(2, 2 ** 0.5))
print('Name: {n}, Age: {a}'.format_map({'n': name, 'a': age}))


