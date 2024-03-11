def common_elements():
    # Генеруємо список чисел, кратних 3
    multiples_of_3 = [i for i in range(1, 101) if i % 3 == 0]
    # Генеруємо список чисел, кратних 5
    multiples_of_5 = [i for i in range(1, 101) if i % 5 == 0]

    # Створюємо множини з цих списків
    set_of_multiples_of_3 = set(multiples_of_3)
    set_of_multiples_of_5 = set(multiples_of_5)

    # Знаходимо перетин множин
    common_elements_set = set_of_multiples_of_3.intersection(set_of_multiples_of_5)

    return common_elements_set

# Виклик функції та виведення результату
result = common_elements()
print("Спільні елементи:", result)