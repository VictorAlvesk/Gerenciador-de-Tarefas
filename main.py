import os

tarefas_pendentes = {}
tarefas_concluidas = {}
tarefas_excluidas = {}

def menu():
    print("\n-------------------------\n")
    print("  Gerenciador de Tarefas  ")
    print("\n------------------------\n")

    print("Informe uma das sentenças opções:")
    print("1. Adicionar tarefa;")
    print("2. Ver tarefas;")
    print("3. Concluir tarefa;")
    print("4. Excluir tarefa;")
    print("5. Sair do Sistema;")

def limpar_tela():
    os.system('cls')

def pausar_tela():
    os.system('PAUSE')

def adicionar_tarefa():
    ...

def ver_tarefas():
    ...

def concluir_tarefa():
    ...

def excluir_tarefa():
    ...

while True:
    try:
        menu()
        escolha = int(input("Escolha um dos valores:"))

        match escolha:
            case 1:
                adicionar_tarefa()
            case 2:
                ver_tarefas()
            case 3:
                concluir_tarefa()
            case 4:
                excluir_tarefa()
            case 5:
                pausar_tela()
                limpar_tela()
                break
    except:
        ...
    
print("Programa finalzado!\n")