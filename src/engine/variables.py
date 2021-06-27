"""
Handles the variable and list class

Custom types for:
    float
    str
"""

__all__ = ('Float', 'Str')

import math


class Float(float):
    """Represents a value of the float type"""

    __slots__ = ('value',)

    def __new__(cls, value):
        try:
            # Try to cast the value to float
            instance = float.__new__(cls, value)

            # NaN should be treated as 0
            if math.isnan(instance):
                return float.__new__(cls, 0)

            return instance

        except ValueError:
            try:
                # Try to cast numbers of alternate base
                return float.__new__(cls, (int(value, base=0)))
            except ValueError:
                # Default to 0
                return float.__new__(cls, 0)

    def __init__(self, value):
        float.__init__(self)
        self.value = value

    def __str__(self):
        # Check if self.value is float NaN
        # If it is, return 'NaN' rather than 'nan'
        if self == 0 and isinstance(self.value, float) and math.isnan(self.value):
            return 'NaN'

        # Return the correct case for float Inf too
        if math.isfinite(self):
            if self > 0:
                return 'Infinity'
            return '-Infinity'

        # If an integer, ommit the '.0'
        integer = int(self)
        if integer != self:
            return str(self)

        return str(integer)

    def __index__(self):
        try:
            # Floors the value
            return int(self)
        except ValueError:
            # Caused if self == float('nan')
            return 0
        except OverflowError:
            # Caused if self == float('inf')
            return 0

    def __truediv__(self, other):
        # TODO What if other is 'inf'?
        try:
            return float(self) / float(other)
        except ValueError:
            return Float('Infinity' if self > 0 else '-Infinity')
        except ZeroDivisionError:
            return Float('Infinity' if self > 0 else '-Infinity')

    def __rtruediv__(self, other):
        return Float(other) / self


class Str(str):
    """Represents a value of the str type"""

    __slots__ = ('value',)

    def __new__(cls, value):
        return str.__new__(cls, value)

    def __bool__(self):
        if self == '' or self.lower() == 'false' or self == '0':
            return False
        return True

    # Float() should be called instead
    # def __float__(self):
    #     try:
    #         value = float(str(self))

    #         # NaN should be treated as 0
    #         if math.isnan(value):
    #             return 0.0

    #         # JS has fewer inf strings than Python
    #         if math.isinf(value) and self not in ('Infinity', '+Infinity', '-Infinity'):
    #             return 0.0

    #         return value

    #     except ValueError:
    #         try:
    #             # Try to cast numbers of alternate base
    #             return float(int(self, base=0))
    #         except ValueError:
    #             return 0.0

    # float and int fall back to this if defined
    # def __index__(self):
    #     try:
    #         return int(float(self))

    #     except OverflowError:
    #         return 0

    #     except ValueError:
    #         try:
    #             return int(self, base=0)
    #         except ValueError:
    #             return 0

    def __getitem__(self, i):
        return str.__getitem__(self, i + 1)

    def __eq__(self, other):
        try:
            return float(self) == float(other)
        except ValueError:
            return self.lower() == str(other).lower()

    def __ne__(self, other):
        try:
            return float(self) != float(other)
        except ValueError:
            return self.lower() != str(other).lower()

    def __lt__(self, other):
        try:
            return float(self) < float(other)
        except ValueError:
            return self.lower() < str(other).lower()

    def __gt__(self, other):
        try:
            return float(self) > float(other)
        except ValueError:
            return self.lower() > str(other).lower()

    def __le__(self, other):
        try:
            return float(self) <= float(other)
        except ValueError:
            return self.lower() <= str(other).lower()

    def __ge__(self, other):
        try:
            return float(self) >= float(other)
        except ValueError:
            return self.lower() >= str(other).lower()
