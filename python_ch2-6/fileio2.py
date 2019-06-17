f = open('test.txt', 'rt', encoding='utf-8')
text = f.read()
print(text)
text = f.read()
print('---', text, '---')


# Position 단위는 byte
# tell(): 현재 파일에서 어디까지 읽고 썼는지 위치 반환
pos = f.tell()
print(pos)


# seek(): 사용자가 원하는 위치로 파일 포인터를 이동
# 1st param: offset
# 2ed param: from_with(0: 시작, 1: 현재 위치, 2: Rmx)
# text mode에서는 from_what은 0(파일 시작)만 허용
# (offset, from_what)
f.seek(16, 0)
text = f.read()
print(text)

# 예외는 seek(0, 2) 끝으로 이동하는 경우
f.seek(0, 2)


# line 단위로 읽기
line_num = 0
f2 = open('fileio2.py', 'rt', encoding='utf-8')
while True:
    line = f2.readline()
    if line == '':
        f2.close()
        break
    line_num += 1
    print('{0}: {1}'.format(line_num, line), end='')     # 개행 포함하여 읽었다.
print()

f3 = open('fileio2.py', 'rt', encoding='utf-8')
lines = f3.readlines()
f3.close()
print(type(lines))
for line_num, line in enumerate(lines):
    print('{0}: {1}'.format(line_num, line), end='')
print()

# with ~ as (파일 자동으로 열고 닫아줌 - 자동 자원 정리)
# 즉, close()가 필요없다.
line_num = 0
with open('fileio2.py', 'rt', encoding='utf-8') as f3:
    for line_num, line in enumerate(f3.readlines()):
        print('{0}: {1}'.format(line_num, line), end='')
print()
