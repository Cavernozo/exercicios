atividadeA = int(input("Informe os dias para a atividade A: "))
atividadeB = int(input("Informe os dias para a atividade B: "))
atividadeC = int(input("Informe os dias para a atividade C: "))

if atividadeA < 0 or atividadeB < 0 or atividadeC < 0:
    print("ERRO, os dias não podem ser negativos!")

else:
    print(f"total de {atividadeA + atividadeB + atividadeC} Dias para conclusão do projeto!")