import random 
 
def input_large_number_array(prompt): 
    """Ввод массива чисел вручную.""" 
    return list(map(int, input(prompt).split())) 
 
def generate_large_number_array(size): 
    """Генерация случайного массива чисел.""" 
    return [random.randint(0, 9) for _ in range(size)] 
 
def sum_arrays(array1, array2): 
    """Суммирует два массива.""" 
    max_length = max(len(array1), len(array2)) 
    array1 = array1 + [0] * (max_length - len(array1)) 
    array2 = array2 + [0] * (max_length - len(array2)) 
    return [a + b for a, b in zip(array1, array2)] 
 
def subtract_arrays(array1, array2): 
    """Вычитает второй массив из первого.""" 
    max_length = max(len(array1), len(array2)) 
    array1 = array1 + [0] * (max_length - len(array1)) 
    array2 = array2 + [0] * (max_length - len(array2)) 
    return [a - b for a, b in zip(array1, array2)] 
 
def task1_operations(array1, array2, operation): 
    """Выполняет операцию сложения или вычитания массивов.""" 
    if operation == '+': 
        result = sum_arrays(array1, array2) 
        print(f"Результат суммы: {result}") 
    elif operation == '-': 
        result = subtract_arrays(array1, array2) 
        print(f"Результат разности: {result}") 
 
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
         
        result = [] 
        for a, b in zip(arr1, arr2): 
            if a == b: 
                result.append(0)  # Если числа совпадают 
            else: 
                result.append(a + b)  # Иначе добавляем их сумму 
         
        result.sort()  # Сортировка результата 
        print("Результат:", result)  # Выводим итоговый массив 