idade = int(input("Qual a sua idade?: "))
estudante = str(input("Você é estudante? (sim/nao): "))
preço_total = 40

if idade <= 18 or estudante == "sim":
    preço = preço_total / 2 
    print(f"A sua meia entrada foi aplicada!! você irá pagar: {float(preço):.1f}")
else:
    preço = preço_total
    print(f"Valor a pagar, R$", preço)