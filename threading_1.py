import threading

# Импортируем функции из модулей
from task1 import task1
from task2 import task2
from task3 import task3

def print_menu():
    """
    Выводит меню с доступными заданиями.
    """
    while True:
        print("\nМеню:")
        print("1. Задание 1")
        print("2. Задание 2")
        print("3. Задание 3")
        print("4. Завершение работы программы")

        choice = input("Выберите пункт меню: ")

        if choice == '1':
            # Создаем и запускаем поток для выполнения задания 1
            threading.Thread(target=task1).start()
        elif choice == '2':
            # Создаем и запускаем поток для выполнения задания 2
            threading.Thread(target=task2).start()
        elif choice == '3':
            # Создаем и запускаем поток для выполнения задания 3
            threading.Thread(target=task3).start()
        elif choice == '4':
            print("Завершение работы программы.")
            break  # Выходим из цикла
        else:
            print("Неверный выбор.")  # Обработка неверного выбора

def main():
    """
    Основная функция, которая управляет потоками.
    Запускает поток для диалогового меню.
    """
    menu_thread = threading.Thread(target=print_menu)  # Создаем поток для меню
    menu_thread.start()  # Запускаем поток меню

    menu_thread.join()  # Ожидаем завершения потока меню перед выходом из программы

if __name__ == "__main__":
    main()  # Запуск основной функции при выполнении скрипта