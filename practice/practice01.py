# 문제 1. 키보드로 정수 수치를 입력 받아 그것이 3의 배수인지 판단하세요.
def problem1():
    print('[문제 1]')

    try:
        var = int(input('수를 입력하세요: '))

        if var % 3 != 0:
            print('3의 배수가 아닙니다.')
        else:
            print('3의 배수 입니다.')

    except ValueError:
        print('정수가 아닙니다.')

    print('')


# 문제 2. 키보드로 정수 수치를 입력 받아 짝수인지 홀수 인지 판별하는 코드를 작성하세요.
def problem2():
    print('[문제 2]')

    try:
        var = int(input('수를 입력하세요: '))

        if var % 2 == 0:
            print('짝수')
        else:
            print('홀수')

    except ValueError:
        print('정수가 아닙니다.')

    print('')


# 문제 3. 다음과 같은 출력이 되도록 이중 for~in 문을 사용한 코드를 작성하세요.
def problem3():
    print('[문제 3]')

    for i in range(1, 11):
        for j in range(0, i):
            print('*', end='')
        print('')

    print('')


# 문제 4. 다음과 같은 출력이 되도록 구구단을 작성하세요. (이중 for~in)



if __name__ == '__main__':
    #problem1()
    #problem2()
    problem3()

