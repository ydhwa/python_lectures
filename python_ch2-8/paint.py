from point import Point
from rect import Rect

def test_bound_instance_method():
    p = Point()
    p.setx(10)
    p.sety(20)
    p.show()


def test_unbound_class_method():
    p = Point()
    Point.setx(p, 10)
    Point.sety(p, 20)
    Point.show(p)


def test_other_method():
    # print(Point.class_method(Point))
    print(Point.class_method())     # @classmethod 어노테이션 붙인 후
    Point.static_method()


def test_member():
    p = Point()
    p.setx(10)
    p.sety(10)
    print(f'{p.x}, {p.y}, {p.count_of_instance}, {Point.count_of_instance}')

    p.count_of_instance = 2000
    print(f'{p.x}, {p.y}, {p.count_of_instance}, {Point.count_of_instance}')


def test_constructor():
    p1 = Point(10, 20)
    print(f'{p1.x}, {p1.y}, {p1.count_of_instance}, {Point.count_of_instance}')

    p2 = Point(10, 20)
    print(f'{p2.x}, {p2.y}, {p2.count_of_instance}, {Point.count_of_instance}')

    del p1
    print(f'{Point.count_of_instance}')

    del p2
    print(f'{Point.count_of_instance}')


def test_to_string():
    p = Point()
    print(p)
    print(repr(p))

    # p2 = eval('Point(0, 0)')
    p2 = eval(repr(p))
    print(p2)


def test_class_rect():
    r1 = Rect(10, 10, 50, 50)
    r2 = eval(repr(r1))

    print(r1, str(r1.area()), sep=':')
    print(r2, str(r2.area()), sep=':')

    r1.draw()
    r2.draw()

    # 비교 연산자 오버로딩
    print(Rect(10, 20) == Rect(20, 10))
    print(Rect(10, 10) > Rect(10, 5))
    print(Rect(10, 20) < Rect(20, 10))


def test_operator_overloading():
    p1 = Point(100, 200)
    p2 = Point(50, 50)
    p3 = p1 + p2
    p4 = p1 - p2

    print(p3)
    print(p4)

    # 확장 산술 연산자 오버로딩
    p3 += Point(-10, -10)
    p4 -= Point(-10, -10)
    print(p3)
    print(p4)


def main():
    # test_bound_instance_method()
    # test_unbound_class_method()
    # test_other_method()
    # test_member()
    # test_constructor()
    # test_to_string()
    test_class_rect()
    # test_operator_overloading()


if __name__ == '__main__':
    main()
