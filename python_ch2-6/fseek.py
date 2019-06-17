f = open('abc.txt', 'wb')
f.write(b'0123456789')
f.close()

f = open('abc.txt', 'rb')
print(f.tell())

f.seek(5, 1)
data = f.read(2)
print(data)

f.seek(-5, 1)
data = f.read(2)
print(data)

f.seek(0, 2)    # 맨끝으로 이동

f.seek(-5, 1)
data = f.read(3)
print(data)

