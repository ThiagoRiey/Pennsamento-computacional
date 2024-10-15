import time

def introducao():
    print("""
 ____                            _           _          __
| __ )  ___ _ __ ___      __   _(_)_ __   __| | ___     \_\_
|  _ \ / _ \ '_ ` _ \ ____\ \ / / | '_ \ / _` |/ _ \   / _` |
| |_) |  __/ | | | | |_____\ V /| | | | | (_| | (_) | | (_| |
|____/ \___|_| |_| |_|      \_/ |_|_| |_|\__,_|\___/   \__,_|
 ____    _    ___  _   _   _    ____  _____ __  __    _      ____   ____
/ ___|  / \  / _ \| | | | / \  |  _ \| ____|  \/  |  / \    |  _ \ / ___|
\___ \ / _ \| | | | | | |/ _ \ | |_) |  _| | |\/| | / _ \   | | | | |
 ___) / ___ \ |_| | |_| / ___ \|  _ <| |___| |  | |/ ___ \  | |_| | |___
|____/_/   \_\__\_\\___/_/   \_\_| \_\_____|_|  |_/_/   \_\ |____/ \____|
""")
    print("Você é um herói que sempre se mete em situações hilariantes.")
    print("Prepare-se para rir e tomar decisões que afetarão o seu destino!")
    print("==========================================\n")
    time.sleep(2)
    cena1()

def cena1():
    print("Cena 1: O dragão espirituoso")
    print("Você está andando pela floresta e de repente encontra um dragão.")
    escolha = input("Você (A) tenta negociar com o dragão ou (B) corre como um covarde? ").lower()

    if escolha == "a":
        print("Você: Olá, Sr. Dragão, gostaria de fazer um acordo?")
        print("Dragão: Hmmm, você parece engraçado. Qual é a oferta?")
        print("Você: Ofereço-lhe um suprimento vitalício de chocolate.")
        print("Dragão: Chocolate? Isso é inusitado! Aceito o acordo.")
        print("Você saiu dessa situação com sucesso!")
        cena2()
    elif escolha == "b":
        print("Você corre como um covarde e tropeça em uma árvore.")
        print("Dragão: HAHA! Você é hilário! Vou deixar você ir desta vez.")
        print("Você saiu dessa situação com sorte, mas não dignidade.")
        cena2()
    else:
        print("Escolha inválida. Tente novamente.")
        cena1()

def cena2():
    print("\nCena 2: A ponte instável")
    print("Você chegou a uma ponte que parece muito instável.")
    escolha = input("Você (A) tenta atravessá-la ou (B) procura outra rota? ").lower()

    if escolha == "a":
        print("Você decide tentar atravessar a ponte.")
        print("A ponte desaba e você cai na água.")
        print("Você emerge molhado e coberto de lama, mas pelo menos está inteiro!")
        cena3()
    elif escolha == "b":
        print("Você decide procurar outra rota e encontra um caminho seguro.")
        print("Você evitou um desastre iminente!")
        cena3()
    else:
        print("Escolha inválida. Tente novamente.")
        cena2()

def cena3():
    print("\nCena 3: O encontro com o feiticeiro atrapalhado")
    print("Você encontra um feiticeiro que está tendo problemas com seus feitiços.")
    escolha = input("Você (A) tenta ajudar o feiticeiro ou (B) sai correndo? ").lower()

    if escolha == "a":
        print("Você: Posso ajudar com alguma coisa?")
        print("Feiticeiro: Ah, você é um anjo! Preciso de ajuda com meu feitiço de levitação.")
        print("Você tenta ajudar, mas acidentalmente o feiticeiro levita sua própria cabeça!")
        print("Feiticeiro: Meu Deus, o que aconteceu?!")
        print("Você não conseguiu ajudar muito, mas pelo menos foi engraçado!")
        cena_final()
    elif escolha == "b":
        print("Você sai correndo do feiticeiro e acaba se perdendo na floresta.")
        print("Depois de muito tempo, você encontra o caminho de volta para casa.")
        cena_final()
    else:
        print("Escolha inválida. Tente novamente.")
        cena3()

def cena_final():
    print("\nParabéns! Você sobreviveu às Aventuras Cômicas do Herói Desajeitado.")
    print("Esperamos que você tenha se divertido e rido bastante!")
    replay = input("Deseja jogar novamente? (sim/não) ").lower()
    if replay == "sim":
        introducao()
    else:
        print("Obrigado por jogar!")

# Iniciar o jogo
introducao()
