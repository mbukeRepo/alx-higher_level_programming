#!/usr/bin/python3
""" Defines Rectangle class """


class Rectangle:
    """ Represents a rectangle.

    Attributes:
       number_of_instances (int): number of Rectangle
       print_symbol (string): string used for representation

    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ initialises new Rectangle
        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
        """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        """ Get/set width of the triangle """
        return self.__width

    @width.setter
    def width(self, width):
        if not isinstance(width, int):
            raise(TypeError("width must be an integer"))
        elif width < 0:
            raise(ValueError("width must be >= 0"))
        else:
            self.__width = width

    @property
    def height(self):
        """ Get/Set height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, height):
        if not isinstance(height, int):
            raise(TypeError("height must be an integer"))
        elif height < 0:
            raise(ValueError("height must be >= 0"))
        else:
            self.__height = height

    def area(self):
        """ Returns the area of rectangle """
        return self.__width * self.__height

    def perimeter(self):
        """ Returns the perimeter of the rectangle"""
        if self.__height == 0 or self.__width == 0:
            return (0)
        return (2 * (self.__height + self.__width))

    def __str__(self):
        """ prints the printable Represantation of our rectangle"""
        if self.__width == 0 or self.__height == 0:
            return ""

        rect = []
        for i in range(self.__height):
            [rect.append(str(self.print_symbol)) for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")

        return ("".join(rect))

    def __repr__(self):
        """ returns a formal represantation of object"""
        ret = "Rectangle(" + str(self.__width) + ", "
        ret += str(self.__height) + ")"
        return ret

    def __del__(self):
        """ executes when the object goes out of scope """
        print("Bye rectangle...")
        type(self).number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ returns rectangle with large area
        Args:
            rect_1 (Rectangle): first rect
            rect_2 (Rectangle): second rect
        Raises:
             TypeError: when rect1 or rect2 is not rectangle instance
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() > rect_2.area():
            return rect_1
        elif rect_2.area() > rect_1.area():
            return rect_2
        else:
            return rect_1

    @classmethod
    def square(cls, size=0):
        """ returns new Rectangle with width = height = size
        Args:
            size (int): size of square
        """
        return cls(size, size)
