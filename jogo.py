import os
tabuleiro = [" "] * 9
jogador_atual = "X"
# def = Define uma função
# Uma função é um bloco de código que faz algo
# Se precisa fazer a mesma coisa várias vezes, cria uma função

# Exemplo:
# def nome_da_funcao():
#     código aqui

# Depois é só chamar:
# nome_da_funcao()

def clean():
    os.system('cls')


def exibir_tabuleiro():
    print(f"{tabuleiro [0]} | {tabuleiro [1]} | {tabuleiro [2]}")
    print("-------------")
    print(f"{tabuleiro [3]} | {tabuleiro [4]} | {tabuleiro [5]}")
    print("-------------")
    print(f"{tabuleiro [6]} | {tabuleiro [7]} | {tabuleiro [8]}")

while True:
    clean()
    exibir_tabuleiro()
    
    # 1. Primeiro criamos a variável 'posicao'
    posicao = int(input(f"Vez do {jogador_atual}. Escolha (0-8): "))
    
    # 2. Agora o Python já sabe o que é 'posicao' e pode testar:
    if posicao < 0 or posicao > 8:
        print("Número fora do limite! Escolha entre 0 e 8.")
    elif tabuleiro[posicao] != " ":
        print("Essa posição já está ocupada!")
    else:
        # Se chegou aqui, a jogada é válida
        tabuleiro[posicao] = jogador_atual
        jogador_atual = "O" if jogador_atual == "X" else "X"

    





