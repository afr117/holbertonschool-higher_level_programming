#!/usr/bin/python3
from models.rectangle import Rectangle
from models.square import Square

if __name__ == "__main__":
    r1 = Rectangle(10, 2)
    print(r1)
    r2 = Rectangle(2, 10)
    print(r2)
    s1 = Square(5)
    print(s1)
    s2 = Square(7, 9, 1)
    print(s2)

    r1_dictionary = r1.to_dictionary()
    print(r1_dictionary)
    s1_dictionary = s1.to_dictionary()
    print(s1_dictionary)

    r1.update(89)
    print(r1)

    r1.update(10, 10, 10, 10, 10)
    print(r1)

    s1.update(x=12)
    print(s1)

    s1.update(size=7, y=1)
    print(s1)

