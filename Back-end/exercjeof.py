numero1 = int(input("Digite o primeiro número inteiro: "))
numero2 = int(input("Digite o segundo número inteiro: "))

soma = numero1 + numero2

print("A soma dos dois números é:", soma)

# Programa que soma dois números inteiros

numero1 = int(input("Digite o primeiro número inteiro: "))
numero2 = int(input("Digite o segundo número inteiro: "))

soma = numero1 + numero2

print("A soma dos dois números é:", soma)


# Programa que calcula a idade do usuário

from datetime import date

ano_nascimento = int(input("Digite o ano do seu nascimento: "))

ano_atual = date.today().year

idade = ano_atual - ano_nascimento

print("Você tem", idade, "anos.")


# Programa que exibe o dobro de um número digitado pelo usuário

numero = float(input("Digite um número: "))
dobro = numero * 2
print("O dobro desse número é:", dobro)

# Programa que converte dólares para reais (cotação fixa de 5.50)

valor_dolar = float(input("Digite o valor em dólares: "))
cotacao = 5.50
valor_real = valor_dolar * cotacao
print("O valor em reais é: R$", round(valor_real, 2))
#projeto prático !!!!!#



# Programa que converte temperatura de Celsius para Fahrenheit

celsius = float(input("Digite a temperatura em Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print("A temperatura em Fahrenheit é:", round(fahrenheit, 2))



# Programa que calcula a idade com base no ano de nascimento

from datetime import date

ano_nascimento = int(input("Digite o ano do seu nascimento: "))
ano_atual = date.today().year
idade = ano_atual - ano_nascimento
print("Você tem", idade, "anos.")



# Programa que calcula a média de três notas

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media = (nota1 + nota2 + nota3) / 3
print("A média das notas é:", round(media, 2))


# Programa que calcula o IMC (Índice de Massa Corporal)

peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros: "))

imc = peso / (altura ** 2)
print("Seu IMC é:", round(imc, 2))
