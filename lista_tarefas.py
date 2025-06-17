import json
import os

### Funções ###
def listar (tarefas):
    print ()
    if not tarefas:
        print ('Nenhuma tarefa para listar.')
        print()
        return
    print('\nTarefas:')
    for i, tarefa in enumerate(tarefas, start=1):
        print(f'{i}. {tarefa}')
    print()

def desfazer (tarefas, tarefas_desfeitas):
    print ()
    if not tarefas:
        print ('Nenhuma tarefa para desfazer.')
        print()
    else:
        tarefa = tarefas.pop()
        tarefas_desfeitas.append(tarefa)
        print(f'Tarefa: "{tarefa}" desfeita.')
        print()

def refazer(tarefas, tarefas_desfeitas):
    print()
    if not tarefas_desfeitas:
        print('Nenhuma tarefa para refazer.')
        print()
        return
    tarefa = tarefas_desfeitas.pop()
    tarefas.append(tarefa)
    print(f'Tarefa: "{tarefa}" refeita.')
    print()

def adicionar(tarefa, tarefas):
    print ()
    tarefa = tarefa.strip()
    if not tarefa:
        print ('Você não digitou uma tarefa.')
        return
    print (f'Tarefa: {tarefa} adicionada a lista com sucesso.')
    tarefas.append(tarefa)
    print ()
    print (tarefas)

def ler (caminho_arquivo):
    dados = []
    try:
        with open(caminho_arquivo, 'r', encoding='utf8') as arquivo:
            dados = json.load(arquivo)
    except FileNotFoundError:
        print('\nArquivo não encontrado. Criando novo arquivo...\n')
        salvar([], caminho_arquivo)
    except json.JSONDecodeError:
        print('\nArquivo vazio ou corrompido. Iniciando lista vazia...\n')
    return dados

def salvar (tarefas, caminho_arquivo):
    dados = tarefas
    with open(caminho_arquivo, 'w', encoding='utf8') as arquivo:
        dados = json.dump(tarefas, arquivo, indent=2, ensure_ascii=False)

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

### Variaveis ###
CAMINHO_ARQUIVO = 'aula56.json'

### Listas ###
tarefas = ler(CAMINHO_ARQUIVO)
tarefas_desfeitas = []

while True:
    print('Comandos: listar, desfazer, refazer,clear e sair')
    tarefa = input('Digite uma tarefa ou comando: ')

    if tarefa == 'sair':
        print ('Saindo do programa...')
        break

    comandos = {
        'listar': lambda: listar(tarefas),
        'desfazer': lambda: desfazer(tarefas, tarefas_desfeitas),
        'refazer': lambda: refazer(tarefas, tarefas_desfeitas),
        'clear': lambda: clear_console(),
        'adicionar': lambda: adicionar(tarefa, tarefas),
    }
    comando = comandos.get(tarefa) if comandos.get(tarefa) is not None else \
        comandos['adicionar']
    comando()
    salvar(tarefas, CAMINHO_ARQUIVO)
