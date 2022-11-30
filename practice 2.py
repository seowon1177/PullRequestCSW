def printMenu():
    print("1. 사칙연산")
    print("2. 도움말")
    print("3. 종료")

def calculator():
    isRuning = True
    num1 = 0
    num2 = 0
    opr = '+'

    while isRuning:
       select = int(input("메뉴 선택 : "))

       if select == 1:
           print("사칙연산")
           num1 = int(input("num1: "))
           num2 = int(input("num2: "))
           opr = input("opr: ")
           if opr == '+':
               print(num1+num2)
           elif opr == '-':
               print(num1-num2)
           elif opr == '*':
               print(num1*num2)
           elif opr == '/':
               print(num1/num2)
       elif select == 2:
           print("도움말")
       elif select == 3:
           print("종료")
           isRuning = False
       else:
           print("입력이 잘못됨.")

if __name__ == "__main__":
    printMenu()
    calculator()
