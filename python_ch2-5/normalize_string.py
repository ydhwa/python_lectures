# 문자열 데이터를 분석하기 전에 처리함수 만들기
# 1. 공백제거
# 2. 필요 없는 문장부호 제거
# 3. 대소문자 정리(Capitalize)
import re

states = ['Alabama', 'Georgia!', 'Georgia', 'georgia', 'FlOrIda', 'south carolina ', 'West virginia?']


def clean_string(strings):
    result = []

    for string in strings:
        string = string.strip()
        string = re.sub('[!#?]', '', string)
        string = string.title()
        result.append(string)

    return result


results = clean_string(states)
print(results)

############################

states = ['Alabama', 'Georgia!', 'Georgia', 'georgia', 'FlOrIda', 'south carolina ', 'West virginia?']

# 가변 인수: 여러개의 함수
def clean_string(strings, *funcs):
    result = []

    for string in strings:
        for func in funcs:
            string = func(string)
        result.append(string)

    return result


def remove_special(s):
    return re.sub('[!#?]', '', s)


# results = clean_string(states, str.strip, str.title, remove_special)
results = clean_string(states, str.strip, str.title, lambda s: re.sub('[!#?]', '', s))
print(results)


print('  abc    '.strip())
print(str.strip("   abc      "))
