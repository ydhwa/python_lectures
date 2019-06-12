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

    print()


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

    print()


# 문제 3. 다음과 같은 출력이 되도록 이중 for~in 문을 사용한 코드를 작성하세요.
def problem3():
    print('[문제 3]')

    for i in range(1, 11):
        for j in range(0, i):
            print('*', end='')
        print()

    print()


# 문제 4. 다음과 같은 출력이 되도록 구구단을 작성하세요. (이중 for~in)
def problem4():
    print('[문제 4]')

    for i in range(1, 10):
        for j in range(1, 10):
            print(j, 'x', i, '=', (j * i), end='\t\t')
        print()

    print()


# 문제 5. 주어진 리스트 데이터를 이용하여 3의 배수의 개수와 배수의 합을 구하여 출력형태와 같이 출력하세요.
def problem5():
    print('[문제 5]')

    l1 = [5, 76, 1, 3, 27, 10]

    print('주어진 리스트에서 3의 배수의 개수=>', len(l1))
    print('주어진 리스트에서 3의 배수의 합=>', sum(l1))

    print()


# 문제 6. 키보드에서 정수로 된 돈의 액수를 입력 받아
# 오만원 권, 만원 권, 오천원 권, 천원 권, 500원짜리 동전, 100원짜리 동전, 50원짜리 동전, 10원짜리 동전, 1원짜리 동전 각 몇 개로 변환 되는지 작성하시오.
def problem6():
    print('[문제 6]')

    money = [50000, 10000, 5000, 1000, 500, 100, 50, 10, 5, 1]

    try:
        balance = int(input('금액: '))
        for m in money:
            share, balance = divmod(balance, m)
            print('{0}원: {1}개'.format(m, share))

    except ValueError:
        print('금액으로 환산할 수 없는 입력입니다.')

    print()


# 문제 7. 키보드에서 5개의 정수를 입력 받아 리스트에 저장하고 평균을 구하는 프로그램을 작성하시오.
def problem7():
    print('[문제 7]')

    # 여긴 예외처리 안함
    #list(map(int, input('리스트에 넣을 정수를 입력해주세요. " " 단위로 구분합니다.').split()))
    l1 = []
    for i in range(5):
        l1.append(int(input('> ')))

    print('채워진 리스트: ', l1)
    print('평균:', sum(l1) / 5)

    print()


# 문제 8. 문자열을 입력 받아, 해당 문자열을 문자 순서를 뒤집어서 반환하는 함수 reverse(s)을 작성하세요.
def problem8():
    print('[문제 8]')

    s = input('입력> ')
    print('결과>', reverse(s))

    print()


def reverse(s):
    slist = list(s)
    size = len(s)
    for i in range(int(size / 2)):
        slist[i], slist[size - 1 - i] = slist[size - 1 - i], slist[i]
    return ''.join(slist)


# 문제 9. 주어진 if 문을 dict를 사용해서 수정하세요.
def problem9():
    print('[문제 9]')

    menu = input('메뉴: ')
    menu_dict = {'오뎅': 300, '순대': 400, '만두': 500}

    # if menu == '오뎅':
    #     price = 300
    # elif menu == '순대':
    #     price = 400
    # elif menu == '만두':
    #     price = 500
    # else:
    #     price = 0

    print('가격: {0}'.format(0 if menu_dict.get(menu) is None else menu_dict[menu]))

    print()


# 문제 10. 숫자를 입력 받아서 아래와 같은 실행결과가 나타나도록 코드를 완성하세요.
# a. 입력 받은 숫자가 홀수인 경우에는, 0부터 입력 값까지 홀수의 합을 출력합니다.
#   - 예제: 입력이 7이면 16을 출력(1 + 3 + 5 + 7 = 16)
# b. 입력 받은 숫자가 짝수인 경우에는, 0부터 입력 값까지 짝수의 합을 출력합니다.
#   - 예제: 입력이 10이면 30을 출력(2 + 4 + 6 + 8 + 10 = 30)
def problem10():
    print('[문제 10]')
    # 예외처리 하지 않음
    var = int(input('숫자를 입력하세요: '))

    if var % 2 == 1:
        result = sum(filter(lambda i: i % 2 == 1, range(var + 1)))
    else:
        result = sum(filter(lambda i: i % 2 == 0, range(var + 1)))

    print('결과 값:', result)

    print();


if __name__ == '__main__':
    # problem1()
    # problem2()
    # problem3()
    # problem4()
    # problem4()
    # problem5()
    # problem6()
    # problem7()
    # problem8()
    # problem9()
    problem10()