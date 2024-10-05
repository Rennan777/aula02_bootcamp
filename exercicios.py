# #### Inteiros (`int`)

# 1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.
n1 = int(input("Digite um numero inteiro: "))
n2 = int(input("Digite outro numero inteiro: "))
soma = n1 + n2
print(f"A soma de {n1} + {n2} é igual a {soma}")

# 2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.
divisor = 5
dividendo = int(input("Digite um numero inteiro: "))
resto = dividendo % divisor
print(f"O resto da divisão de {dividendo} por {divisor} é {resto}")

# 3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.
n1 = int(input("Digite um numero inteiro: "))
n2 = int(input("Digite outro numero inteiro: "))
result = n1 * n2
print(f"A multiplicação de {n1} x {n2} é igual a {result}")

# 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.
n1 = int(input("Digite um numero inteiro: "))
n2 = int(input("Digite outro numero inteiro: "))
div_inteira = n1 // n2
print(f"A divisão inteira de {n1} por {n2} é igual a {div_inteira}")

# 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.
numero = int(input("Digite um numero inteiro: "))
quadrado = numero ** 2
print(f"O quadrado de {numero} é {quadrado}")

# #### Números de Ponto Flutuante (`float`)

# 6. Escreva um programa que receba dois números flutuantes e realize sua adição.
n1 = float(input('Digite um numero real: '))
n2 =float(input('Digite outro numero real: '))
total = n1 + n2
print(f'A soma de {n1} + {n2} é igual a {total}')

# 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.
n1 = float(input('Digite um numero real: '))
n2 = float(input('Digite outro numero real: '))
media = (n1 + n2) / 2
print(f'A media de {n1} + {n2} é {media}')

# 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
base = float(input('Digite o numero base: '))
exp = float(input('Digite o expoente: '))
potencia = base ** exp
print(f'{base} elevado a {potencia} é igual a {potencia}')

# 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.
celsius = float(input('Digite a temperatuda em graus celsius: '))
fahrenheit = celsius * 1.8 + 32
print(f'{celsius} em graus celsius equivale a {fahrenheit} em graus fahrenheit')

# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.
raio = float(input('Digite o raio do circulo: '))
area = 3.14 * (raio ** 2)
print(f'A área do circulo de raio {raio} é {area}')

# #### Strings (`str`)

# 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
frase = str(input('Digite uma frase (minuscula): '))
print(frase.upper())

# 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
nome = str(input('Digite seu nome completo: '))
print(nome.lower())

# 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.
frase = str(input('Digite uma frase: '))
print(frase.strip())

# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.
data = str(input('Digite uma data no formato dd/mm/aaaa: '))
dia, mes, ano = data.split('/')
print(f'Dia {dia} do Mes {mes} do Ano {ano}')

# 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.
string1 = str(input('Digite uma string: '))
string2 = str(input('Digite outra string: '))
print(string1 + string2)

# #### Booleanos (`bool`)

# 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
exp1 = input('Digite uma expressão booleana(True/False): ')
exp2 = input('Digite outra expressão booleana(True/False): ')
result = bool(eval(exp1) and eval(exp2))
print(f'O resultado da expressão AND entre "{exp1}" e "{exp2}" é {result}')

# 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
exp1 = input('Digite uma expressão booleana(True/False): ')
exp2 = input('Digite outra expressão booleana(True/False): ')
result = eval(exp1) or eval(exp2)
print(f'O resultado da expressão OR entre "{exp1}" e "{exp2}" é {result}')

# 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
valor = eval(input('Digite um valor booleano(True/False): '))
print(f'O valor invertido é {not valor}')

# 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
numero1 = int(input("digite um numero inteiro: "))
numero2 = int(input("digite outro numero inteiro: "))
print(f'O numero {numero1} é igual ao {numero2}? R: {numero1 == numero2}')

# 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.
numero1 = int(input("digite um numero: "))
numero2 = int(input("digite outro numero: "))
print(f'O numero {numero1} é diferente ao {numero2}? R: {numero1 != numero2}')

# #### try-except e if

# 21: Conversor de Temperatura
# 22: Verificador de Palíndromo
# 23: Calculadora Simples
# 24: Classificador de Números
# 25: Conversão de Tipo com Validação
