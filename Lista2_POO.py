
# Exercício 1
# Número posítivo ou negativo: Peça ao usuário um número e informe se ele é positivo, negativo ou zero.

numero = float(input('Digite um número: '))

if numero > 0:
    print('O número é positivo.')
elif numero == 0:
    print('O número é zero.')
else:
    print('O número é negativo.')


# Exercício 2
# Maioridade: Peça a idade do usuário e informe se ele é maior de idade (18 anos ou mais).

idade = int(input('Digite sua idade: '))

if idade >= 18:
    print('Você é maior de idade.')
else:
    print('Você é menor de idade.')


# Exercício 3
# Par ou Impar: Peça  um número ao usuário e informe se é par ou impar.

numero = int(input('Digite um número: '))

if numero % 2 == 0:
    print('O número é par.')
else:
    print('O número é ímpar.')


# Exercício 4
# Número maior: Peça ao usuário dois números e informe qual é o maior.

numero = float(input('Digite um número: '))
numero2 = float(input('Digite outro número: '))

if numero > numero2:
    print('O primeiro número é maior.')
elif numero == numero2:
    print('Os números são iguais.')
else:
    print('O segundo número é maior.')


# Exercício 5
# Desconto de compra: Peça ao usuário o valor de uma compra. Se o valor for maior que 100, aplique um desconto de 10%. Caso contrário, exiba o valor sem desconto.

valor_da_compra = float(input('Digite o valor da compra: '))
if valor_da_compra > 100:
    valor_com_desconto = valor_da_compra - (valor_da_compra* 0.10)
    print(f'O valor da compra com desconto é de R${valor_com_desconto:.2f}')
else:
    print(f'O valor da compra sem desconto é de R${valor_da_compra:.2f}')


# Exercício 6
# Verificar múltiplo: Peça ao usuário um número e verifique se ele é múltiplo de 5.

numero = int(input("Digite um número: "))
if numero % 5 == 0:
    print(f"{numero} é múltiplo de 5.")
else:
    print(f"{numero} não é múltiplo de 5.")


# Exercício 7
# Calculo de média: Peça três notas ao usuário e calcule a média. 
#Se a média for maior ou igual a 7, informe que o aluno foi aprovado, senão reprovado.

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
nota3 = float(input('Digite a terceira nota: '))

media = (nota1 + nota2 + nota3) / 3
if (nota1 + nota2 + nota3) / 3 >= 7:
    print(f'Mostre a média: {media:.2}')
    print('O aluno foi Aprovado')
else:
    print(f'Mostre a média: {media:.2}')
    print('O Aluno foi Reprovado')


# Exercício 8
#Senha correta: Crie um programa que peça a senha do usuário. 
#Se a senha for "python123_EFG", exiba "Acesso permitido". Caso contrário, "Senha incorreta".

senha = input('Digite a senha: ')
if senha == 'python123_EFG':
    print('Acesso permitido')
else:
    print('Senha incorreta')


# Exercício 9
# Entrada gratuita: Peça ao usuário sua idade e informe se ele tem direito a entrada gratuita
# (idade menor que 5 anos ou maior que 60 anos).

idade = int(input('Digite sua idade: '))
if idade < 5 or idade > 60:
    print('Você tem direito a entrada gratuita.')
    print(f'Sua idade é {idade} anos.')
    print('Aproveite!')
else:
    print('Você não tem direito a entrada gratuita.')
    print(f'Sua idade é {idade} anos.')
    print('Aproveite!')


# Exercício 10
# Verificar nota: Peça uma nota entre 0 e 10 ao usuário.
# Se o valor for inválido, exiba uma mensagem de erro.

nota = float(input('Digite uma nota entre 0 e 10: '))
if nota >= 0 and nota <= 10:
    print(f'A nota é {nota}.')
    print('O Valor da nota é válida.')
else:
    print(f'A nota é {nota}.')
    print('Valor da nota é inválido.')


# Exercício 11
# Categoria de idade: 
# Peça a idade do usuário e informe se ele é "Criança" (menos de 12 anos),
# "Adolescente" (entre 12 e 17 anos) ou "Adulto" (entre 18 ou mais).

idade = int(input('Digite sua idade: '))
crianca = idade < 12
adolescente = idade >= 12 and idade <= 17
adulto = idade >= 18
if crianca:
    print(f'Sua idade é {idade} anos.')
    print('Você é uma Criança.')
elif adolescente:
    print(f'Sua idade é {idade} anos.')
    print('Você é um Adolescente.')
elif adulto:
    print(f'Sua idade é {idade} anos.')
    print('Você é um Adulto.')


# Exercício 12
# Maior de três números:
# Peça três números ao usuário e informe qual é o maior.

n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
n3 = float(input('Digite o terceiro número: '))

if n1 > n2 and n1 > n3:
    print('O maior número é n1.')
elif n2 > n1 and n2 > n3:
    print('O maior número é n2.')
else:
    print('O maior número é n3.')


# Exercício 13
# Divisão segura:
# Peça dois números ao usuário e divida o primeiro pelo segundo.
# Se o segundo for zero, informe que a divisão não é possível.

n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))

if n2 == 0:
    print('A divisão não é possível.')
    
else:
    divisao = n1 / n2
    print('A divisão é possível.')
    print(f'O resultado da divisão é {divisao}.')


# Exercício 14
# Número dentro de intervalo:
# Peça ao usuário um número  e verifique se ele está entre 10 e 50.

n1 = float(input('Digite um número: '))

if n1 >= 10 and n1 <= 50:
    print('O número está entre 10 e 50.')
    print(f'O número é {n1}')
else:
    print('O número não está entre 10 e 50.')
    print(f'O número é {n1}')
    

# Exercício 15
# Aprovado, recuperação ou reprovado:
# Peça a média do aluno e informe se ele está "Aprovado" (média>=7), "Em recuperação" (5 <= média < 7) ou "Reprovado" (média < 5).

nota1 = float(input('Digite a nota1: ')) 
nota2 = float(input('Digite a nota3: '))
nota3 = float(input('Digite a nota3: '))

media = (nota1+nota2+nota3)/3
print(f'A média é: {media:.2f}')

if media >= 7:
    print('Aluno está Aprovado')
elif media >= 5 and media < 7:
    print('Aluno está Em recuperação')
else:
    print('Aluno está Reprovado')

# Exercício 16
# Calcular o IMC:
# Peça ao usuário o peso e a altura, calcule o IMC informe se ele está "Abaixo do peso" (IMC < 18,5),
# "Peso normal" (18,5 >= IMC < 25), "A cima do peso" (IMC >= 25).

peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
IMC = peso / altura **2
print(f'O IMC é {IMC:.2f}')
if IMC < 18.5:
    print('Abaixo do peso')
elif IMC >= 18.5 and IMC < 25:
    print('Peso normal')
else:
    print('Acima do peso')

# Exercício 17
# Identificar o triângulo:
# Peça ao usuário três lados e verifique se eles podem formar um triângulo. 
# Caso possam, informe se o triângulo é "Equilátero", "Isósceles" ou "Escaleno".

lado1 = float(input('Digite o comprimento do primeiro lado: '))
lado2 = float(input('Digite o comprimento do segundo lado: '))
lado3 = float(input('Digite o comprimento do terceiro lado: '))

if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:
    if lado1 == lado2 == lado3:
        tipo_triangulo = 'Equilátero'  # Todos os lados iguais
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        tipo_triangulo = 'Isósceles'  # Dois lados iguais
    else:
        tipo_triangulo = 'Escaleno'  # Todos os lados diferentes

    print(f'Os lados formam um triângulo {tipo_triangulo}.')


# Exercício 18
# Login e senha:
# Peça o ao usuário um nome de usuário e senha.
# Verifique se o nome de usuário é "admin" e a senha é "1234".
# Caso ambos estejam corretos, informe "Login bem-sucedido".

nome_de_usuario = input('Digite seu nome de usuário: ')
senha = input('Digite sua senha: ')

if nome_de_usuario == 'admin' and senha == '1234':
    print('Login bem-sucedido')
    print('Seja Bem-vindo')
else:
    print('Nome de usuário ou senha incorretos')


# Exercício 19
# Verificar a maioridade para dirigir:
# Peça a idade do usuário e verifique se ele pode dirigir (18 anos ou mais).
# Se tiver menos de 18, informe quantos anos faltam para ele dirigir.

idade = int(input('Digite sua idade: '))

if idade >= 18:
    print('Você pode dirigir.')
else:
    anos_faltando = 18 - idade
    print(f'Você ainda não pode dirigir. Faltam {anos_faltando} anos para você dirigir.')
    
