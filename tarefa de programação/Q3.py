import math
#Programa que recebe do usuário um número com duas casas decimais que representa um valor monetário
##e calcula (e printa) o menor número de notas e moedas possíveis no qual o valor pode ser decomposto.

notas = [100,50,20,10,5,2,1,0.50,0.25,0.10,0.05,0.01] ##array para armazenar as notas
result = [0,0,0,0,0,0,0,0,0,0,0,0] ##array para armazenar a quantidade de notas

number = float(input()) ##recebe o input do usuário em float

##loop para percorrer cada nota do array
for i in range(len(notas)):
    if(number>=notas[i]): #confere se o numero é divisível pela nota correspondente em cada loop
        
        qntd_notas = int(number/notas[i]) #calcula o numero de notas máximo para o numero em questão
        result[i] = qntd_notas #armazena em um array a quantidade achada para cada nota

        number = number - (qntd_notas*notas[i]) #subtrai essas notas do numero

#loop auxiliar para printar o resultado em moedas e notas
for i in range(len(result)):
    if(i<6):
        if(i==0):
            print("\nNOTAS:")
        print("{} nota(s) de R${}".format(result[i],notas[i]))
    
    else:
        if(i==6):
            print("\nMOEDAS:")
        print("{} moeda(s) de R${}".format(result[i],notas[i]))