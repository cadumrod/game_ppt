import random


while True:
    print("### Bem-vindo ao Pedra, papel e tesoura! ###")
    jogador = input("Digite o nome do jogador: ")

    print()
    print(jogador.capitalize())
    opcoes = ['pedra', 'papel', 'tesoura']
    escolha_bot = random.choice(opcoes)

    escolha_jogador = input("Escolha entre - Pedra | Papel | Tesoura: ")


    # Se opcao nao existir
    while escolha_jogador not in opcoes:
        print("Escolha apenas entre as opções disponíveis!")
        print()
        print(jogador.capitalize())
        escolha_jogador = input("Escolha entre - Pedra | Papel | Tesoura: ")

    
    # Verificação de escolhas
    if escolha_jogador == escolha_bot:
        print (f"Empate... O bot escolheu {escolha_bot.capitalize()}.\n")
    elif (escolha_jogador == 'pedra' and escolha_bot == 'tesoura') or \
         (escolha_jogador == 'papel' and escolha_bot == 'pedra') or \
         (escolha_jogador == 'tesoura' and escolha_bot == 'papel'):
        print(f"Você venceu... O bot escolheu {escolha_bot.capitalize()}.\n")
    else:
        print(f"Você perdeu... O bot escolheu {escolha_bot.capitalize()}.\n")