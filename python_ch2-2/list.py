# 리스트 생성
l = [1, 2, 'python']

print(l, type(l))

# indexing
print(l[-3], l[-2], l[-1], l[0], l[1], l[2])

# slicing
print(l[1:3])
print(l[:])
print(l[2:])
print(l[len(l) - 1::-1])

# 반복
l2 = l * 2
print(l2)

# 연결
l3 = l + [3, 4, 5]
print(l3)

# 길이
print(len(l3))

# 확인
print(5 in l3)

# 삭제
del l3[0]
print(l3)

# 변경 가능한 시퀀스(mutable)
a = ['apple', 'banana', 10, 20]
a[2] = a[2] * 90
print(a)

# 슬라이싱을 통한 치환
a = [1, 12, 123, 1234]

a[0:2] = [10, 20]
print(a)

a[0:2] = [10]
print(a)

a[1:2] = [20, 30, 40]
print(a)

# 슬라이싱을 통한 삭제
a = [1, 12, 123, 1234]
a[1:2] = []
print(a)

a[0:] = []
print(a)

# 슬라이싱을 통한 삽입
a = [1, 12, 123, 1234]

# 중간
a[1:1] = ['a']
print(a)

# 마지막
a[len(a):] = [12345]
print(a)

# 처음
a[:0] = [0]

# 여러개 삽입
a[2:2] = [-12, -1, 0]
print(a)


# 객체함수
a = [1, 12, 123, 1234]

# 삽입
a.insert(1, 'a')
print(a)

# 뒤에 삽입
a.append(12345)
print(a)

# 앞에 삽입
a.insert(0, 'bb')
print(a)

# reverse
a.reverse()
print(a)

# 제거(값)
a.remove(12)
print(a)

# 확장
a.extend([-1, -2, -3])
print(a)

# 스택으로 확장하기
stack = []
stack.append(10)
stack.append(20)
stack.append(30)

print(stack)
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack)

# queue로 사용하기
q = [1, 2]
q.append(3)
q.append(4)
q.append(5)

print(q)
print(q.pop(0))
print(q.pop(0))
print(q.pop(0))
print(q)

# sort() 내장된 소팅 알고리즘
l3 = [1, 5, 2, 3, 40, 9, 8]
l3.sort()
print(l3)

l3.sort(reverse=True)
print(l3)

l3 = [10, 2, 22, 9, 8, 33, 4]
# l3.sort(key=str)
l3.sort(key=int)
print(l3)

# cf. 내장(전역) 함수 sorted
l3 = [10, 2, 22, 9, 8, 33, 4]
l4 = sorted(l3, reverse=True)
print(l4)


def foo(x):
    return x


l3 = [10, 46, 22, 93, 81, 35, 44]
l4 = sorted(l3, key=foo)
print(l3)
