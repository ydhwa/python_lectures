import re


# 문제 1. 파이썬 경로면 s = '/usr/local/bin/python' 에서 각각의 디렉토리 경로명을 분리하여 출력하세요.
#   또, 디렉토리 경로명과 파일명을 분리하여 출력하세요.
def problem1():
    print('[문제 1]')

    s = '/usr/local/bin/python'

    list1 = s[1:].split('/')
    print(', '.join(list(map(str, list1))))

    last_index = s.rfind('/')
    print('{0}, {1}'.format(s[0:last_index], s[last_index + 1:]))

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
    </html>
    """

    # 아직 정규식 완성 못함. 인터넷이 안됨
    print(re.sub('[<]{1}[/]?[\w\s=:\'/#.\-]*[>]{1}', '  ', s))


if __name__ == '__main__':
    # problem1()
    problem2()

