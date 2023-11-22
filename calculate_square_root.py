from math import sqrt

message = 'Добро пожаловать в самую лучшую программу для вычисления ' \
          'квадратного корня из заданного числа'
print(message)


def calculate_square_root(Number):
    """Вычисляет квадратный корень."""
    return sqrt(Number)


def calc(your_number):
    """Принемает и проверяет число, выводит ответ."""
    if your_number <= 0:
        return
    answer = calculate_square_root(your_number)
    print(f'Мы вычислили квадратный корень '
          f'из введённого вами числа. '
          f'Это будет: {answer}')


calc(25.5)
