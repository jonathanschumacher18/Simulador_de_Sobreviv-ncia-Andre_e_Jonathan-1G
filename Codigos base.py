import os


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
            break
        else:
            limpar() 
            print("Opção inválida")


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
    d = 0
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
            jogo(Sobreviventes, vd0, vd1, vd2, vd3, mn0, mn1, mn2, mn3, d)
        elif continuar == "2":
            limpar()
            cadastro_pers()
        else:
            limpar()
            print("Opção inválida")



def jogo(Sobreviventes, vd0, vd1, vd2, vd3, mn0, mn1, mn2, mn3, d):
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
3 - Sair
""")    
        opcao = input("Digite uma opção: ")
        if opcao == "1":
            limpar()
            lugares(d)
        elif opcao == "2":
            limpar()
            inventario()
        elif opcao == "3":
            limpar()
            print("Saindo do jogo...")
            menu()
        else:
            limpar() 
            print("Opção inválida")




def lugares(d):
    limpar()
    while True:
        print("- "* 40)
        print("""   Locais
1 - Floresta
2 - Caverna
3 - Cidade Ohio
4 - voltar""") #------------------------------------------------------------------------------------
        print("- "* 40)
        opcao = input("Digite uma opção: ")
        if opcao == "1":
            limpar()
            floresta()
        elif opcao == "2":
            limpar()
            caverna()
        elif opcao == "3":
            limpar()
            cidade(d)
        elif opcao == "4":
            limpar()
            print("Voltando...")
            break
        else:
            limpar()
            print("Opção inválida")
            

        


def floresta():
    pass

def caverna():
    pass

def cidade(d):
    limpar()
    while True:
        print("- "* 40)
        print()
        print("""           Bem Vindo a Cidade de Ohio!

1 - Loja
2 - Ferreiro 
3 - Voltar""") #------------------------------------------------------------------------------------
        print()
        print("- "* 40)
        opcao = input("Digite uma opção: ")
        if opcao == "1":
            limpar()
            loja(d)
        elif opcao == "2":
            limpar()
            ferreiro()
        elif opcao == "3":
            limpar()
            print("Voltando...")
            break
        else:
            limpar()
            print("Opção inválida")

def loja(dinheiro):
    limpar()
    while True:
        print("- "* 40)
        print(f"""           Itens á venda

Suas Moedas: {dinheiro}

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
        if opcao == "1" and dinheiro >= 5:
            limpar()
            dinheiro -= 5
            pass #------------------------------------------------------------------------------
        elif opcao == "2" and dinheiro >= 2:
            limpar()
            dinheiro -= 2
            pass
        elif opcao == "3" and dinheiro >= 1:
            limpar()
            dinheiro -= 1
            pass
        elif opcao == "4" and dinheiro >= 10:
            limpar()
            dinheiro -= 10
            pass
        elif opcao == "5":
            limpar()
            print("voltando...")
            break
        else:
            limpar()
            print("Opção inválida")


def ferreiro():
    pass





def inventario():
    pass




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


#--------------------------------------------------------------
a = ["a","b","c","d"]
aiai = 10
#menu()
#jogo(a)
loja(aiai)
