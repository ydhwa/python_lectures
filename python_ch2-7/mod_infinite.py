import sys

import mod_a

# 아무리 무한 반복되는 호출이라도 모듈은 한 번씩만 로드되는 것을 확인할 수 있다.
# 그래도 조심해서 코드를 짜자.
print('import infinitely')

for key in sys.modules.keys():
    print(key)