"""Faça um programa que peça para oo usuario para digitar
um número inteiro, informe se este número é par ou impar.
Caso o usuário não digite um número inteiro, informe que
não é um número inteiro.
"""


# MEU CÓDIGO
# num = int(input ('Digite um número inteiro: '))
# try:
#     if num %2 == 0:
#         print (f'O numero {num} é par.')  

#     else:
#         print(f'O numero {num} é impar.')

# except ValueError:
    
#     print(f'Este numero {num} não é um numero inteiro')


# entrada = input("Digite um número: ")

# try:
#     # Tenta converter para inteiro
#     num = int (entrada)
#     if num % 2 == 0:
#         print(f"O número {num} é par.")
#     else:
#         print(f"O número {num} é ímpar.")
# except ValueError:
#     try:
#         # Se não for inteiro, tenta converter para float
#         num = float(entrada)
#         print(f"O número {num} é decimal, não um inteiro.")
#     except ValueError:
#         # Se não for float, é texto
#         print(f"'{entrada}' não é um número.")  

"""Faça um programa que pergunte a hora ao usuário e, 
baseando-se no horário descrito, exiba a saudação apropriada. Ex. Bom dia 0-11,
 Boa tarde 12-17 e Boa noite 18-23. """

# try:
#     horas = int (input('Que horas são? '))
#     if horas >= 0 and horas <= 11:
#         print('Bom dia.')
#     elif horas >=12 and horas<= 17:
#         print('Boa tarde.') 
#     elif horas >=18 and horas<=23:
#         print('Boa noite. ')
#     else:
#         print ('Esse horario não existe.')
# except ValueError:
#     print ('Você não digitou um horario. ')

"""Faça um programa que peça o primeiro nome do usuario. Se o nome tiver 4 letras ou menos escreva
"Seu nomeé curto"; se tiver entre 5 e 6 letras, escreva Seu nome é normal; se for mais que 6 letras
escreva seu nome é muito grande """

nome = input ('Digite o seu nome: ')
tamanho = len(nome)

if tamanho > 1:
    if tamanho <=4:
        print('Seu nome é curto')
    elif tamanho >=5 and tamanho <=6:
        print('Seu nome é normal')
    else:
        print('Seu nome é muito grande')

else:
    print('Digite mais de uma letra.' )