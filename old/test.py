"""
Test
"""


def number(value):
    """Attempts to cast a value to a number"""
    if isinstance(value, str):
        try:
            value = float(value)
            if value.is_integer():
                value = int(value)
        except ValueError:
            return 0
    if value == float('NaN'):
        return 0
    return value


class Variable:
    """Handles variable casting for +="""

    def __init__(self, value):
        self.value = value

    def __get__(self, obj, _=None):
        return self.value

    def __set__(self, obj, value):
        """Set the variable's value"""
        self.value = value

    def __iadd__(self, other):
        self.value = number(self.value) + number(other)
        return self

    def __str__(self):
        return str(self.value)

    def __float__(self):
        return number(self.value)

    def show(self):
        """Print the value"""
        print(self.value)

    def hide(self):
        """Do nothing"""


class Test:
    bob = Variable(6)

    def __init__(self):
        self.bob = "5"
        print(self.bob)
        self.bob += 3
        print(self.bob)
        self.bob = "5"
        print(self.bob)
        self.bob += 2
        self.bob.show()


t = Test()


class Value:
    """Handles casting a value as necesary"""

    def __init__(self, value):
        self.value = value

    def __lt__(self, other):
        return self.value < other

    def __le__(self, other):
        return self.value <= other

    def __eq__(self, other):
        return str(self.value) == str(other)

    def __ne__(self, other):
        return str(self.value) != str(other)

    def __gt__(self, other):
        return self.value > other

    def __ge__(self, other):
        return self.value >= other

    def __bool__(self):
        return bool(self.value)

    def __add__(self, other):
        return self.to_number(self.value) + self.to_number(other)

    def __sub__(self, other):
        return self.to_number(self.value) - self.to_number(other)

    def __mul__(self, other):
        return self.to_number(self.value) * self.to_number(other)

    def __truediv__(self, other):
        return self.to_number(self.value) / self.to_number(other)

    def __mod__(self, other):
        return self.to_number(self.value) % self.to_number(other)

    def __pow__(self, other):
        return pow(self.to_number(self.value), self.to_number(other))

    def __iadd__(self, other):
        self.value = self.to_number(self.value) + self.to_number(other)

    def __isub__(self, other):
        self.value = self.to_number(self.value) + self.to_number(other)

    def __index__(self):
        try:
            return int(self)
        except ValueError:
            return 0
        except OverflowError:
            return 0

    @staticmethod
    def to_number(value):
        """Attempts to cast a value to a number"""
        if isinstance(value, str):
            try:
                value = float(value)
                if value.is_integer():
                    value = int(value)
            except ValueError:
                return 0
        if value == float('NaN'):
            return 0
        return value
