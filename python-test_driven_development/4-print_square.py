
#!/usr/bin/python3
""" Function that prints a square"""


def print_square(size):
        """ function that check the parameter and print a square
        Args:
                size (int): is the size of the square
        Raises:
                TypeError: if size is not int
                ValueError: if size is less than 0
        """
        if type(size) is not int:
                raise TypeError("size must be an integer")
        if size < 0:
                raise ValueError("size must be >= 0")
        for x in range(size):
                for y in range(size):
                        print("#", end='')
                print()
