###Programa que recebe a posição inicial e final de um cavalo, 
###e printa se essa movimentação é válida ou não dentro de um tabuleiro 8x8.

##Definido como válido o movimento em "L", ou seja, movimento de
##2 casas na coluna e 1 na linha OU 1 casa na coluna e 2 na linha.

def xadrez():
    #recebe a entrada do usuário para posição inicial e final e coloca em minusculo para não gerar erro
    xi, xf = input().lower().split()
    tab_num="12345678" #tabuleiro de xadrez para a coluna
    tab_let="abcdefgh" #tabuleiro de xadrez para a linha

    ##confere se a posição inicial é inválida
    if(xi[0] not in tab_let or xi[1] not in tab_num):
        return "INVÁLIDO"
    ##confere se a posição final é inválida
    if(xf[0] not in tab_let or xf[1] not in tab_num):
        return "INVÁLIDO"

    ##variáveis auxiliares para encontrar a subtração (em módulo) entre duas posições
    sub_let=abs(ord(xi[0])-ord(xf[0])) #subtrai as letras do alfabeto entre pos. inicial e pos. final
    sub_num=abs(ord(xi[1])-ord(xf[1])) #subtrai os numeros entre pos. inicial e pos. final

    ##confere se o movimento é válido conforme a definição
    if((sub_let==2 and sub_num==1) or (sub_let==1 and sub_num==2)):
        return "VÁLIDO"
    else:
        return "INVÁLIDO"

print(xadrez())