# 리스트, 세트, 사전 내포(comprehension)

results = []
for n in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    result = n * n
    results.append(result)
print(results)

# list comprehension
results = [result * result for result in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]
print(results)

# 문자열 리스트에서 길이가 2 이하인 문자열 리스트
strings = ['a', 'as', 'bar', 'car', 'dove', 'python', 'py']
strings = ['[' + s + ']' for s in strings if len(s) <= 2]
print(strings)

# 1~100 사이의 수 중에서 짝수 리스트
evens = [i for i in range(1, 101) if i % 2 == 0]
print(evens)


# set comprehension
strings = ['a', 'as', 'bar', 'car', 'dove', 'as', 'python', 'py']
strings = {s for s in strings if len(s) <= 2}
print(strings, type(strings))

# 문자열 길이를 set으로 저장하기
strings = ['a', 'as', 'bar', 'car', 'dove', 'as', 'python', 'py']
stringths = {len(s) for s in strings}
print(stringths)


# dict comprehension
strings = ['a', 'as', 'bar', 'car', 'dove', 'as', 'python', 'py']
d = {s: len(s) for s in strings}
print(d)


# 369 (practice2: problem04)
for t in [(n, '짝'*(str(n).count('3') + str(n).count('6') + str(n).count('9'))) for n in range(1, 1000) if '3' in str(n) or '6' in str(n) or '9' in str(n)]:
    print('%s: %s' % t)
