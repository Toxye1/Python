nome = input("Digite seu nome: ")
valor = float(input("Qual é o valor da venda: R$ "))


if valor > 4999.99:
    gold = (valor * 7 // 100)
    print(f'O valor do desconto é: R$ {gold}')
    valorLiquido =  (valor - gold)
    print(f'O valor líquido a pagar é: R$ {valorLiquido}')
elif valor > 1999.99 and valor < 5000.00:
    silver = (valor * 5 // 100)
    print(f'O valor do desconto é: R$ {silver}')
    valorLiquido =  (valor - silver)
    print(f'O valor líquido a pagar é: R$ {valorLiquido}')
elif valor > 999.99  and valor < 2000.00:
    bronze = (valor * 3 // 100)
    print(f'O valor do desconto é: R$ {bronze}')
    valorLiquido =  (valor - bronze)
    print(f'O valor líquido a pagar é: R$ {valorLiquido}')
else:
    print(f'Sem desconto')
    valorLiquido = valor
    print(f'O valor líquido a pagar é: R$ {valorLiquido}')

    