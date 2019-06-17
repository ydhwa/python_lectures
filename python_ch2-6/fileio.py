# text mode가 default: t
f = open('test.txt', 'w', encoding='utf-8')
write_size = f.write('안녕하세요~\n파이썬입니다.')
f.close()

print(write_size)    # 적힌 글자 수 반환


# binary mode: b
f = open('test.txt', 'wb')      # binary 파일이므로 여기서 encoding 지정은 굳이 필요 없다.
write_size = f.write(bytes('안녕하세요~\n파이썬입니다.', encoding='utf-8'))
f.close()


# read test
f = open('test.txt', 'rt', encoding='utf-8')
text = f.read()
f.close()
print(text)


# binary read: copy file
fsrc = open('python.png', 'rb')
data = fsrc.read()
fsrc.close()

print(type(data))

fdest = open('python2.png', 'wb')
fdest.write(data)
fdest.close()

