import string
import random
import re
##VARIÁVEIS
thislist=string.ascii_lowercase
list1=[' ','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9']
listMorse=[' ','.-','-...','-.-.','-..','.','..-.','--.','....','..','.--.','-.-','.-..','--','-.','---','.--.','--.-','.-.','...','-','..-','...-','.--','-..-','-.--','--..','-----','.----','..---','...--','....-','.....','-....','--...','---..','----.']
i=0
k=0
traduzida=""
##FUNÇÕES
#Verifica se existe algum número na string
def temNumero(frase):
    '''
    Recebe a frase e verifica se algum dos dígitos é um número, se for a variável num é True e entra no while.
    Continua no while até a frase não ter números
    Requires: frase seja string
    Ensures: return a frase sem números
    '''
    num=any(string.isdigit() for string in frase)
    while num==True:
        frase=input("Escreva a frase que deseja traduzir apenas com letras: ")
        num=any(string.isdigit() for string in frase)
    return frase
#Verifica se é a frase é maior que 4 e tira-lhe os espaços
def fraseMaiorQue4(frase):
    while len(frase)<=4:
        frase=input("Escreva a frase com mais do que 4 caracteres que deseja traduzir: ")
    i=0
    fraseArrumada=''
    while i<len(frase):
        letra=frase[i]
        if letra ==' ':
            fraseArrumada+=''
        else:
            fraseArrumada+=letra
        i+=1
    return fraseArrumada
##MENU
print(" ----------------------------------------")
print("|    Alfabeto trocado[Z-A] - 1           |")
print("|    Alfabeto numeral[A=1] - 2           |")
print("|    Alfabeto numeral[A=26] - 3          |")
print("|    Data[Chave=1984] - 4                |")
print("|    Transposto[A=V] - 5                 |")
print("|    Passa um melro[A(R)B] - 6           |")
print("|    Alf. Numeral com Chave[A=12] - 7    |")
print("|    Romano-Árabe[A=I] - 8               |")
print("|    Metades - 9                         |")
print(" ----------------------------------------")
##INPUT
linguagem=input("Introduza o número da linguagem respetiva: ")
frase=input("Escreva a frase que deseja traduzir: ")
#Linguagem 1
if(linguagem == "1"):
#Troca o alfabeto pelo alfabeto invertido
    print(frase.translate(str.maketrans("abcdefghijklmnopqrstuvwxyz","zyxwvutsrqponmlkjihgfedcba")))
#linguagem 2
if(linguagem == "2"):
#Troca o alfabeto para n?meros
#Verifica se é letra
    frase=temNumero(frase)
    while i<len(frase):
        letra=frase[i]
        if letra==' ':
            traduzida+=' '
        else:
            while letra!=thislist[k]:
                k+=1
            traduzida+=str(k+1)+"/"
        i+=1
        k=0
    print(traduzida)
#Linguagem 3
if(linguagem == "3"):
#Troca o alfabeto para números a começar no 26
#Verifica se é letra
    frase=temNumero(frase)
    while i<len(frase):
        letra=frase[i]
        thislist=string.ascii_lowercase[::-1]
        if letra==' ':
            traduzida+=letra
        else:
            while letra!=thislist[k] and letra!=' ':
                k+=1
            traduzida+=str(k+1)+"/"
        i+=1
        k=0
    print(traduzida)
#Linguagem 4
if(linguagem == "4"):
#Simula a tabela do código
    m,s,d,a=input("Introduza a data: ")
    while i<len(frase):
        letra=frase[i]
        if letra==' ':
            traduzida+=' '
        else:
            #Aumenta o k e seleciona com que parte da data este se relaciona
            while letra!=list1[k]:
                k+=1
            if k<=9:
                traduzida+=m+str(k)+" "
            elif k==10:
                traduzida+=m+"0 "
            elif k>10 and k<=19:
                k=k-10
                traduzida+=s+str(k)+" "
            elif k==20:
                traduzida+=s+"0 "
            elif k>20 and k<=29:
                k=k-20
                traduzida+=d+str(k)+" "
            elif k==30:
                traduzida+=d+"0 "
            elif k>30 and k<=36:
                k=k-30
                traduzida+=a+str(k)+" "
        i+=1
        k=0
    print(traduzida)
#Linguagem 5
if(linguagem == '5'):
#Transporta o alfabeto até "A" ser igual à letra introduzida
#Verifica se é letra
    frase=temNumero(frase)
    letraChave=input("Introduza a letra: ")
    while letraChave!=thislist[i]:
        i+=1
    chave=i
    letraChave=chave
    i=0
    j=0
    while i<len(frase):
        letra=frase[i]
        if letra==' ':
            traduzida+=' '
        else:
            while letra!=list1[j]:
                if letraChave==26:
                    letraChave=0
                letraChave+=1
                j+=1
            traduzida+=list1[letraChave]
        i+=1
        j=0
        letraChave=chave
    print(traduzida)
#Linguagem 6
if(linguagem == '6'):
#Mete letras random entre as letras da frase
    melros=int(input("Quantos melros passam?"))
    while i<len(frase):
        char=frase[i]
        traduzida+=char
        while k<melros:
            traduzida+=random.choice(string.ascii_lowercase)
            k+=1
        i+=1
        k=0
    print(traduzida)
#Linguagem 7
if(linguagem == '7'):
#Transporta o alfabeto até "A" ser o número introduzido
#Verifica se é letra
    frase=temNumero(frase)
    k=int(input("Introduza o número: "))
    chave=k
    j=0
    while i<len(frase):
        letra=frase[i]
        if letra==' ':
            traduzida+=' '
        else:
            while letra!=thislist[j]:
                k+=1
                j+=1
            traduzida+=str(k)+' '
        i+=1
        j=0
        k=chave
    print(traduzida)
#Linguagem 8
if(linguagem == '8'):
#Transforma as vogais em números romanos e retira-lhes o valor árabe(o alfabeto vai até 21)
#Verifica se é letra
    frase=temNumero(frase)
    thislist=['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
    while i<len(frase):
        letra=frase[i]
        if letra==' ':
            traduzida+=' '
        else:
            if letra == 'a':
                    traduzida+="I"+" "
            elif letra == 'e':
                traduzida+="II"+" "
            elif letra == 'i':
                traduzida+="III"+" "
            elif letra == 'o':
                traduzida+="IV"+" "
            elif letra == 'u':
                traduzida+="V"+" "
            else:
                while letra!=thislist[k]:
                    k+=1
                traduzida+=str(k+1)+" "
        i+=1
        k=0
    print(traduzida)
#Linguagem 9
if(linguagem == '9'):
#Divide a frase ao meio separando letras de 2 em 2 e junta as 2 partes
    traduzida2=''
    while i<len(frase):
        letra=frase[i]
        if letra==' ':
            letra=''
        if i%2 == 0:
            traduzida+=letra
        else:
            traduzida2+=letra
        i+=1
    print(traduzida+traduzida2)
#Linguagem 10
if(linguagem == '10'):
    #Variáveis
    #Variável que contem as posições das letras reais
    position=''
    #Variável que obtem os chars da var position
    cross=''
    l=0
    m=0
    #Retira os espaços da frase e verifica se é maior que 4
    frase=fraseMaiorQue4(frase)
    #Indica o número de linhas e colunas de acordo com o número de letras
    if len(frase)%2==0:
        n=len(frase)+2
    else:
        n=len(frase)+3
    #Conta o número de linhas e colunas
    slots=n/2-1
    #Desenha a tabela de letras
    for i in range(1,n,1):
        for j in range(1,n,1):
            if i%2!=0 or j%2!=0:
                print("+++",end='')
            else:
                #Escolhe se vai escrever uma letra verdadeira ou uma random
                rand=random.choice([True, False])
                #Se a frase ainda não foi toda lida e vai escrever uma letra verdadeira
                # ou
                #Se o número de slots que faltam ocupar é igual ao número de letras que faltam escrever
                if k<len(frase) and rand==True or slots*slots-m==len(frase)-k:
                    letra=frase[k]
                    print(' '+letra+' ',end='')
                    k+=1
                    m+=1
                    position+='1'
                elif k>=len(frase) or rand==False:
                    print(' '+random.choice(string.ascii_lowercase)+' ',end='')
                    m+=1
                    position+='0'
        print(' ')
    print('\n')
    for i in range(1,n,1):
        for j in range(1,n,1):
            if i%2!=0 or j%2!=0:
                print("+++",end='')
            else:
                cross=position[l]
                if cross=='1':
                    print(' X ',end='')
                else:
                    print('   ',end='')
                l+=1
        print(' ')
        
        #linguagem 11
        if(linguagem == "11"):
        #Troca o alfabeto para morse
        #Verifica se é letra
            frase=temNumero(frase)
            while i<len(frase):
                letra=frase[i]
                if letra==' ':
                    traduzida+=' '
                else:
                    while letra!=thislist[k]:
                        k+=1
                    traduzida+=str(listMorse[k])+"/"
                i+=1
                k=0
            print(traduzida)
