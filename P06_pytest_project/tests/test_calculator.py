class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        return a / b


def test_add():
    # arrange
    a = 123
    b = 456
    cal = Calculator()

    # act
    result = cal.add(a, b)

    # assert
    expected = 579
    assert result == expected


def test_subtract():
    # arrange
    a = 4321
    b = 1234
    cal = Calculator()

    # act
    result = cal.subtract(a, b)

    # assert
    expected = 3087
    assert result == expected


def test_multiply():
    # arrange
    a = 10
    b = 5
    cal = Calculator()

    # act
    result = cal.multiply(a, b)

    # assert
    expected = 50
    assert result == expected


def test_divide():
    # arrange
    a = 100
    b = 10
    cal = Calculator()

    # act
    result = cal.divide(a, b)

    # assert
    expected = 10
    assert result == expected
