import sys

# 레퍼런스 카운트는 객체를 참조하는 수이다.
# 레퍼런스 카운트가 0이 되면 더 이상 사용하지 않는 객체이므로 자동으로 사라진다.
# 이러한 작업을 Garbage Collection 이라 부른다.

x = object()
print(type(x))
print(sys.getrefcount(x))

y = x
print(sys.getrefcount(x))

# 레퍼런스 값 줄이기
# del은 심볼테이블에서 이름을 제거한다.
del x
print(sys.getrefcount(y))
print(globals())