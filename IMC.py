Peso = int(input("Qual o seu peso (Exemplo: 100) ? "))
Altura = float(input("Qual a sua altura em cm (Exemplo: 1.75) ? "))
IMC = Peso / (Altura * Altura)
print(f"Seu peso é {Peso} Kg, sua altura {Altura}, e o seu IMC é {IMC}")
if IMC < 18.5:
    print("Você está abaixo do peso")
elif IMC >= 18.5 and IMC <= 24.9:
    print("Seu Peso está normal")
elif IMC >= 25 and IMC <= 29.9:
    print("Você está com Pré-obesidade")
elif IMC >= 30 and IMC <= 34.9:
    print("Você está com Obesidade Grau 1")
elif IMC >= 35 and IMC <= 39.9:
    print("Você está com Obesidade Grau 2")
elif IMC >= 40:
    print("Você está com Obesidade Grau 3")
else:
    print("Deu ruim")
