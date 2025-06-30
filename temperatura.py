temp = 25
temp_atual = int(input("Digite a temperatura atual: "))

if temp_atual > temp:
    print("Alerta! Temperatura acima do limite permitido.")
else:
    print(f"Temperatura {temp_atual}°C")