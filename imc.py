peso = int(input("Digite seu peso(kg): "))
altura = float(input("Digite sua altura(m): "))

imc = peso/(altura**2)

if imc < 18.5:
    print(f"Seu imc é {imc} \nVocê está abaixo do peso!")
elif 18.5 <= imc < 25:
    print(f"Seu imc é {imc} \nPeso normal!")
else:
    print(f"Seu imc é {imc} \nVocê está acima do peso!")