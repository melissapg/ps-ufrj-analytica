##Programa que lê um arquivo de texto (Texto.txt), lista todas as palavras únicas 
#(sem diferenciar upper e lowercase) e sua frequência no texto. No final, printa este conteúdo.

f = open("TextoQ4.txt", 'r', encoding = 'utf8') #abre o arquivo para leitura
texto = f.readlines() #lê e amarzena o arquivo.txt em linhas terminadas em '\n'
f.close #fecha o arquivo

palavras = [] #array que armazenará as palavras do texto separadas
for linha in texto:
    #tira os caracteres "?!,:\n" do texto, coloca tudo em minusculo e separa cada palavra em uma posição do array
    palavras += linha.replace('?', '').replace('!', '').replace(',','').replace(':','').replace('\n','').lower().split(' ')

palavras_unicas = [] #array para as palavras únicas
frequencia = [] #array para a frequência das palavras únicas

#percorre todas as palavras do texto
for palavra in palavras:
    if (palavra not in palavras_unicas): #verifica se a palavra atual não está no array de palavras únicas
        palavras_unicas.append(palavra) #adiciona essa palavra no array de palavras únicas
        frequencia.append(palavras.count(palavra)) #e conta a frequência dela no texto, adicionando ao array de frequencias 

#loop auxiliar para printar as palavras e suas frequências
for i in range(len(frequencia)):
    print("{}:{}".format(palavras_unicas[i], frequencia[i]))