import os

tarefas = {}
tarefas_finalizadas = {}
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
    print("5. Ver tarefas concluidas;")
    print("6. Sair do Sistema;")

def limpar_tela():
    os.system('cls')

def pausar_tela():
    os.system('PAUSE')


def adicionar_tarefa():

    tipo_atividade = input("Informe o tipo de atividade que deseja adicionar: ")
    atividade = input("Digite a atividade: ")
    tarefas.setdefault(tipo_atividade, atividade)
    print("Adicionada com sucesso!")
    pausar_tela()
    limpar_tela()

def ver_tarefas():
    for numero, tarefa in enumerate(tarefas):
        print(f"{numero+1}. {tarefas[tarefa]}")
    pausar_tela()
    limpar_tela()

def concluir_tarefa():
    
    ver_tarefas()
    atividade = input("Digite qual atividade deseja concluir: ")
    if atividade in tarefas:
        tarefas_finalizadas[atividade] = tarefas.pop(atividade)
    else:
        print("Tarefa não encontrada. Por favor, selecione uma atividade que esteja no dicionário.")
        
    pausar_tela()
    limpar_tela()

def tarefas_concluidas():
    for numero, item in enumerate(tarefas_finalizadas):
        print(f"{numero} . {tarefas_finalizadas[item]}")


def excluir_tarefa():
    adicionar_tarefa()
    atividade = input("Digite qual atividade deseja excluir: ")
    if atividade in tarefas:
        tarefas.pop(atividade)
    else:
        print("Tarefa não encontrada. Por favor, selecione uma atividade que esteja no dicionário.")
        
    pausar_tela()
    limpar_tela()

while True:
    try:
        
        menu()
        escolha = int(input("Escolha um dos valores: "))
        limpar_tela()
        
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
                tarefas_concluidas()
            case 6:
                pausar_tela()
                limpar_tela()
                break
    except TypeError:
        print("Informe o tipo correto.")
        pausar_tela()
        limpar_tela()
        
    
print("Programa finalzado!\n")