import os
lista = []
os.system("cls")

while True:
    print("Digite o valor: ")
    opcao = input("[i]inserir [a]apagar [l]listar [e]ditar [s]sair: ")

    if opcao == "i":
        os.system("cls")
        valor = input("Digite o valor: ")
        lista.append(valor)
        print("Valor inserido com sucesso!!!")
        print("---------------------------------------")

    elif opcao == "a":
        os.system("cls")
        apagar = input("Qual valor que você deseja apagar?: ")

        try:
            lista.remove(apagar)
            print("Valor deletado com sucesso !!!")
            print("---------------------------------------")
        except ValueError:
            print("Valor não encontrado.")
            print("---------------------------------------")

    elif opcao == "l":
        os.system("cls")
        if len(lista) == 0:
            print("Nada para listar")
        else:
            for i, listageral in enumerate (lista):
                print("---------------------------------------")
                print(i, listageral)
        print("---------------------------------------")

    elif opcao == "e":
        os.system("cls")
        if len(lista) == 0:
            print("Nada para editar")
        else:
            index = int(input("Digite o índice do valor que deseja editar: "))
            if index < 0 or index >= len(lista):
                print("Índice inválido")
            else:
                novo_valor = input("Digite o novo valor: ")
                lista[index] = novo_valor
                print("Valor editado com sucesso !!!")
                print("---------------------------------------")
        
    elif opcao == "s":
        print("Saindo do programa...")
        break