import os
import sys
import time


# ФУНКЦИИ КОНВЕРТАЦИИ ТЕМПЕРАТУР

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



# ЛОГОТИП

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
    color = colors[index % len(colors)]
    return f"\033[{color}m{c}\033[0m"


def print_with_animation():
    os.system("cls" if os.name == "nt" else "clear")

    for row in logo:
        for i, ch in enumerate(row):
            sys.stdout.write(rainbow_char(ch, i))
            sys.stdout.flush()
            time.sleep(0.002)
        print()
        time.sleep(0.02)



# ОСНОВНАЯ ПРОГРАММА

def main():
    # Показать логотип
    print_with_animation()
    input("\nНажмите ENTER, чтобы продолжить...")

    # Логика калькулятора
    print("Добро пожаловать в Temperature Calculator!")
    print("Выберете величину ввода:")
    print("1. Градусы Цельсия")
    print("2. Градусы Фаренгейта")
    print("3. Кельвины")
    input_1 = int(input("->: "))

    x = float(input("Введите температуру ->: "))

    print("Выберете величину вывода:")
    print("1. Градусы Цельсия")
    print("2. Градусы Фаренгейта")
    print("3. Кельвины")
    input_2 = int(input("->: "))

    print("Результат:")

    if input_1 == 1:
        if input_2 == 1:
            print(x)
        elif input_2 == 2:
            print(c_to_f(x))
        elif input_2 == 3:
            print(c_to_k(x))
        else:
            print("Неверный выбор!")

    elif input_1 == 2:
        if input_2 == 1:
            print(f_to_c(x))
        elif input_2 == 2:
            print(x)
        elif input_2 == 3:
            print(f_to_k(x))
        else:
            print("Неверный выбор!")

    elif input_1 == 3:
        if input_2 == 1:
            print(k_to_c(x))
        elif input_2 == 2:
            print(k_to_f(x))
        elif input_2 == 3:
            print(x)
        else:
            print("Неверный выбор!")

    else:
        print("Неверный выбор ввода!")

if __name__ == "__main__":
    main()
