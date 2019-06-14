import math


# 문제1.
# 다음 세 개의 리스트가 있을 때,
# subs = [‘I’, ‘You’]
# verbs = [‘Play’, ‘Love’]
# objs = [‘Hockey’, ‘Football’]
#
# 3형식 문장을 모두 출력해 보세요. 반드시 comprehension을 사용합니다.
import random


def problem01():
    print('[문제 1]')

    subs = ['I', 'You']
    verbs = ['Play', 'Love']
    objs = ['Hockey', 'Football']
    result = ['{0} {1} {2}'.format(subs[i], verbs[i], objs[i]) for i in range(2)]
    print('\n'.join(result))

    print()

# 문제2.
# range() 함수와 유사한 frange() 함수를 작성해 보세요. frange() 함수는 실수 리스트를
# 반환합니다.
def problem02():
    print('[문제 2]')

    print(frange(2))
    print(frange(1.0, 2.0))
    print(frange(1.0, 3.0, 0.5))

    print()


def frange(val, base=0.0, step=0.1):
    result = []
    if val < base:
        start = val
        stop = base
    else:
        start = base
        stop = val

    while start <= stop:
        result.append(start)
        start += step
    return result


# 문제3.
# 중첩 루프를 이용해 신문 배달을 하는 프로그램을 작성하세요. 단, 아래에서 arrears 리스트는 신문
# 구독료가 미납된 세대에 대한 정보를 포함하고 있는데, 해당 세대에는 신문을 배달하지 않아야
# 합니다.
def problem03():
    print('[문제 3]')

    apart = [[101, 102, 103, 104], [201, 202, 203, 204], [301, 302, 303, 304], [401, 402, 403, 404]]
    arrears = [101, 203, 301, 404]

    for i in range(len(apart)):
        for room in apart[i]:
            if room not in arrears:
                # print('Newspaper delivery: {0}'.format(room))
                print(f'Newspaper delivery: {room}')        # 이게 더 빠르다고 함

    print()


# 문제4.
# 구구단 중에 특정 곱셈을 만들고 그 답을 선택하는 프로그램을 작성하는 문제입니다.
# 답을 포함하여 9개의 정수가 아래와 같은 형태로 출력되고 사용자는 답을 골라 입력하게 됩니다.
# 프로그램은 정답 여부를 다시 출력합니다
def problem04():
    print('[문제 4]')

    first_num, second_num = random.randrange(9) + 1, random.randrange(9) + 1
    answer = first_num * second_num
    print('{0} x {1} = ?\n'.format(first_num, second_num))

    examples = make_example_list(answer)        # 정답을 포함한 답 목록 생성
    print_example_list(examples)                # 답 목록 출력

    # 풀기 전까진 빠져나올 수 없는 지옥
    while True:
        user_answer = input('answer: ')

        if user_answer.isdigit():
            if int(user_answer) not in examples:
                print('보기에 있는 답 중 하나를 입력해주세요.')
            elif answer == int(user_answer):
                print('정답')
                break
            else:
                print('오답')
        else:
            print('정수를 입력하세요.')

    print()


# 정답을 포함한 답 목록 생성
def print_example_list(examples):
    for i in range(0, 9, 3):
        print('{0}\t{1}\t{2}'.format(examples[i + 0], examples[i + 1], examples[i + 2]))
    print()

    return examples


# 답 목록 출력
def make_example_list(answer):
    answers = []
    examples = set()

    for i in range(1, 10):
        for j in range(1, 10):
            answers.append(i * j)

    answers = list(answers)

    # 답 목록을 넣을 때 중복검사 해야한다.
    while len(examples) < 9:
        example = answers[random.randrange(len(answers))]
        examples.add(example)

    examples = list(examples)
    examples[random.randrange(9)] = answer

    return examples


# 문제5.
# 선택정렬(제자리 정렬 알고리즘)을 적용하는 코드를 완성하세요.
# 문제에 주어진 배열 [ 5, 9, 3, 8, 60, 20, 1 ] 를
# 크기 순서대로 정렬하여 다음과 같은 출력이 되도록 완성하는 문제입니다.
def problem05():
    print('[문제 5]')

    l = [5, 9, 3, 8, 60, 20, 1]

    # print('Before sort\n{0}'.format(' '.join(str(i) for i in l)))
    # print('(Bubble Sort)After sort\n{0}'.format(' '.join(str(i) for i in bubble_sort(l))))
    # print('(Selection Sort)After sort\n{0}'.format(' '.join(str(i) for i in selection_sort(l))))

    print_sort('Before', l)
    print_sort('Bubble Sort - After', bubble_sort(l))
    print_sort('Selection Sort - After', selection_sort(l))

    print()


def print_sort(sort_style, l):
    print('{0} sort\n{1}'.format(sort_style, ' '.join(str(i) for i in l)))


def bubble_sort(l):
    for i in range(len(l) - 1):
        for j in range(len(l) - 1 - i):
            if l[j] < l[j + 1]:
                l[j + 1], l[j] = l[j], l[j + 1]
    return l


def selection_sort(l):
    for i in range(len(l) - 1):
        max_index = i
        for j in range(i, len(l)):
            if l[j] > l[max_index]:
                max_index = j
        l[max_index], l[i] = l[i], l[max_index]

    return l


if __name__ == '__main__':
    # problem01()
    # problem02()
    # problem03()
    # problem04()
    problem05()

