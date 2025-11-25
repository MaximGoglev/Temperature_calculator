import sys
import time
import threading
import os
from colorama import init

init()
os.system('cls' if os.name == 'nt' else 'clear')

# Конвертация температур
def c_to_f(celsius):
    return celsius * 9 / 5 + 32

def f_to_c(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

def c_to_k(celsius):
    return celsius + 273.15

def k_to_c(kelvin):
    return kelvin - 273.15

def f_to_k(fahrenheit):
    return (fahrenheit - 32) * 5 / 9 + 273.15

def k_to_f(kelvin):
    return (kelvin - 273.15) * 9 / 5 + 32

# Логотип
logo = [
"████████╗███████╗███╗   ███╗██████╗ █████╗ ██████╗  █████╗ ████████╗██╗   ██╗██████╗ ███████╗",
"╚══██╔══╝██╔════╝████╗ ████║██╔══██╗██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝██║   ██║██╔══██╗██╔════╝",
"   ██║   █████╗  ██╔████╔██║██████╔╝███████║██████╔╝███████║   ██║   ██║   ██║██████╔╝█████╗  ",
"   ██║   ██╔══╝  ██║╚██╔╝██║██╔══██╗██╔══██║██╔══██╗██╔══██║   ██║   ██║   ██║██╔══██╗██╔══╝  ",
"   ██║   ███████╗██║ ╚═╝ ██║██║  ██║██║  ██║██║  ██║██║  ██║   ██║   ╚██████╔╝██║  ██║███████╗",
"   ╚═╝   ╚══════╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚══════╝",
"",
" ██████╗ █████╗ ██╗      ██████╗██╗   ██╗██╗      ██╗   ██╗ █████╗ ████████╗ ██████╗ ██████╗ ",
"██╔════╝██╔══██╗██║     ██╔════╝██║   ██║██║      ██║   ██║██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗",
"██║     ███████║██║     ██║     ██║   ██║██║      ██║   ██║███████║   ██║   ██║   ██║██████╔╝",
"██║     ██╔══██║██║     ██║     ██║   ██║██║      ██║   ██║██╔══██║   ██║   ██║   ██║██╔══██╗",
"╚██████╗██║  ██║███████╗╚██████╗╚██████╔╝███████╗ ╚██████╔╝██║  ██║   ██║   ╚██████╔╝██║  ██║",
" ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚══════╝  ╚═════╝ ╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝",
]

colors = ["31", "33", "32", "36", "34", "35"]

def rainbow_char(c, index):
    return f"\033[{colors[index % len(colors)]}m{c}\033[0m"

# Анимация логотипа
def animate_logo(stop_event):
    shift = 0
    while not stop_event.is_set():
        for i, row in enumerate(logo):
            sys.stdout.write(f"\033[{i+1};1H")  # курсор в строку i
            line = "".join(rainbow_char(ch, j + shift) for j, ch in enumerate(row))
            sys.stdout.write(line + "\033[K")
        sys.stdout.flush()
        shift = (shift + 1) % len(colors)
        time.sleep(0.1)

# Запуск анимации
stop_event = threading.Event()
thread = threading.Thread(target=animate_logo, args=(stop_event,), daemon=True)
thread.start()

# Ожидание Enter от пользователя
input("\nНажмите Enter, чтобы начать программу...")

# Остановка анимации
stop_event.set()
thread.join()

# Очистка области под программой
print("\n" * 2)

# Основная программа
print("Добро пожаловать в Temperature Calculator!")
print("Выберете величину ввода:")
print("1. Градусы Цельсия")
print("2. Градусы Фаренгейта")
print("3. Кельвины")
input_1 = int(input("->: "))

print("\n")
x = float(input("Введите температуру ->: "))
print("\n")

print("Выберете величину вывода:")
print("1. Градусы Цельсия")
print("2. Градусы Фаренгейта")
print("3. Кельвины")
input_2 = int(input("->: "))

print("\n")
print("Результат:")

if input_1 == 1:
    if input_2 == 1:
        print(x)
    elif input_2 == 2:
        print(c_to_f(x))
    elif input_2 == 3:
        print(c_to_k(x))
    else:
        print("Неверный выбор ввода!")
elif input_1 == 2:
    if input_2 == 1:
        print(f_to_c(x))
    elif input_2 == 2:
        print(x)
    elif input_2 == 3:
        print(f_to_k(x))
    else:
        print("Неверный выбор ввода!")
elif input_1 == 3:
    if input_2 == 1:
        print(k_to_c(x))
    elif input_2 == 2:
        print(k_to_f(x))
    elif input_2 == 3:
        print(x)
    else:
        print("Неверный выбор ввода!")
else:
    print("Неверный выбор ввода!")
