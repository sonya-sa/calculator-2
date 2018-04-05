"""Math functions for calculator."""


def add(nums):
    """Return the sum of all inputs."""

    return reduce(lambda x, y: x + y, nums)


def subtract(nums):
    """Return the second number subtracted from the first."""

    return reduce(lambda x, y: x - y, nums)


def multiply(nums):
    """Multiply all inputs together."""

    return reduce(lambda x, y: x * y, nums)


def divide(nums):
    """Return the quotient of all inputs."""

    return reduce(lambda x, y: x / y, nums)


def square(num):
    """Return the square of all inputs."""

    return num ** 2


def cube(num):
    """Return the cube of all inputs."""

    return num ** 3


def power(nums):
    """Raise num1 to the power of num and return the value."""

    return reduce(lambda x, y: x ** y, nums)


def mod(nums):
    """Return the remainder of the quotient of all inputs."""

    return reduce(lambda x, y: x % y, nums)
