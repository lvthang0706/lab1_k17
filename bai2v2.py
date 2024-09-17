
class Integer:
    def __init__(self, value):
        self.value = value

    def from_float(cls, value):
        if not isinstance(value, float):
            return "value is not a float"
        return cls(int(value))

    def from_roman(cls, value):
        roman_to_int = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = 0
        prev_value = 0
        for char in reversed(value):
            int_val = roman_to_int[char]
            if int_val < prev_value:
                result -= int_val
            else:
                result += int_val
            prev_value = int_val
        return cls(result)

    def from_string(cls, value):
        if not isinstance(value, str) or not value.isdigit():
            return "wrong type"
        return cls(int(value))

    def add(self, integer):
        if not isinstance(integer, Integer):
            return "number should be an Integer instance"
        return self.value + integer.value

first_num = Integer(10)
second_num = first_num.from_roman("IV")
print(first_num.from_float("2.6"))
print(first_num.from_string(2.6))
print(first_num.add(second_num))
