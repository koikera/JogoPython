import random

def jogar():
    print("*****************************")
    print("Bem vindo ao jogo Adivinhacao")
    print("*****************************")
    
    numero_secreto= random.randrange(1, 100)
    total_tentativas = 0
    pontos = 1000
    
    print("qual nivel de dificuldade?")
    print("(1) Facil (2)Medio (3)Dificil")
    
    nivel = int(input("Defina um nivel: "))
    
    if (nivel == 1):
        total_tentativas = 20
    elif (nivel == 2):
        total_tentativas = 10
    else:
        total_tentativas = 5
    
    for rodada in range(1, total_tentativas + 1):
        print("Tentativa {} de {}".format(rodada,total_tentativas))
        chute_str = input("Digite um numero de 1 a 100: ")
        
        print("Voce Digitou", chute_str)
        
        chute_int = int(chute_str)
        
        if (chute_int < 1 | chute_int > 100):
            print("Voce deve digitar um numero entre 1 e 100")
            continue
        
        acertou = chute_int == numero_secreto
        maior   = chute_int > numero_secreto
        menor   = chute_int < numero_secreto
        
        if (acertou):
            print("Voce Acertou e fez {} pontos!".format(pontos))
            break
        else:
            if(maior):
                print("seu chute foi maior que o numero secreto")
            elif(menor):
                 print("seu chute foi menor que o numero secreto")
            pontos_perdidos = abs(numero_secreto - chute_int)
            pontos = pontos - pontos_perdidos
                 
    print("O numero secreto era: {}".format(numero_secreto))
    print("Fim de jogo")
    
if(__name__ == "__main__"):
    jogar()
