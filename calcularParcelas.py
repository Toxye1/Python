valor = float(input("Digite o valor total da venda: "))
parcela = int(input("Digite a quantidade de parcelas: "))


valorPrimeira =  (valor // parcela) + (valor % parcela)
# print(f'Valor primeira parcela é: {valorPrimeira}')
parcelaRestante = (valor // parcela)

print(f'Parcela 1/{parcela}: {valorPrimeira}')

for i in range(parcela - 1):
    print(f'Parcela {i+2}/{parcela}: {parcelaRestante}')







