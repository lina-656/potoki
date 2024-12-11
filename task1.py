import random

def task1():
    """Меню первого задания."""
    while True:
        print("\nЗадание 1: Сумма двух массивов")
        print("Введите массивы вручную или введите 'exit' для выхода.")

        arr1_input = input("Введите элементы первого массива через пробел: ")
        if arr1_input.lower() == 'exit':
            break
        
        arr2_input = input("Введите элементы второго массива через пробел: ")

        arr1 = list(map(int, arr1_input.split()))
        arr2 = list(map(int, arr2_input.split()))

        if len(arr1) != len(arr2):
            print("Массивы должны быть одинакового размера.")
            continue

        arr1.sort(reverse=True)  # Убывание
        arr2.sort()               # Возрастание

        result = [0 if a == b else a + b for a, b in zip(arr1, arr2)]
        
        result.sort()  # Сортировка результата
        print("Результат:", result)  # Выводим итоговый массив
