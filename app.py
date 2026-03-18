

n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
opcao = 0 

while opcao != 5:
    print('''
    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos numeros 
    [5] sair do programa''')
    opcao = int(input('>>>>>Qual a sua opção? '))
    if opcao == 1:
        escolha = n1 + n2
        print(f'O valor de sua conta deu {escolha}')
    elif opcao == 2:
        escolha = n1 * n2
        print(f'O valor de sua multiplicação deu {escolha}')
    elif opcao == 3:
        if n1 > n2:
            print(f'O maior numero é {n1}')
        else:
            print(f'O maior numero é {n2}')
    elif opcao == 4:
        n1 = int(input('Digite o primeiro numero: '))
        n2 = int(input('Digite o segundo numero: '))
    elif opcao == 5:
        print('Encerrando o programa...')
        opcao = 5
    else:
        print('opção inválida, tente novamente: ') 