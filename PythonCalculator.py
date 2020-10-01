def main(num1, num2, sign):
    if sign == "+":
        print(num1+num2)
    elif sign == "-" :
        print (num1-num2)
    elif sign == "*" :
        print(num1*num2)
    elif sign == "/" :
        print(num1/num2)
    else:
        print("Error: Try again!")

        
if __name__ == "__main__":
    number1 = int(input("Введите первое число:"))
    number2 = int(input("Введите второе число:"))
    sign = (input("Введите знак:"))
    main(num1=number1, num2=number2, sign=sign)
