numero1 = int(input("Selecione um numero: "))

numero2 = int(input("escolha outro numero: "))



conta = (numero1 + numero2) % 2 

if conta == 0:
    print("Seu numero é par")
else:
    print("Seu numero é impar")

