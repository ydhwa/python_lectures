# ~
print(~5)
# 위의 값: ~00000101 = 11111010
# 6의 2의 보수: 00000110 -> 11111001 -> 11111010
print(~-1)

# << 연산
a = 4
print(a >> 1)

a = -4
print(a >> 1)

# bit and, or, exclusive or
a = 3
print(a & 2)
print(a | 8)
print(0x0f ^ 0x06)


