#Calcular a média de um aluno que cursou a disciplina de Programação I, a partir da leitura das notas M1, 
#M2 e M3; passando por um cálculo da média aritmética. Após a média calculada,
#devemos anunciar se o aluno foi aprovado, reprovado ou pegou exame
# - Se a média estiver entre 0.0 e 4.0, o aluno está reprovado
# - Se a média estiver entre 4.1 e 6.0, o aluno pegou exame
# - Se a média for maior do que 6.0, o aluno está aprovado
# - Se o aluno pegou exame, deve ser lida a nota do exame. Se a nota do exame for maior do que 6.0, está aprovado, senão; está reprovado

m1 = float(input('Nota M1: '))
m2 = float(input('Nota M2: '))
m3 = float(input('Nota M3: '))

media = (m1+m2+m3)/3

if media>=0.0 and media<=4.0:
    print('\nO aluno está reprovado.')
elif media>=4.1 and media<=6.0:
    print('\nO aluno pegou exame.')
    n_exame = float(input('\nNota do exame: '))
    res = 'aprovado' if n_exame>6.0 else 'reprovado'
    print('\nO aluno está', res)
elif media>6.0:
    print('\nO aluno está aprovado.')