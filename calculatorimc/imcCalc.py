# Calculator of IMC.
# Written by Tiago Coelho
# Email: tiagocoelho100h@gmail.com
# Date: 2018/05/18 13:54:52

# funções
# functions:

# função que coleta dados do usuario:
# function that collects user data:
def coletaDados():
    name = input('Nome:  ')
    genre = input('Genero M - Masculino, F - Feminino: ')
    age = input('Idade: ')
    weight =float( input('Peso em Kg: '))
    height =float( input('Altura em Cm: '))
    return (name, genre, age, weight, height)

# função que gerencia o resultado.
# function that maneges the result.
def resultadoAdulto(i):
    if x < 16:
        print('Seu Indice de Massa Corporal é: ', x)
        print('Você está na faixa de Magreza grave.')
    elif x >= 16 and x < 17:
        print('Seu Indice de Massa Corporal é: ', x)
        print('Você está na faixa de Magreza moderada.')
    elif x >= 17 and x < 18.5:
        print('Seu Indice de Massa Corporal é: ', x)
        print('Você está na faixa de Magreza leve.')
    elif x >= 18.5 and x < 25:
        print('Seu Indice de Massa Corporal é: ', x)
        print('Você está na faixa de Saudavel.')
    elif x >= 25 and x < 30:
        print('Seu Indice de Massa Corporal é: ', x)
        print('Você está na faixa de Sobre peso.')
    elif x >= 30 and x < 35:
        print('Seu Indice de Massa Corporal é: ', x)
        print('Você está na faixa de Obesidade grau I.')
    elif x >= 35 and x < 40:
        print('Seu Indice de Massa Corporal é: ', x)
        print('Você está na faixa de Obesidade grau II (severa).')
    elif x >= 40:
        print('Seu Indice de Massa Corporal é: ', x)
        print('Você está na faixa de Obesidade grau III (mórbida).')
    else:
        print('Algo está errado!')

# loop principal
# main loop:
print('Welcome to IMC calculator. by Tiago Coelho | tiagocoelho100h@gmail.com')
l = 's'
while l == 's':
    name, genre, age, weight, height = coletaDados()
    print(name, genre, age, weight, height)
    height = height/100
    x = weight/(height*height)
    resultadoAdulto(x)
    l = input('Realizar uma nova consulta? (s - sim, n - não) ')
    if l == 's':
        print('')
        print('------ Nova consulta -------')
        print('')
    elif l == 'n':
        print('')
        print('Programa encerrado.')
        print('')
    else:
        print('')
        print('Erro fatal.')
        print('Programa encerrado.')