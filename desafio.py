#Calculo de bonus com entrada do usuario
BONUS_2024 = 1000
#Tratamento erros nome
try:
    nome = input("Digite seu nome: ")
    if nome.isdigit():
        raise ValueError("Nome inválido. Não pode conter numeros.")
    elif len(nome.strip()) == 0:
        raise ValueError("Nome inválido. Não pode ser vazio.")
    else:
        print(f"Nome: {nome}.")
except ValueError as e:
    print(e)        

#Traramento erros salario
try:
    salario = float(input("Qual seu salario? "))
    if salario < 0:
        raise ValueError("Salário inválido. digite apenas valores positivos.")
except ValueError:
    print("Salário inválido. digite apenas numeros.")

#Tratamento erros bonus
try:
    bonus_percent = float(input("Qual o valor do bonus recebido? "))
    if bonus_percent < 0:
        print("Bonus inválido. digite apenas valores positivos.")
    total_bonus = (salario * bonus_percent) + BONUS_2024
    print(f"{nome}, seu bonus sera de: {total_bonus}")
except ValueError:
    print("Bonus inválido. digite apenas numeros.")
