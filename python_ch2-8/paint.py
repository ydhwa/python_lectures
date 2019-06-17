from point import Point


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


def main():
    test_bound_instance_method()
    test_unbound_class_method()
    test_other_method()


if __name__ == '__main__':
    main()