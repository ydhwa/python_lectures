import collections
import random
import re


# 문제 1. 파이썬 경로면 s = '/usr/local/bin/python' 에서 각각의 디렉토리 경로명을 분리하여 출력하세요.
#   또, 디렉토리 경로명과 파일명을 분리하여 출력하세요.
def problem1():
    print('[문제 1]')

    s = '/usr/local/bin/python'

    list1 = s[1:].split('/')
    # print(', '.join(list(map(str, list1))))
    print(list1)

    list2 = s.rsplit('/', 1)
    # print('{0}, {1}'.format(list2[0], list2[1]))
    print(list2)

    print()


# 문제 2. 다음과 같은 텍스트에서 모든 태그를 제외한 텍스트만 출력하세요.
def problem2():
    print('[문제 2]')

    s = """
<html>
    <body style='background-color:#ffff'>
        <h4>Click</h4>
        <a href='http://www.python.org'>Here</a>
        <p>
            To connect to the most powerful tools in the world.
        </p>
    </body>
</html>"""
    print(re.sub('[<]{1}[/]?[\w\s\-\'=:/#.]*[>]{1}', '  ', s))

    print()


# 문제 3.
# 1) 다음 문자열을 모든 소문자를 대문자로 변환하고, 문자 ',', '.', '\n'을 없앤 후에 중복 없이 각 단어를 순서대로 출력하세요.
# 2) 각 단어의 빈도수도 함께 출력해 보세요.
def problem3():
    print('[문제 3]')

    s = """We encourage everyone to contribute to Python. If you still have questions after reviewing the material
in this guide, then the Python Mentors group is available to help guide new contributors through the process.""".upper()

    s_list = re.sub("[.,\n]+", "", s).split(" ")
    s_set = sorted(set(s_list))
    s_dict = {}

    print('1)')     # 1)
    for se in s_set:
        print(se)
    print()

    print('2)')     # 2)
    for se in s_list:
        s_dict[se] = s_dict[se] + 1 if se in s_dict else 1
    s_dict = collections.OrderedDict(sorted(s_dict.items()))
    for se in s_dict:
        print('{0}: {1}'.format(se, s_dict[se]))

    # 버그 있음. count를 할 경우 부분 포함까지 카운팅함.
    # for se in s_set:
    #     print('{0}: {1}'.format(se, s.count(se)))

    print()


# 문제 4. 반복문을 이용해서 369게임에서 박수를 쳐야 하는 경우의 수를 순서대로 화면에 출력해보세요.
# 1에서 99까지만 실행하세요.
def problem4():
    print('[문제 4]')

    for i in range(1, 100):
        value1, value2 = divmod(i, 10)
        value1 = '짝' if value1 != 0 and value1 % 3 == 0 else ''
        value2 = '짝' if value2 != 0 and value2 % 3 == 0 else ''

        if value1 == '짝' or value2 == '짝':
            print('{0} {1}{2}'.format(i, value1, value2))

    print()


# 문제 5. 함수 sum을 만드세요. 이 함수는 임의의 개수의 인수를 받아서 그 합을 계산합니다.
# args_sum으로 만듦
def problem5():
    print('[문제 5]')

    print(args_sum(0))
    print(args_sum(0, 1, 2))
    print(args_sum(0, 1, 2, 3, 4, 5, 3))

    print()


def args_sum(*args):
    result = 0
    for i in args:
        result += i
    return result


# 문제 6. 숨겨진 카드의 수를 맞추는 게임입니다.
# 1~100까지의 임의의 수를 가진 카드를 한 장 숨기고 이 카드의 수를 맞추는 게임입니다.
# 아래의 화면과 같이 카드 속의 수가 57인 경우를 보면 수를 맞추는 사람이 40이라고 입력하면 "더 높게",
# 다시 75라고 입력하면 "더 낮게"라는 식으로 범위를 좁혀가며 수를 맞추고 있습니다.
# 게임을 반복하기 위해 y/n 이라고 묻고 n인 경우 종료됩니다.
def problem6():
    print('[문제 6]')

    answer = count = low = high = 0
    start = True
    while True:
        if start:
            start = False
            answer = random.randrange(1, 101)
            count = 1
            low = 1
            high = 100
            print('수를 결정하였습니다. 맞추어보세요.')

        print('{0}-{1}'.format(low, high))
        guess = int(input('{0}>> '.format(count)))
        count += 1

        if guess == answer:
            continue_command = input('맞았습니다.\n다시 하시겠습니까?(y/n)>> ')
            if continue_command == 'y':
                start = True
            else:
                break
        else:
            if guess < answer:
                print('더 높게')
                low = guess if guess > low else low
            else:
                print('더 낮게')
                high = guess if guess < high else high

    print()


if __name__ == '__main__':
    problem1()
    # problem2()
    # problem3()
    # problem4()
    # problem5()
    # problem6()