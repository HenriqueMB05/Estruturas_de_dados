import os

def limpar():
    return os.system("cls" if os.name == "nt" else "clear")

def primerio_passo():
    print("Hello, world!")


def receber_entrada():
    nome = input("Digite seu nome: ")
    print(f"Bom dia {nome}")


def tipos_basicos():
    idade =25 # Integer
    print(f"Idade = {idade} -> Integer")
    altura =1.75 # Float
    print(f"Altura = {altura} -> Float")
    name = "Alice" # String
    print(f"Nome = {name} -> String")
    eh_maior_de_idade = True # Boolean
    print(f"É maior de idade = {eh_maior_de_idade} -> Boolean")


def operacoes_basicas():
    # Matematica
    x = 10+5  # Soma
    print(f"Soma = {x}")
    y = 10-2  # Subtração
    print(f"Subtração = {y}")
    z = 10*3  # Multiplicação
    print(f"Multiplicação = {z}")
    w = 10/2  # Divisão
    print(f"Divisão = {w}")
    u = 10//3 # Resto da divisão
    print(f"Resto da divisão = {u}")

    # Concatenação de String
    nome_completo = "Aline" + " " + "Souza"
    print(f"Contatenação de String\n{nome_completo}")


def estruturas_de_controle():
    #if elif else
    temperatura =10
    if temperatura>25:
        print("Dia quente")
    elif temperatura> 15:
        print("Dia agradavel")
    else:
        print("Dia frio!")
    
    # for while 
    # Loop for
    contar = 0
    for i in range(5):
        print(i, end=' ');
    
    # Loop while
    print("\nConte", end=" ")
    while contar<5:
        print(f"{contar} ", end=" ")
        contar +=1


chc =0
while chc != 6:
    print("Digite qual função você quer usar: ")
    print('''[1] - Primeiros passos
[2] - Receber entrada
[3] - Tipos básicos
[4] - Operações básicas
[5] - Estruturas de controle
[6] - Sair''')
    chc = int(input(">>> "));
    match chc:
        case 1:
            primerio_passo()
            input()
            limpar()
        case 2:
            receber_entrada()
            input()
            limpar()
        case 3:
            tipos_basicos()
            input()
            limpar()
        case 4:
            operacoes_basicas()
            input()
            limpar()
        case 5:
            estruturas_de_controle()
            input()
            limpar()