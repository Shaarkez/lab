# Лабораторная работа №7 - Система контроля версий

print("(изменено через Локально) ===")
print("Система контроля версий Git")

def sum_two_numbers(a, b):
    \"\"\"Функция суммирования двух чисел\"\"\"
    return a + b

def multiply_two_numbers(a, b):
    \"\"\"Функция умножения двух чисел\"\"\"
    return a * b

# Тест функции
if __name__ == "__main__":
    print("5 + 7 =", sum_two_numbers(5, 7))
    print("6 * 8 =", multiply_two_numbers(6, 8))

# Изменения для пункта 6 лабораторной работы
print("Пункт 6 выполнен: изменения внесены локально и отправлены на GitHub")
# 2. Добавляем изменения в main.py

# Изменения в отдельной ветке (5.6)
def divide_two_numbers(a, b):
    """Функция деления двух чисел"""
    if b == 0:
        return "Ошибка: деление на ноль"
    return a / b

print("Новая функция divide_two_numbers добавлена в ветке feature/advanced-calculator")