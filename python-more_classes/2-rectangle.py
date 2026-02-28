#!/usr/bin/python3
""" Defines a rectangle classes"""


class Rectangle:
    """Represent a rectangle"""

    def __init__(self, width=0, hight=0):
        """ Iinitialize a new Rectangle.

        Args:
            width (int): The width of the new rectangle.
            hight (int): The hight of the new rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """get the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be int")
        if value < 0:
            raise ValueError("must be >= 0")
        self.__width = value

    @property
    def height(self):
        """get the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise ValueError("must be an integer")
        if value < 0:
            raise TypeError(" must be >=0")
        self.__height = value

    def area(self):
        """Return the area of the rectangle"""
        return (self.__width * self.__height)

    def perimetr(self):
        """return the perimetr of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return(0)
        return ((self.__width * 2) + (self.__height * 2))
