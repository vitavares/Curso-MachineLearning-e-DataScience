#Efetuar o cálculo da quantidade de litros de combustível gasto em uma viagem,
#utilizando um automóvel que faz 12 Km por litro. Para obter o cálculo, o usuário deve fornecer o 
#tempo gasto na viagem e a velocidade média durante ela. Desta forma, será possível obter a distância 
#percorrida com a fórmula DISTANCIA = TEMPO * VELOCIDADE. Tendo o valor da distância, basta calcular a 
#quantidade de litros de combustível utilizada na viagem, com a fórmula: LITROS_USADOS = DISTANCIA / 12.
#O programa deve apresentar os valores da velocidade média, tempo gasto na viagem, a distância percorrida 
#e a quantidade de litros utilizada na viagem.

tempo = float(input('Tempo de viagem (horas): '))
v_media = float(input('Velocidade média(km/h): '))

distancia = tempo*v_media
litros = distancia/12

print('\nVelocidade média: ', v_media, 'KMs/H')
print('Tempo de viagem: ', tempo, 'h')
print('Distância percorrida: ', round(distancia, 2), 'KMs')
print('Combustivel gasto: ', round(litros, 2), 'litros')