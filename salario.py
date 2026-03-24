salario = float("1652.90")

gastos = float(input("Quanto você gastou hoje?: "))

saldo = salario - gastos 

while saldo >= 0:
    print(f"Seu saldo atual é de: R${float(saldo):.2} ")
    gasto_hoje = float(input("Quanto você gastou hoje?"))

    saldo -= gasto_hoje

if saldo > 0:
    input("Oque você comprou hoje?")
else:
    print("Ixi, acabou o seu dinheiro! Ou você pode estar devendo")

print(f"O mês finalmente chegou ao fim! Seu saldo é de: R${float(saldo):.2}.")


