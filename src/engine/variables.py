"""
Handles the variable and list class

TODO Fix mod for NaN values
"""

import math


class Value:
    """Represents a value and handles operations"""

    __slots__ = ('value', )

    def __init__(self, value):
        if isinstance(value, Value):
            value = value.value
        self.value = value

    # Casting methods
    def __float__(self):
        try:
            value = float(self.value)

            # NaN should return 0
            if math.isnan(value):
                return 0.0

            # Python has more inf casts than JS
            if math.isinf(value) and not isinstance(self.value, float) and \
                    self.value not in ('Infinity', '+Infinity', '-Infinity'):
                return 0.0

            return value

        except ValueError:
            try:
                # Convert values like '0xFF'
                return float(int(self.value, base=0))
            except ValueError:
                return 0.0

    def __str__(self):
        try:
            return str(int(self.value))
        except ValueError:
            # Give float nan proper case
            # if isinstance(self.value, float) and math.isnan(self.value):
            #     return 'NaN'

            return str(self.value)
        except OverflowError:
            if self.value == float('inf'):
                return 'Infinity'
            return '-Infinity'

    def __bool__(self):
        if isinstance(self.value, float) and math.isnan(self.value):
            return False
        if str(self.value).lower() == 'false':
            return False
        if self.value == 0 or self.value == '0':
            return False
        return bool(self.value)

    def __round__(self, digits=0):
        try:
            return round(float(self.value), digits)
        except ValueError:
            return 0

    def __index__(self):
        try:
            return int(float(self.value))
        except ValueError:
            return 0
        except OverflowError:
            return 0

    # Math operators
    def __add__(self, other):
        return self.__float__() + float(other)

    def __radd__(self, other):
        return float(other) + self.__float__()

    def __sub__(self, other):
        return self.__float__() - float(other)

    def __rsub__(self, other):
        return float(other) - self.__float__()

    def __mul__(self, other):
        return self.__float__() * float(other)

    def __rmul__(self, other):
        return float(other) * self.__float__()

    def __truediv__(self, other):
        try:
            return self.__float__() / float(other)
        except ZeroDivisionError:
            # Handle zero division
            if self.__float__() == 0:
                return Value(float('nan'))
            return math.copysign(float('inf'), self.__float__())

    def __rtruediv__(self, other):
        try:
            return float(other) / self.__float__()
        except ZeroDivisionError:
            # Handle zero division
            if float(other) == 0:
                return Value(float('nan'))
            return math.copysign(float('inf'), float(other))

    def __mod__(self, other):
        return self.__float__() % float(other)

    def __rmod__(self, other):
        return float(other) % self.__float__()

    def __pow__(self, other):
        return pow(self.__float__(), float(other))

    def __rpow__(self, other):
        return pow(float(other), self.__float__())

    # Comparison operators
    def __eq__(self, other):
        return self.__str__().lower() == str(other).lower()

    def __ne__(self, other):
        return self.__str__() != str(other)

    def __lt__(self, other):
        if isinstance(other, Value):
            other = other.value

        try:
            return float(self.value) < float(other)
        except ValueError:
            return str(self.value).lower() < str(other).lower()

    def __gt__(self, other):
        if isinstance(other, Value):
            other = other.value

        try:
            return float(self.value) > float(other)
        except ValueError:
            return str(self.value).lower() > str(other).lower()

    def __le__(self, other):
        if isinstance(other, Value):
            other = other.value

        try:
            return float(self.value) <= float(other)
        except ValueError:
            return str(self.value).lower() <= str(other).lower()

    def __ge__(self, other):
        if isinstance(other, Value):
            other = other.value

        try:
            return float(self.value) >= float(other)
        except ValueError:
            return str(self.value).lower() >= str(other).lower()


class Variable(Value):
    """Represents a variable"""

    __slots__ = ('shown', )

    def __init__(self, value, shown):
        super().__init__(value)
        self.shown = shown

    def __get__(self, instance, owner=None):
        return self

    def __set__(self, instance, value):
        self.value = value

    def __repr__(self):
        return f"Variable(value={repr(self.value)}, shown={bool(self.shown)})"

    def show(self):
        """Show the variable"""
        self.shown = True
        print(self)

    def hide(self):
        """Hide the variable"""
        self.shown = False


print()
