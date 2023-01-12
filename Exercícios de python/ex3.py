#Leia a idade do usuário e classifique-o em:
# - Criança – 0 a 12 anos
# - Adolescente – 13 a 17 anos
# - Adulto – acima de 18 anos
# -Se o usuário digitar um número negativo, mostrar a mensagem que a idade é inválida

idade = int(input('Qual sua idade? '))

if idade<0:
    print('\nIdade inválida')
elif idade>=0 and idade<=12:
    print('\nCriança')
elif idade>=12 and idade<=17:
    print('\nAdolescente')
elif idade>=18:
    print('\nAdulto')
