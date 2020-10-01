import os
import time

def clear():
    if os.name == "NT" or "nt":
        os.system("cls")
    else:
        os.system("clear")


def calc(num1, num2, sign):
    return f"{num1}{sign}{num2}"


def main():
    num1 = int(input("Введите первое число:"))
    num2 = int(input("Введите второе число:"))
    sign = (input("Введите знак:"))
    if sign in ["-", "+", "/", "*", "**"]:
        print("Ответ: ", calc(num1=num1, num2=num2, sign=sign))
    else:
        print("Ошибка: заданное значение переменной sign не находится в signs!")
        time.sleep(3)
        clear()
        main()


if __name__ == "__main__":
    main()
