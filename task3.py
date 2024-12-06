# task3.py
def rotate_matrix(matrix):
    """
    Поворачивает матрицу на 90 градусов против часовой стрелки.

    :param matrix: Исходная матрица (список списков).
    
    :return: Новая матрица, повернутая на 90 градусов.
    """
    
    return [list(reversed(col)) for col in zip(*matrix)]

def task3():
    """
    Выполняет задание 3: Поворот матрицы.

     Запрашивает у пользователя ввод матрицы и направление поворота,
     затем выполняет поворот матрицы и выводит результат.
     
     - Направление поворота может быть "по часовой стрелке" или "против часовой стрелки".
     - В случае неверного направления выводится сообщение об ошибке.
     - Результат выводится в виде повернутой матрицы.
     """
    
    print("Задание 3: Поворот матрицы")

    rows = int(input("Введите количество строк матрицы: "))
    cols = int(input("Введите количество столбцов матрицы: "))
   
    matrix = []
   
    for i in range(rows):
       row = list(map(int, input(f"Введите элементы строки {i + 1} через пробел: ").split()))
       matrix.append(row)

    direction = input("Введите направление поворота (по часовой стрелке/против часовой стрелки): ")
   
    if direction.lower() == "по часовой стрелке":
       matrix = rotate_matrix(matrix)
       matrix = rotate_matrix(matrix)  
       matrix = rotate_matrix(matrix)
       
    elif direction.lower() == "против часовой стрелки":
       matrix = rotate_matrix(matrix)
       
    else:
       print("Неверное направление поворота.")
       return

    print("Повернутая матрица:")
    for row in matrix:
       print(" ".join(map(str, row)))