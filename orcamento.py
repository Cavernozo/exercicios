limite = 3000
gastos = float(input("Digite o total de despesas do mês(R$): "))

if gastos >= limite:
    print(f"Atenção! Você ultrapassou o limite do orçamento.")
else:
    print("Ainda está dentro do orçamento.")