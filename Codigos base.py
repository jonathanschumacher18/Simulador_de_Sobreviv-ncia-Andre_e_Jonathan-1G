import os
import sys
import random


def limpar():
    os.system("cls")



def menu():
    while True:
        print("- "* 30)
        print("""    1 - começar um jogo novo
    2 - sair""")
        print("- "* 30)
        print()
        opcao1 = input("Insira uma opção: ")

        if opcao1 == "1":
            iniciar()
        elif opcao1 == "2":
            print("Saindo do jogo...")
            input("ENTER para continuar")
            sys.exit()
        else:
            limpar() 
            print("Opção inválida")
            input("ENTER para continuar")


def iniciar():
    limpar()
    while True:
        print("- "* 30)
        print("""4 aventureiros vagam na cidade de Ohio, a capital sagrada
de Osmantus. Qual o nome desses aventureiros?""")
        print("- "* 30)
        input("ENTER para continuar")
        cadastro_pers()


def cadastro_pers():
    limpar()
    nome = input(" Digite o nome do seu personagem (guerreiro): ")
    sobrenome = input( " Digite o sobrenome do seu personagem (guerreiro): ")
    nome_completo = nome + " " + sobrenome
    limpar()


    nome1 = input(" Digite o nome do seu personagem (arqueiro): ")
    sobrenome1 = input( " Digite o sobrenome do seu personagem (arqueiro): ")
    nome_completo1 = nome1 + " " + sobrenome1
    limpar()

    nome2 = input(" Digite o nome do seu personagem (mago): ")
    sobrenome2 = input( " Digite o sobrenome do seu personagem (mago): ")
    nome_completo2 = nome2 + " " + sobrenome2
    limpar()

    nome3 = input(" Digite o nome do seu personagem (curandeiro): ")
    sobrenome3 = input( " Digite o sobrenome do seu personagem (curandeiro): ")
    nome_completo3 = nome3 + " " + sobrenome3
    limpar()

    Sobreviventes = [
        nome_completo,
        nome_completo1,
        nome_completo2,
        nome_completo3
    ]
    vd0 = 40
    vd1 = 25
    vd2 = 20
    vd3 = 30
    mn0 = 10
    mn1 = 15
    mn2 = 25
    mn3 = 20
    inv = {
    "Moedas": 0,
    "Pocao de Cura": 0,
    "Minerio de Ferro": 0,
    "Madeira": 0,
    "Diamante": 0
}
    while True:
        print("Estes são os seus 4 aventureiros:", ", ".join(Sobreviventes))

        print("- "* 30)
        print('''1 - continuar
2 - renomear''')
    
        continuar = input("Insira uma opção: ")
        if continuar == "1":
            limpar()
            print("- "* 30)
            print()
            print("COMEÇANDO O JOGO...")
            print()
            print("- "* 30)
            input("ENTER para continuar")
            limpar()
            jogo(Sobreviventes, vd0, vd1, vd2, vd3, mn0, mn1, mn2, mn3, inv)
        elif continuar == "2":
            limpar()
            cadastro_pers()
        else:
            limpar()
            print("Opção inválida")
            input("ENTER para continuar")



def jogo(Sobreviventes, vd0, vd1, vd2, vd3, mn0, mn1, mn2, mn3, inv):
    limpar()
    while True:
        print("- "* 40)
        print()
        print(f"""{Sobreviventes[0]}
Vida = {vd0}/40
Mana = {mn0}/10""")
        print()
        print(f"""{Sobreviventes[1]}
Vida = {vd1}/25
Mana = {mn1}/15""")
        print()
        print(f"""{Sobreviventes[2]}
Vida = {vd2}/20
Mana = {mn2}/25""")
        print()
        print(f"""{Sobreviventes[3]}
Vida = {vd3}/30
Mana = {mn3}/20""")
        print()
        print("- "* 40)
        print("""   Opções
1 - Explorar
2 - Inventário
3 - Sair do jogo
""")    
        opcao = input("Digite uma opção: ")
        if opcao == "1":
            limpar()
            lugares(inv, Sobreviventes, vd0, vd1, vd2, vd3, mn0, mn1, mn2, mn3)
        elif opcao == "2":
            limpar()
            inventario(inv)
        elif opcao == "3":
            limpar()
            print("fechando o jogo...")
            input("ENTER para continuar")
            sys.exit()
        else:
            limpar() 
            print("Opção inválida")
            input("ENTER para continuar")




def lugares(inv, Sobreviventes, vd0, vd1, vd2, vd3, mn0, mn1, mn2, mn3):
    limpar()
    while True:
        print("- "* 40)
        print("""   
     Os aventureiros entram em uma
    encruzilhada onde eles devem ir?
        
- - - - - - - - - - - -

        Locais
1 - Floresta
2 - Caverna
3 - Cidade Ohio
4 - voltar""")
        print("- "* 40)
        opcao = input("Digite uma opção: ")
        if opcao == "1":
            limpar()
            floresta(inv, Sobreviventes, vd0, vd1, vd2, vd3, mn0, mn1, mn2, mn3)
        elif opcao == "2":
            limpar()
            caverna(inv, Sobreviventes, vd0, vd1, vd2, vd3, mn0, mn1, mn2, mn3)
        elif opcao == "3":
            limpar()
            cidade(inv)
        elif opcao == "4":
            limpar()
            print("Voltando...")
            input("ENTER para continuar")
            limpar()
            break
        else:
            limpar()
            print("Opção inválida")
            input("ENTER para continuar")
            






def evento_aleatorio(bioma):

    if bioma == "caverna":
        evento = random.randrange(4)

        if evento == 0:
            print("Você acaba de encontrar um minério!")
            print("Use sua picareta para quebrá-lo.")
            return 0

        elif evento == 1:
            print("Você não encontrou nada, continue explorando.")
            return 1

        elif evento == 2:
            print("Você deu de cara com um inimigo!")
            print("Derrote-o para ganhar recompensas.")
            return 2

        elif evento == 3:
            print("Você encontrou uma pequena quantidade de ouro!")
            return 3


    elif bioma == "floresta":
        evento = random.randrange(4)
        return evento




def floresta(inv, Sobreviventes, vd0, vd1, vd2, vd3, mn0, mn1, mn2, mn3):
    bioma = "floresta"
    print("- "* 40)
    print("""
            Eles entram na floresta escura na procura de monstros
                e recompensas para sua incrivel aventura.
                """)
    print("- "* 40)
    input("ENTER para continuar")
    dentro_f(bioma, inv, Sobreviventes, vd0, vd1, vd2, vd3, mn0, mn1, mn2, mn3)

def dentro_f(bioma, inv, Sobreviventes, vd0, vd1, vd2, vd3, mn0, mn1, mn2, mn3):
    limpar()
    while True:
        print("- "* 40)
        print("""
    O que devemos fazer agora?
    
1 - explorar a floresta
2 - voltar
""")
        print("- "* 40)
        opcao = input("Digite uma opção: ")

        if opcao == "1":
            evento = evento_aleatorio(bioma)
            if evento == 0:
                print("Você deu de cara com um inimigo, derrote-o para ganhar recompensas")
                input("ENTER para continuar")
                vidas, manas = batalha(bioma, Sobreviventes, vd0, vd1, vd2, vd3, mn0, mn1, mn2, mn3)

                vd0 = vidas[0]
                vd1 = vidas[1]
                vd2 = vidas[2]
                vd3 = vidas[3]

                mn0 = manas[0]
                mn1 = manas[1]
                mn2 = manas[2]
                mn3 = manas[3]

                limpar()

            elif evento == 1:
                print("Você achou uma carroça cheia de dinheiro, que sorte em")
                print()
                print("- "*10)
                print()
                inv["Moedas"] += 10
                print("Você recebeu 10 moedas de ouro!")
                input("ENTER para voltar")
                limpar()

            elif evento == 2:
                print("""
                Você encontrou uma macieira
                coletou um pouco de madeira
                e algumas maçãs para vender.
                """)
                print("- "*10)
                inv["Moedas"] += 2
                inv["Madeira"] += 1
                print()
                print("Você recebeu 2 moedas e 1 madeira!")
                input("ENTER para voltar")
                limpar()


            elif evento == 3:
                print("Você não encontrou nada, continue explorando")
                input("ENTER para voltar")
                limpar()

        elif opcao == "2":
            limpar()
            print("Voltando...")
            input("ENTER para continuar")
            limpar()
            break

        else:
            limpar()
            print("Opção inválida")
            input("ENTER para continuar")

def batalha(bioma, Sobreviventes, vd0, vd1, vd2, vd3, mn0, mn1, mn2, mn3):

    vidas = [vd0, vd1, vd2, vd3]
    manas = [mn0, mn1, mn2, mn3]

    vidas_max = [40, 25, 20, 30]
    manas_max = [10, 15, 25, 20]


    monstros_floresta = [
        {
            "nome": "Goblin",
            "vida": 100,
            "ataque_min": 5,
            "ataque_max": 10
        },

        {
            "nome": "Slime",
            "vida": 75,
            "ataque_min": 3,
            "ataque_max": 8
        },

        {
            "nome": "Árvore Viva",
            "vida": 150,
            "ataque_min": 8,
            "ataque_max": 15
        }
    ]

    monstros_caverna = [
        {
            "nome": "Goblin",
            "vida": 100,
            "ataque_min": 5,
            "ataque_max": 10
        },

        {
            "nome": "Pedra Viva",
            "vida": 125,
            "ataque_min": 7,
            "ataque_max": 12
        },

        {
            "nome": "Morcego Gigante",
            "vida": 60,
            "ataque_min": 4,
            "ataque_max": 9
        },

        {
            "nome": "Cobra",
            "vida": 80,
            "ataque_min": 6,
            "ataque_max": 11
        }
    ]


    if bioma == "floresta":
        monstros = monstros_floresta

    elif bioma == "caverna":
        monstros = monstros_caverna

    else:
        monstros = []


    monstro = random.choice(monstros)

    nome_inimigo = monstro["nome"]
    vida_inimigo = monstro["vida"]
    vida_inimigo_max = monstro["vida"]

    turno = 0

    while vida_inimigo > 0 and any(vida > 0 for vida in vidas):

        limpar()

        print("=" * 50)
        print("                  BATALHA")
        print("=" * 50)

        print()
        print(f"              {nome_inimigo}")
        print(f"              Vida: {vida_inimigo}/{vida_inimigo_max}")
        print()

        print("-" * 50)

        for i in range(4):

            print(f"{i + 1} - {Sobreviventes[i]}")
            print(f"    Vida: {vidas[i]}/{vidas_max[i]}")
            print(f"    Mana: {manas[i]}/{manas_max[i]}")
            print()

        print("-" * 50)

        print("Quem irá agir: ")
        print("1 - Guerreiro")
        print("2 - Arqueiro")
        print("3 - Mago")
        print("4 - Curandeiro")
        print()

        personagem = input("Digite uma opção: ")

        if personagem not in ["1", "2", "3", "4"]:
            print("Opção inválida!")
            input("ENTER para continuar")
            continue

        jogador = int(personagem) - 1

        if vidas[jogador] <= 0:
            print("Esse personagem está derrotado!")
            input("ENTER para continuar")
            continue

        limpar()

        print("=" * 50)
        print(f"             TURNO DE {Sobreviventes[jogador]}")
        print("=" * 50)

        print()
        print("1 - Ataque")
        print("2 - Magia")
        print("3 - Defender")
        print()

        acao = input("Escolha uma ação: ")




        if acao == "1":


            danos = [10, 8, 5, 4]

            dano = danos[jogador]

            vida_inimigo -= dano

            if vida_inimigo < 0:
                vida_inimigo = 0

            print()
            print(f"{Sobreviventes[jogador]} atacou!")
            print(f"O ataque causou {dano} de dano!")
            





        elif acao == "2":

            custo_mana = [3, 4, 8, 6]
            dano_magia = [15, 18, 25, 0]

            if manas[jogador] < custo_mana[jogador]:

                print("Você não possui mana suficiente!")

                input("ENTER para continuar")
                continue

            manas[jogador] -= custo_mana[jogador]


            if jogador == 3:

                print(f"{Sobreviventes[jogador]} utilizou Cura!")

                for i in range(4):

                    if vidas[i] > 0:

                        vidas[i] += 10

                        if vidas[i] > vidas_max[i]:
                            vidas[i] = vidas_max[i]

                print("Todos os personagens recuperaram 10 de vida!")
                

            else:

                dano = dano_magia[jogador]

                vida_inimigo -= dano

                if vida_inimigo < 0:
                    vida_inimigo = 0

                print(f"{Sobreviventes[jogador]} utilizou uma magia!")
                print(f"A magia causou {dano} de dano!")
                



        elif acao == "3":

            print(f"{Sobreviventes[jogador]} está se defendendo!")

        else:

            print("Opção inválida!")
            input("ENTER para continuar")
            continue

        input("ENTER para continuar")


        if vida_inimigo <= 0:
            break


        limpar()

        print("=" * 50)
        print("              TURNO DO INIMIGO")
        print("=" * 50)


        personagens_vivos = []

        for i in range(4):

            if vidas[i] > 0:
                personagens_vivos.append(i)

        alvo = random.choice(personagens_vivos)

        dano_inimigo = random.randint(
    monstro["ataque_min"],
    monstro["ataque_max"]
)

        vidas[alvo] -= dano_inimigo

        if vidas[alvo] < 0:
            vidas[alvo] = 0

        print()
        print(f"O {nome_inimigo} atacou {Sobreviventes[alvo]}!")
        print(f"Causou {dano_inimigo} de dano!")

        if vidas[alvo] <= 0:
            print(f"{Sobreviventes[alvo]} foi derrotado!")

        input("ENTER para continuar")




    limpar()

    print("=" * 50)

    if vida_inimigo <= 0:

        print("              VITÓRIA!")
        print("=" * 50)
        print()
        print(f"Você derrotou o {nome_inimigo}!")

    else:

        print("             DERROTA!")
        print("=" * 50)
        print()
        print("Todos os seus aventureiros foram derrotados.")

    print()

    input("ENTER para continuar")

    return vidas, manas



def caverna(inv, Sobreviventes, vd0, vd1, vd2, vd3, mn0, mn1, mn2, mn3):

    bioma = "caverna"

    limpar()

    print("- " * 40)
    print("""
        Os aventureiros entram em uma enorme caverna.
        
        O som das gotas de água ecoa pelas paredes
        enquanto eles procuram por minérios, tesouros
        e criaturas escondidas nas profundezas.
    """)
    print("- " * 40)

    input("ENTER para continuar")

    dentro_c(bioma, inv, Sobreviventes, vd0, vd1, vd2, vd3, mn0, mn1, mn2, mn3)



def dentro_c(bioma, inv, Sobreviventes, vd0, vd1, vd2, vd3, mn0, mn1, mn2, mn3):
    limpar()

    while True:

        print("- " * 40)

        print("""
        Você está dentro da caverna.

        O que devemos fazer agora?

        1 - Explorar a caverna
        2 - Voltar
        """)

        print("- " * 40)

        opcao = input("Digite uma opção: ")

        if opcao == "1":

            limpar()

            evento = evento_aleatorio(bioma)


            if evento == 0:

                print("- " * 40)
                print("        MINÉRIO ENCONTRADO!")
                print("- " * 40)

                print("""
Você acaba de encontrar um minério!

Use sua picareta para quebrá-lo.
""")

                print()
                minerio()

                print()
                print("Você encontrou minério de ferro!")

                inv["Minerio de Ferro"] += 1

                print()
                print("Você recebeu 1 Minério de Ferro!")

                input("ENTER para continuar")
                limpar()


            elif evento == 1:

                print("- " * 40)

                print("""
Você não encontrou nada,
continue explorando.
""")

                print("- " * 40)

                input("ENTER para continuar")
                limpar()


            elif evento == 2:

                print("- " * 40)

                print("""
Você deu de cara com um inimigo!

Derrote-o para ganhar recompensas.
""")

                print("- " * 40)

                input("ENTER para começar a batalha")

                vidas, manas = batalha(bioma, Sobreviventes, vd0, vd1, vd2, vd3, mn0, mn1, mn2, mn3)

                vd0 = vidas[0]
                vd1 = vidas[1]
                vd2 = vidas[2]
                vd3 = vidas[3]

                mn0 = manas[0]
                mn1 = manas[1]
                mn2 = manas[2]
                mn3 = manas[3]

                limpar()



            elif evento == 3:

                print("- " * 40)

                print("""
Você encontrou algumas moedas
escondidas entre as pedras!
""")

                print("- " * 40)

                inv["Moedas"] += 5

                print("Você recebeu 5 moedas de ouro!")

                input("ENTER para continuar")
                limpar()



        elif opcao == "2":

            limpar()

            print("Saindo da caverna...")

            input("ENTER para continuar")

            limpar()

            break


        else:

            limpar()

            print("Opção inválida!")

            input("ENTER para continuar")



def cidade(inv):
    limpar()
    while True:
        print("- "* 40)
        print("""           
        Bem Vindo a Cidade de Ohio!
           Onde você deseja ir?
1 - Loja
2 - Ferreiro 
3 - Voltar""")
        print()
        print("- "* 40)
        opcao = input("Digite uma opção: ")
        if opcao == "1":
            limpar()
            loja(inv)
        elif opcao == "2":
            limpar()
            ferreiro(inv)
        elif opcao == "3":
            limpar()
            print("Voltando...")
            input("ENTER para continuar")
            limpar()
            break
        else:
            limpar()
            print("Opção inválida")
            input("ENTER para continuar")

def loja(inv):
    limpar()
    while True:
        print("- "* 40)
        print(f"""           Itens á venda

Suas Moedas: {inv["Moedas"]}

Poção de Cura - 1
   _@_ 
   | |
  ( ° ) 
   --- 
  5 moedas
- - - - - - - - - - - -
Minerio de Ferro - 2
   ___
   |_|
 2 moedas
- - - - - - - - - - - -
 Madeira - 3
  |||||
  |||||
 1 moeda
- - - - - - - - - - - -
Diamante - 4
  /\\
  \\/
 10 moedas

Voltar - 5
""")
        opcao = input("Digite uma opção: ")
        if opcao == "1" and inv["Moedas"] >= 5:
            limpar()
            inv["Moedas"] -= 5
            inv["Pocao de Cura"] += 1
            print("Você comprou uma Poção de Cura!")
            print(f"Você possui {inv['Pocao de Cura']} poção(ões).")
            input("ENTER para continuar")
        elif opcao == "2" and inv["Moedas"] >= 2:
            limpar()
            inv["Moedas"] -= 2
            inv["Minerio de Ferro"] += 1
            print("Você comprou um minério de ferro!")
            print(f"Você possui {inv['Minerio de Ferro']} minério(s) de ferro.")
            input("ENTER para continuar")
        elif opcao == "3" and inv["Moedas"] >= 1:
            limpar()
            inv["Moedas"] -= 1
            inv["Madeira"] += 1
            print("Você comprou um pedaço de madeira!")
            print(f"Você possui {inv['Madeira']} madeira(s).")
            input("ENTER para continuar")        
        elif opcao == "4" and inv["Moedas"] >= 10:
            limpar()
            inv["Moedas"] -= 10
            inv["Diamante"] += 1
            print("Você comprou um diamante!")
            print(f"Você possui {inv['Diamante']} diamante(s).")
            input("ENTER para continuar")
        elif opcao == "5":
            limpar()
            print("voltando...")
            input("ENTER para continuar")
            break
        else:
            limpar()
            print("Opção inválida")
            input("ENTER para continuar")


def ferreiro(inv):
    limpar()
    inv_armas = {
        "Espada de ferro": 0,
        "Espada de Diamante": 0,
        "Espada Vorpal": 0,
        "Arco pesado(ferro)": 0,
        "Cajado de Diamante": 0,
        "Cetro de Diamante": 0
    }
    while True:
        print("- " * 40)
        print("""
                            Bem Vindo ao Ferreiro
                              da nossa cidade!
              """)
        print("- " * 40)
        print("""       
O'que deseja fazer hoje?

0 - Inventario
- - - - - - - - - - - - - 

1 - Espada de ferro
    | 2 madeiras  |
    | 2 m/ ferros |

- - - - - - - - - - - - - 

2 - Espada de Diamante
    | 2 madeiras  |
    | 2 diamantes |

- - - - - - - - - - - - - 

3 - Arco pesado
    | 3 madeiras  |
    | 1 m/ ferros |

- - - - - - - - - - - - - 

4 - Cajado de Diamante
    | 3 madeiras  |
    | 1 diamantes |

- - - - - - - - - - - - -

5 - Cetro de Diamante
    | 2 diamantes |
    | 2 m/ ferros |

- - - - - - - - - - - - - 

6 - Espada Vorpal
    | 4 diamantes |
    | 2 m/ ferros |

- - - - - - - - - - - - -

7 - voltar

- - - - - - - - - - - - - 
""")
        opcao = input("Digite uma opção: ")

        if opcao == "0":
            for item, quantidade in inv.items():
                print(f"{item}: {quantidade}")

            print("- " * 30)
            input("ENTER para continuar")
            limpar()


        elif opcao == "1":
            if inv["Madeira"] >= 2 and inv["Minerio de Ferro"] >= 2:
                if inv_armas['Espada de ferro'] == 0:
                    print("Item Feito!")
                    inv_armas['Espada de ferro'] += 1
                    inv["Madeira"] -= 2
                    inv["Minerio de Ferro"] -= 2
                    if inv_armas['Espada de Diamante'] == 1 or inv_armas['Espada Vorpal'] == 1:
                        print("Você já está usando uma espada melhor!")
                        input("ENTER para continuar")
                        limpar()
                    else:
                        print(f"Seu Guerreiro equipou uma Espada de Ferro!")
                        input("ENTER para continuar")
                else:
                    print("Você Já possui essa arma")
                    input("ENTER para continuar")
            else:
                print("Você não tem os materias suficientes para fazer essa arma.")
                input("ENTER para continuar")
                limpar()


        elif opcao == "2":
            if inv["Madeira"] >= 2 and inv["Diamante"] >= 2:
                if inv_armas['Espada de Diamante'] == 0:
                    print("Item Feito!")
                    inv_armas['Espada de Diamante'] += 1
                    inv["Madeira"] -= 2
                    inv["Diamante"] -= 2
                    if inv_armas['Espada Vorpal'] == 1:
                        print("Você já está usando uma espada melhor!")
                        input("ENTER para continuar")
                        limpar()
                    else:
                        print(f"Seu Guerreiro equipou uma Espada de Diamante!")
                        input("ENTER para continuar")
                else:
                    print("Você Já possui essa arma")
                    input("ENTER para continuar")
            else:
                print("Você não tem os materias suficientes para fazer essa arma.")
                input("ENTER para continuar")
                limpar()

                
        elif opcao == "3":
            if inv["Madeira"] >= 3 and inv["Minerio de Ferro"] >= 1:
                if inv_armas['Arco pesado(ferro)'] == 0:
                    print("Item Feito!")
                    inv_armas['Arco pesado(ferro)'] += 1
                    inv["Madeira"] -= 3
                    inv["Minerio de Ferro"] -= 1
                    print(f"Seu Arqueiro equipou o Arco pesado!")
                    input("ENTER para continuar")
                else:
                    print("Você Já possui essa arma")
                    input("ENTER para continuar")
            else:
                print("Você não tem os materias suficientes para fazer essa arma.")
                input("ENTER para continuar")
                limpar()



        elif opcao == "4":
            if inv["Madeira"] >= 3 and inv["Diamante"] >= 1:
                if inv_armas['Cajado de Diamante'] == 0:
                    print("Item Feito!")
                    inv_armas['Cajado de Diamante'] += 1
                    inv["Madeira"] -= 3
                    inv["Diamante"] -= 1
                    print(f"Seu Mago equipou o Cajado de Diamante!")
                    input("ENTER para continuar")
                else:
                    print("Você Já possui essa arma")
                    input("ENTER para continuar")
            else:
                print("Você não tem os materias suficientes para fazer essa arma.")
                input("ENTER para continuar")
                limpar()


        elif opcao == "5":
            if inv["Minerio de Ferro"] >= 2 and inv["Diamante"] >= 2:
                if inv_armas['Cetro de Diamante'] == 0:
                    print("Item Feito!")
                    inv_armas['Cetro de Diamante'] += 1
                    inv["Minerio de Ferro"] -= 2
                    inv["Diamante"] -= 2
                    print(f"Seu Curandeiro equipou o Cetro de Diamante!")
                    input("ENTER para continuar")
                else:
                    print("Você Já possui essa arma")
                    input("ENTER para continuar")
            else:
                print("Você não tem os materias suficientes para fazer essa arma.")
                input("ENTER para continuar")
                limpar()


        elif opcao == "6":
            if inv["Minerio de Ferro"] >= 2 and inv["Diamante"] >= 4:
                if inv_armas['Espada Vorpal'] == 0:
                    print("Item Feito!")
                    inv_armas['Espada Vorpal'] += 1
                    inv["Minerio de Ferro"] -= 2
                    inv["Diamante"] -= 4
                    print(f"Seu Guerreiro equipou a lendária Espada Vorpal!!")
                    input("ENTER para continuar")
                else:
                    print("Você Já possui essa arma")
                    input("ENTER para continuar")
            else:
                print("Você não tem os materias suficientes para fazer essa arma.")
                input("ENTER para continuar")
                limpar()


        elif opcao == "7":
            print("voltando...")
            input("ENTER para continuar")
            limpar()
            break

        else:
            print("Opção inválida.")
            input("ENTER para continuar")
            limpar()

        

def inventario(inv):
    limpar()

    while True:
        print("- " * 30)
        print("             INVENTÁRIO")
        print("- " * 30)

        for item, quantidade in inv.items():
            print(f"{item}: {quantidade}")

        print("- " * 30)
        print()
        print("1 - Usar poção")
        print("2 - Voltar")

        opcao = input("Digite uma opção: ")

        if opcao == "1":
            if inv["Pocao de Cura"] > 0:
                inv["Pocao de Cura"] -= 1
                print("Você usou uma Poção de Cura!")
                input("ENTER para continuar")
                limpar()
            else:
                print("Você não possui nenhuma poção.")
                input("ENTER para continuar")
                limpar()

        elif opcao == "2":
            print("voltando...")
            input("ENTER para continuar")
            limpar()
            break

        else:
            print("Opção inválida.")
            input("ENTER para continuar")
            limpar()

    return inv["Moedas"]




def personagem_principal():
    print("  O")
    print(" /|\\")
    print(" / \\")


def picareta():
    print("/|\\")
    print(" |")


def espada():
    print(" /")
    print("/")


def boss():
    print(" ______")
    print(" | 0 0|")
    print(" | \\/ |")
    print(" ------")


def arvore():
    print(" _____ ")
    print("(     )")
    print("(     )")
    print(" -----")
    print(" |   |")
    print(" |   |")
    print(" -----")


def minerio():
    print(" ________")
    print(" | °.. .|")
    print(" |°  .°.|")
    print(" --------")

def poção():
    print(" _@_ ")
    print(" | |")
    print("( ° ) ")
    print(" --- ")

def ferro():
    print("___")
    print("|_|")

def diamante():
    print("/\\")
    print("\\/")

#-----------------------------------------------------------------------------------------------------------
menu()
