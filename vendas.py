vendas1 = int(input("Digite a quantidade de maçãs vendidas: "))
vendas2 = int(input('Digite o numero de bananas vendidas: '))

if vendas1 == vendas2:
    print("houve empate!")
elif vendas1 > vendas2:
    print("As maçãs tiveram mais vendas!")
else:
    print("As bananas tiveram mais vendas!")