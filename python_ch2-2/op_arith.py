# 사칙연산
print(2 * 3)
print(2 / 3)
print(2 + 3)
print(2 - 3)
# 나눗셈은 Java처럼 하지 않고, 결과값이 실수라면 정수로만 나타낸 식이라도 실수로 나타낸다.
print(2 / 3)
print(2 / 3.0)
print(2.0 / 3)

# //(몫) **(지수승), %(나머지)
print(2 // 3)
print(2 ** 3)
print(2 % 3)

# 몫과 나머지를 동시에 반환
# 자동 unpacking
result, last = divmod(2, 3)
print(result, last)

# 자동 packing
t = divmod(2, 3)
print(t, type(t))

# 연산자 우선순위
print(2 + 3 * 4)
print(-2 + 3 * 4)   # 단항연산자가 제일 우선순위 높음
print(-(2 + 3) * 4)
print(4 / 2 * 2)
print(4 / 2 * 2)    # 연산자 결합 순서가 있다. 보통 좌 -> 우지만,
print(2 ** 3 ** 4)  # 이런 경우 결합 순서를 주의해야 한다. 3 ** 4의 결과값이 2 ** ___에 대입된다. (= 2 ** (3 ** 4))
print((2 ** 3) ** 4)
print(2 ** (3 ** 4))

