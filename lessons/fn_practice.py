"""Example function to learn definition and calling syntax"""

def my_max(number1: int, number2: int) -> int:
    """Returns the maximum value out of two numbers"""
    if number1 >= number2:
        return number1
    else: #number1 < number2
        return number2

max_number: int = my_max(1,10)
print(max_number)
other_max_number: int = my_max(3,11)
print(other_max_number)