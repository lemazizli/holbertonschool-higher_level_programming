#!/usr/bin/python3

"""Define a class Square with size and position attributes."""


class Square:
    """Represents a square with private size and position attributes."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize the square with size and position.

        Args:
            size (int): size of the square (default is 0)
            position (tuple): coordinates (x, y) (default is (0, 0))

        Raises:
            TypeError: if size is not an integer
            ValueError: if size < 0
            TypeError: if position is not a tuple of 2 positive integers
        """
        self.size = size      # use setter for validation
        self.position = position  # use setter for validation

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieve the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position with validation."""
        if (not isinstance(value, tuple) or
            len(value) != 2 or
            not all(isinstance(n, int) for n in value) or
            not all(n >= 0 for n in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the current square area."""
        return self.__size ** 2

    def my_print(self):
        """Print the square with the character # to stdout.

        Accounts for position attribute.
        If size is 0, prints an empty line.
        """
        if self.__size == 0:
            print()
            return

        # print vertical position
        for _ in range(self.__position[1]):
            print()

        # print square lines
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
