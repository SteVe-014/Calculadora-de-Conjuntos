###_JOÃO PEDRO CORREIA_###

#EU FIZ DUAS FUNÇÕES PARA VALIDAÇÃO DOS NÚMEROS, SENDO UMA PARA NÚMEROS NATURAIS E OUTRA PARA NÚMEROS INTEIROS.
#ESSA FUNÇÃO VALIDA NÚMEROS NATURAIS, SE OS DIGITOS INSERIDOS SÓ APRESENTAM NÚMEROS. PARA ISSO É RECEBIDO OS CARACTERES EM STRING E ASSIM É AVALIADO SE SÓ TEM NÚMERO OU SE TEM ALGUM SÍMBOLO OU LETRA NO MEIO. RETORNANDO "True" SE SÓ TIVER NÚMEROS E "False" PARA QUALQUER OUTRA COISA NO MEIO.
def inserirValorNatural():
    natural=str(input("->"))
    #<isdigit> É UMA FUNÇÃO QUE VERIFICA SE OS CARACTERES DA VARIAVEL <natural> SÃO SOMENTE NÚMEROS. RETORNANDO 'True' OU 'False'.
    while(natural.isdigit()==False): 
        print("Inválido")
        natural=str(input("->"))
    return int(natural)

#NESSA FUNÇÃO É AVALIADO SE OS CARACTERES INSERIDOS SÃO ALGUM NÚMERO PERTECENTE AOS INTEIROS. EU UTILIZO BASICAMENTE A TÉCNICA QUE EU USEI NOS NÚMEROS NATURAIS, MAS PERMITO QUE O SÍMBOLO "-" POSSA SER INSERIDO SOMENTE UMA VEZ. 
#TEM UM bug PRESENTE EM <inserirValorInteiro()>, DEVIDO AO SINAL "-" NÃO TER UM LUGAR ESPECÍFICO PARA SER POSICIONADO. MAS É INFORMADO PARA USAREM INTEIROS.
def inserirValorInteiro():
    inteiro=str(input("->"))
    while (inteiro.replace('-','',1).isdigit()==False):
        print("Inválido")
        inteiro=str(input("->"))
    return int(inteiro)

#<acharIndice> RECEBE UM ELEMENTO E UMA LISTA. A FUNÇÃO LOCALIZA O VALOR DENTRO DO ARRAY E RETORNA SEU RESPECTIVO ÍNDICE.
# A FUNÇÃO <len()> RETORNA A QUANTIDADE DE ÍNDICES PRESENTE DENTRO DO VETOR. 
def acharIndice(vet,valor):
    for i in range(len(vet)):
        if valor==vet[i]:
            return i

#<inserirValoresArray()> É USADA PARA ADICIONAR VALORES DENTRO DOS CONJUNTOS "A" E "B". É VERIFICADO SE O VALOR JÁ NÃO ESTÁ PRESENTE DENTRO DO CONJUNTO, CASO ESTEJA, É APRESENTADO UMA MENSAGEM DE ERRO E É PEDIDO NOVAMENTE UM NÚMERO. 
def inserirValoresArray(qntd,vetor):
    print("Insira valores inteiros!")
    print("\nInsira os valores")
    while(qntd!=0):
        n=inserirValorInteiro()
        while(n in vetor):#ESSE <while():> VERIFICA SE JÁ NÃO TEM VALOR IGUAL DENTRO DO ARRAY.
            print("Inválido")
            n=inserirValorInteiro()

        vetor.append(n)
        qntd-=1

#A PARTIR DAQUI COMEÇA AS FUNÇÕESQUE REALIZAM AS OPERAÇÕES DE CONJUNTO. EM CADA UMA (COM EXCEÇÃO DO <inserirElementos>) EU ADICIONEI UM TERCEIRO VETOR COM O NOME <vet> E SEMPRE É RETORNADO O VETOR PARA QUE SEJA REALIZADO O PRINT.

#FUNÇÃO DO MENU 1.
#A FUNÇÃO É USADA PARA INSERIR ELEMENTOS DENTRO DOS CONJUNTOS "A" E "B". PARA TAL, É PEDIDO O NÚMERO DE VALORES QUE O USUÁRIO DESEJA INSERIR E POSTERIORMENTE É PERGUNTADO QUAIS SÃO ESSE VALORES.
def inserirElementos(conjunto):
    print("Quantidade dos elementos")
    qntd=inserirValorNatural()
    inserirValoresArray(qntd,conjunto)

#FUNÇÃO DO MENU 2.
#É CRIADO UM TERCEIRO ARRAY <vet> PARA REALIZAR A UNIÃO ENTRE OS CONJUNTOS "A" E "B". ESSE NOVO VETOR RECEBE OS VALORES DO CONJUNTO "B" E VERIFICA QUAIS ELEMENTOS DO CONJUNTO "A" ESTÃO EM "B",CASO SENJA IGUAL, O CONTADOR É ADICIONA +1 E NÃO É FEITO NADA, CASO NÃO ENCONTRE, É ADICIONADO EM <vet>. LOGO QUE REINICIADO O LOOP, O CONTADOR VOLTA A 0.
def uniao(conjuntoA,conjuntoB,vet):
    vet+=conjuntoB
    for i in (conjuntoA):
        cont=0
        for e in (conjuntoB):
            if (i==e):
                cont+=1
                break
        if(cont==0):
            vet.append(i)
    return vet

#MENU 3
#REALIZA A INTERSEÇÃO ENTRE OS CONJUNTOS "A" E "B". VERIFICA QUAIS ELEMENTOS SÃO IGUAIS NOS DOIS CONJUNTOS E ADICIONA A UM NOVO ARRAY.
def intersecao(conjuntoA,conjuntoB,vet):
    for i in (conjuntoA):
        for e in (conjuntoB):
            if(i == e):
                vet.append(i)#ADICIONA UM VALOR DENTRO DA LISTA <vet>.
                break
    return vet

#MENU 4
#MENU 5
#FAZ A DIFERENÇA ENTRE OS CONJUNTOS. A REPRESENTAÇÃO DESSA FUNÇÃO PODE SER ESCREVER COMO, (conjunto1 - conjunto2). 
# É ADICIONADO OS VALORES PERTENCENTE AO <conjunto1> A UM NOVO VETOR. É VERIFICADO QUAIS OS ELEMENTOS DE <vet> TAMBÉM PERTENCEM AO <conjunto2>, CASO TENHA, É LOCALIZADO O ÍNDICE DENTRO DE <vet> E RETIRADO.   
def diferenca(conjunto1, conjunto2,vet):
    vet+=conjunto1
    for i in conjunto2:
        for e in vet:
            if(i==e):
                numIgual=acharIndice(vet,e)
                del(vet[numIgual])
    return vet

#MENU 6
#A DIFERENÇA SIMÉTRICA ADICIONA OS VALORES DO CONJUNTO "A" A <vet>. 
# UTILIZA DE UM CONTADOR PARA SABER SE UM ELEMENTO TAMBÉM PERTENCE AO <conjuntoB>, CASO TAMBÉM PERTENÇA, É ADICIONADO +1, LOGO, É LOCALIZADO O ÍNDICE DO VALOR E RETIRADO DO TERCEIRO VETOR. CASO O CONTADOR PERMANESSA 0, SÓ É ADICIONADO O NOVO VALOR.
def diferencaSimetrica(conjuntoA,conjuntoB,vet):
    vet+=conjuntoA
    for e in (conjuntoB):
        cont=0
        for i in vet:
            if (i==e):
                cont+=1
                break
        if(cont==0):
            vet.append(e)
        else:
            numIgual=acharIndice(vet,i)
            del(vet[numIgual])
    return vet

#MENU 7
#NA MULTIPLICAÇÃO DOS CONJUNTOS, FIZ UM FOR DENTRO DE OUTRO FOR, ONDE, <a> RECEBE OS VALORES PERTENCENTES AO <conjuntoA> E <e> RECEBE OS VELEMENTOS PERTENCENTES AO <conjuntoB>. É ENVIADO PARA CADA COMBINAÇÃO POSSIVEL DE <a> E <e> PARA DENTRO DO VETOR <vet> COM PARÊNTESES DIVIDINDO CADA COMBINAÇÃO. <(a,e)>. 
def multiplicacao(conjuntoA,conjuntoB,vet):
    for a in conjuntoA:
        for e in conjuntoB:
            vet.append([a,e])
    return vet
    
    

###CÓDIGO PRINCIPAL###
a=[] #CONJUNTO A
b=[] #CONJUNTO B
cc=[] #CONJUNTO NOVO
rodar=1

#INFORMAÇÕES APRESENTADAS NO COMEÇO DO PROGRAMA!
print("\nINFORMAÇÕES \n-Cada opção da calcuadora vai estar com seu respectivo valor ao lado!")
print("-Insira esse valor na opção 'Menu' para rodar determinada função.")
print("-Insira somente valores inteiros (I) nos conjuntos A e B")

#LOOP DO PROGRAMA, É REALIZADO PARA QUE O USUÁRIO POSSA SAIR QUANDO SESEJAR DO PROGRAMA.
while(rodar!=0):
    input("\n[Aperte Enter]")
    print("\n\n__CALCULADORA DE CONJUNTOS__")
    print("1- Inserir elementos em A e B")
    print("2- A \u222A B")
    print("3- A \u2229 B")
    print("4- A - B")
    print("5- B - A")
    print("6- A \u0394 B")
    print("7- A x B")
    print("0- Sair")

    menu=int(input("\nMenu: "))
    #!NO PYTHON <else if> É ABREVIADO PARA <elif>!
    #CONDIÇÕES PARA DETERMINAR O QUE VAI SER REALIZADO NA CALCULADORA DEPENDENDO DO VALOR QUE O USUÁRIO DIGITOU NO MENU
    if menu==1:
        a=[]
        b=[]
        print("\n\nConjunto A")
        inserirElementos(a)
        print("\n\nConjunto B")
        inserirElementos(b)
    elif menu==2:
        uni=uniao(a,b,cc)
        print("\nA \u222A B = ",end='')
        print(uni)
    elif menu==3:
        inter=intersecao(a,b,cc)
        print("\nA \u2229 B = ",end='')
        print(inter)
    elif menu==4:
        sub1=diferenca(a,b,cc)
        print("\nA - B = ",end='')
        print(sub1)
    elif menu==5:
        sub2=diferenca(b,a,cc)
        print("\nB - A = ",end='')
        print(sub2)
    elif menu==6:
        simetrico=diferencaSimetrica(a,b,cc)
        print("\nA \u0394 B = ",end='')
        print(simetrico)
    elif menu==7:
        matriz=multiplicacao(a,b,cc)
        print(matriz)
    else:
        rodar=0

    cc.clear()#ISSO LIMPA A LISTA <cc> PARA QUE ELA NÃO FIQUE "SUJA" QUANDO FOR CHAMADA POR OUTRA FUNÇÃO