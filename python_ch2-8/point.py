# class Point

class Point(object):
    count_of_instance = 1000

    # 인스턴스 메소드
    def setx(self, x):
        self.x = x

    def sety(self, y):
        self.y = y

    def getx(self):
        return self.x

    def gety(self):
        return self.y

    def show(self):
        print(f'점[{self.x}, {self.y}]를 그렸습니다.')


    # 클래스 메소드
    @classmethod
    def class_method(cls):
        return cls.count_of_instance


    # 스태틱 메소드
    def static_method():
        print('static_method() 호출')


