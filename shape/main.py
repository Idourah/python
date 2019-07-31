""""
   Author      : YOANE KARATSUBA
   
   TITLE       : compute area and perimeter of shapes 
   
   DESCRIPTION : this Tp covers OOP principles in python : Abstraction, Polymorphism, Inheritance, Decomposition
   
   COMMENT     : feel free to download copy and alter to view how it properly work, email me if you have questions 
   
   Email       : idourah96@gmail.com
   
   DATE        : 31-08-2019
   
   VERSION     : 1.0
   
   Motto       : Learn code, Love code, Live code
"""""

from Triangle.rectangle import RectangleTriangle
from Triangle.equilateral import EquilateralTriangle
from Triangle.isosceleTriangle import IsosceleTriangle


def main():
    a, b, c = 4, 20, 63
    isoscele = IsosceleTriangle(b, a)    # a = b

    rectangle = RectangleTriangle(c, b)  # a , b

    equilateral = EquilateralTriangle(a)  # a = b = c

    print("\nisoscele triangle area :", isoscele.area(), " perimeter :", isoscele.perimeter())

    print("\nequilateral triangle area :", equilateral.area(), " perimeter :", equilateral.perimeter())

    print("\nrectangle triangle area :", rectangle.area(), " perimeter :", rectangle.perimeter())


if __name__ == "__main__":
    main()
