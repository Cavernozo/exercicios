hr = int(input("Digite a hora atual (formato 24 horas): "))

if hr < 8 or hr > 18:
    print("Acesso negado!")

else:
    print("acesso permitido!")