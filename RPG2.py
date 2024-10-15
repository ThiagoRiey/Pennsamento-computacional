import time

def introducao():
    print('''
  ___  _   _ _____ ____  _____  __
 / _ \| \ | |_   _|  _ \|_ _\ \/ /
| | | |  \| | | | | |_) || | \  /
| |_| | |\  | | | |  _ < | | /  \
 \___/|_| \_| |_| |_| \_\___/_/\_\
 ''')
    print("Estamos tratando do ano de 2098, a época mais tecnológica e versátil do planeta.")
    print("Os recursos são escassos nesse tempo. Por isso, cientistas de todo o mundo se reuniram para criar uma substância capaz de transformar mortais em seres aprimorados que não sentem fome, sede, frio ou calor.")
    print("Entretanto, para atingir esse nível, são necessárias pelo menos duas doses dessa substância.")
    print("A tal substância, agora nomeada de 'ONTRIX,' começa a ser produzida, e são produzidos poucos lotes.")
    print("Esse benefício seria incrível se não fosse pela mesquinhez e pelo egoísmo sujo do capitalismo, que prevalecem até hoje.")
    time.sleep(4)
    cena1()

def cena1():
    print("\nCena 1: A escassez de ONTRIX")
    print("Muitas pessoas e famílias estão morrendo devido à escassez de ONTRIX.")
    print("Sua tribo luta diariamente para sobreviver, e a situação é desesperadora.")
    print("Você se revolta com a falta de humanidade e decide que irá atrás das doses de ONTRIX.")
    print(''' Você revoltado

                                                     .:===-:
                                                :++++====----====.
                                             .**++====-----------=+=
                                           :#*+++===-----:::-------==+
                                          *#**++=-----:::::::::-----==+.
                                         =##**+==---:::::::::::::----===:
                                        :####*+==--:::::::::::::::-----=-
                                        +%##*+==---:::::..::::::::::-----.
                                        *###*+==--::::..........:::::::--:
                                        *###*+==--:::::::::.....:::::::--:
                                        **##*+=----::::::::...:::::::::---
                                      :.***#*+=----:::.::........::::::--..:-
                                      *#%**#*+==--=-::.-:........:::::::-.:--
                                      -%***####*+=-::::-:::::-----:::::::-:::
                                       =#*##**##%%#*##=-::-+****=-=:...:::::
                                       .#*#++##+==-=+#*:..::---:::.....::::.
                                        =**+===---:-=**-.:.............::..
                                         =**=--:::::-**-:::............::.
                                         .=*==--::::+*=:.::............:
                                          -*+=+=-::=*+-:..:::.........:.
                                          .++*+=-::=*#*=-:::.........::
                                           -**+=-:-=++=:-::::.......:::
                                           .*#+===+++=-:::::::::...:::.
                                            .**===+##+===---:::-:::::-**+-
                                            -##*=-==++++==-:::::::::--##%*+:
                                          .#%@%#++=--==-:::::....:-=::-+@#*+.
                                         :%%%@@%#+====-:--:::..:-+-:::-:=#++=.
                                      .:*%%%%@@@%%%*===-=-----=+=-::::::=*+++++=.
                                  .-*%%%%%%%%@@@%%%%%%%###**=---:::::::-***+++++***-
                             .:+####%%#%%%%%#%@@%%###%#*=----::::::::::=****++++******=.
                       .:=****#####%%#####%###@%#%#*****+=--::::::::::-******************+=.
                  .=+****##########%%##########***#*+++=--:::::::::::-+**********************+=:
                +****##############%###########++++**===---:::::::::-+*************#*#####*#*****+=.
               =##################%%###########*==-=+=-:--:::::::::=*##*************#########********=.
             .*##################%%###%%%%%@@@#**=-----:::::::::::*###%%%@%#*******##*##########*******:
           -#####################%##########%@@%#*-:::::::::::.:-#################***############*******-
          +%####################%##############%@@#*:::::::::::+######*#####*********##########**********+:
        -%#####################%#############%####%@%*::::::::*######*##**##*********##########***********+=
       *%####################################%######%%#=:::::*######******##*********############***********-
     .%%%#######%#######%####%####*#################*###=::=#####*********##***********###########**#*******++
    :%%%########%######%####%####################*##***##+-*###***********#************#**########*##********++.
   =%%################%##########**#******########*####*######****************************###*#######*********++.    ''')
    escolha = input("Você (A) se prepara para a jornada em busca do ONTRIX ou (B) hesita, preocupado com os perigos? ").lower()

    if escolha == "a":
        print("'Você se prepara para a jornada em busca do ONTRIX, determinado a ajudar sua tribo.")
        print('''
+=-----===+****##****#*#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%#%%%%@@@@@@@@@@@@@@@@@
**++==+===+**************%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#**+++++****#%%%%%%%%%###@@@@@@@@@@@@@@@@@@@@@%%#***#+*@@@@@@@@@@@@@@@@@@@@@@@@%%%%%@@@@@@@@@@@@@@@@
##*+*****#%%%%%%%%%%%%%%@@@@@@@@@@@@@@@@@@@@%#*****+::::#@@@@@@@@@@@@@@@@@@@@@@#*****************###
*******%%%%%%@@@@@@@@@@@@@@@@@@@@@%#@@@@@%%#***+++::::::+@@@@@@@@@@@@@@@@@@@@@@@%%%%%@@@@@%%%%%%%%%%
*****%%%%%%@@@@@@@@@@@@@@@@@@@@@@@##@@@@%#****+-+::::::=*@@@@@%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%@%%
***%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@##%@@@%#**+*=:=::::::=+%@@@@%*#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%%%%
+%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%#%@@%#***+-:=::-:::++#@@@%#*++%@@@@@@@%*-::@@@@@@@@@@@@@%%%%%%%%%%
%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%@@%@@%***++::-::::=+++*@@%#*+=+#@@#@@@#-::=:-@@@@@@@@@%%%%%%%%%%%%%%
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%@@@@***-*=:-:-:-+*=-+%%#++:-+*@%*%@@#::*+=:*@@@@@@@%%###%%#########
##*+++*#############%%@@@@@@@@@@@%#=#@%*=+=-:::=+-:=+##=:::+%@@@##@@*:++*+--@@@@%*#*#########%%%%%##
###**++*################*#@@@@@@@%#+.:*@+.--::=-:::::::+%@@@%%@@@%+-::=+:::%@@@@@@@@@@%%%%#######*+*
*********************#*%@@@@@@@@@%#*-..#@*-::::::::=#@@@%+...-=:::.::-++:.*@@@@@@@%%#*************++
*******************##@@@@@@@@@@@@@%**=::-+*:--:-=%%+..-+:....:::...:-+=::*@@@%*=---+******+******=-:
****+*++++++++++**%@@@%#**++++**++*#%%#*+++**+:=:--.::--=----:....:::::=@@@@@@@%#*=::::-+=--=+++++==
+++++++++++++++++*+++++++++++++++++##*+:.::-=:::-=++++=::::::.....::.=-:===--::::::::-===++++=--::--
++++++++=======++++++++++++++++++++*##**=::+=:::::-+-:::::::.....::::.::.:+*#*-:::::::::-:-:::::::::
--==--::::::::---==+======++++*#%%%@%#***+*+::..::::::::::::.....-:::.:-:.-##*++:::::::::-::::::::::
----::::::::::::::::::::-==+*%%%@@%@@%#++**=-=*=::::::::::::....:::::.:+=*#**+++*=:::--==--::::::.::
-----------:::::::::-*%%%%%%%%%@@%%@%%%#*+*++*+---:::::::::...:-:::::.-*#**++++++**-::--=--::....:::
---::----::---=*##%###%%%%%%%@@@@@@%%%%#*#**++++::.::::::..:--:::::::*#*++++++++++++*##*=-::::::::::
:::::::::::::*%#####%%%%%%%%@@%@%%%%%###**%***+***-::::::-=::::::::+#*+++++++++++++*##*++-::::::::::
::::::::::+*%%######%%%#%%@@%%%%%%%%###****##*+-:::::::=+::==::::=##*++++++++++++*##*+++**+=::::::..
:::::::=*##%#######%%%#%%%@%%%%%%%%####***+***#+----=#+::=++=:::+#*+++++++++++++*#*+++*#*++++*+-:.::
:::::++*#%%#%#####%%#%#%%%%%%%%%%%%##***##==*+******+::-+++++:-#*+++++++++++++*#++++*#%*+++++++++*+:
:::-***#%%%%%########%%%%%#%%%%%%###**####=:*--::++::.#++++++*#*++*++++++++*+*++++*%%##++++++++++*+*
..=**##%%%%%%#########%%%%##%%##%*=::::=**=.*====-::::::--=*#*+++++++++++++*++++*#%##*++++++++++++++
.=*###%%%%%%%%#**##%%%%%#########*=:....:-**+::::.........+#*++++++++++++**+++*#%##*++++++++++++++++
:*#**#%%%%%%%#***##%%%%%#######%#*+-....:**+::::::......:##***************+***%#********************
=****#%%%%%%#*****%%%%%%%#%###%%%*++:..=**+::::::::....+%***************+***%#+*********************''')
        cena2()
    elif escolha == "b":
        print("Você hesita, mas a necessidade de ajuda para sua tribo supera o medo.")
        cena2()
    else:
        print("Escolha inválida. Tente novamente.")
        cena1()

def cena2():
    print("\nCena 2: A busca por ONTRIX")
    print("Você parte em busca de ONTRIX e se depara com desafios e obstáculos pelo caminho.")
    print("Será uma jornada estreita e dificultosa, mas você está determinado.")
    escolha = input("Você (A) usa sua inteligência e astúcia para superar os desafios ou (B) confia em sua força para enfrentar os obstáculos? ").lower()

    if escolha == "a":
        print("Você usa sua inteligência e astúcia para superar os desafios, evitando perigos desnecessários.")
        cena3()
    elif escolha == "b":
        print("Você confia em sua força, mas enfrenta alguns obstáculos difíceis ao longo do caminho.")
        cena3()
    else:
        print("Escolha inválida. Tente novamente.")
        cena2()

def cena3():
    print("\nCena 3: O confronto final")
    print("Você se aproxima do local onde o ONTRIX está sendo armazenado, mas encontra um guardião poderoso.")
    print("É um confronto final que decidirá o destino do ONTRIX e de sua tribo.")
    escolha = input("Você (A) tenta negociar com o guardião ou (B) entra em um confronto direto? ").lower()

    if escolha == "a":
        print("Você tenta negociar com o guardião, oferecendo ajuda em troca do ONTRIX.")
        print("Após uma longa conversa, o guardião concorda em compartilhar parte do ONTRIX com sua tribo.")
        cena_final_vitoria()
    elif escolha == "b":
        print("Você entra em um confronto direto com o guardião, mostrando sua força e determinação.")
        print("Após uma batalha difícil, você vence e obtém o ONTRIX para sua tribo.")
        cena_final_vitoria()
    else:
        print("Escolha inválida. Tente novamente.")
        cena3()

def cena_final_vitoria():
    print("\nCena Final: Vitória e Esperança")
    print("Você retorna à sua tribo com as doses de ONTRIX, trazendo esperança e vida para as pessoas.")
    print("Sua determinação e coragem ajudaram a comunidade a sobreviver e prosperar.")
    print("O egoísmo do capitalismo pode ser superado quando a humanidade se une em solidariedade.")
    print("O futuro da sua tribo agora é brilhante.")
    print("Obrigado por jogar!")

# Iniciar o jogo
introducao()
