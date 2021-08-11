##Programa que recebe números inteiros em loop até encontrar “f”,
##calcula a média aritmética dos números recebidos e os printa na tela.

number = 0; #recebe os números do usuário;
count = 0; #armazena a quantidade de números;
total = 0; #soma os números do usuário;

print("Digite os números seguidos de 'enter' | Parar digite 'f':")
while (True):
    number = input()
    if(number=="f"): #estopim de parada
        break
    total+=int(number)
    count+=1

total/=count #calcula a média aritmética
print("A média é:", total) 