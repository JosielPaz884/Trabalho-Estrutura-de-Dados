from Calculadora import*

def menu():
    try:
        print("-------------------------")
        print("\033[0;34mBEM VINDO AO MENU PRINCIPAL\033[m")
        print("1. Calcular uma expressão")
        print("2. Sair do sistema")
        opc = int(input("Digite a ação que deseja realizar: "))
    except ValueError:
        print("Você não digitou uma opção válida!")
        return menu()
    return opc

def main():
    opc = 0

    while opc != 2:
        opc = menu()
        if opc == 1:
            expression= str(input("Digite a Expressão: "))
            result = calculate(expression)
            print(f'Resultado: {result}')

if __name__== '__main__':
    main()
