preco = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO 
      [1] á vista dinheiro/cheque
      [2] á vista cartão
      [3] 2x no cartão
      [4] 3x ou mais no cartão''')
opcao = int(input('Qual opção você escolhe? '))

if opcao == 1:
    total1 = preco - (preco * 10 / 100)
    print(f'Sua compra fica no valor total de {total1:.2f}R$')
    print('com desconto de 10%')

elif opcao == 2: 
    total2 = preco - (preco * 5 /100)
    print(f'sua compra fica no valor total de {total2:.2f}R$')
    print('Com desconto de 5%')

elif opcao == 3:
    total3 = preco / 2 
    print(f'Sua compra fica {total3:.2f}R$ com 2 parcelas')
    print('Sem juros')

elif opcao == 4:
    parcelas = int(input('Quantas parcelas você quer? '))
    total4 = preco + (preco * 20 / 100)
    valor_parcelas = total4 / parcelas
    print('sua compra terá juros de 20%')
    print(f'Sua compra fica com parcelas de: {valor_parcelas:.2f}R$')
    print(f'Valor total com o juros: {total4:.2f}')

else:
    print('OPÇÃO INVÁLIDA')

