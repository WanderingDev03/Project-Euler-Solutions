from sys import set_int_max_str_digits
def fibonacci(n: int):
    a, b = 0, 1
    for i in range(n):
        temp = a+b
        a = b
        b = temp

    return b
