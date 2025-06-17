lista_tarefas = []
tarefas_desfeitas = []

while True:
    print ('Comandos: Listar, Desfazer, Refazer e Sair')
    tarefa = input('Digite uma tarefa ou comando: ')

    if tarefa == 'listar' or tarefa == 'Listar' or tarefa == 'LISTAR':
        if not lista_tarefas:
            print ('Nenhuma tarefa na lista.')
            print ()
        else:
            print ('\nTarefas:')
        for i, tarefa in enumerate(lista_tarefas, start=1):
            print (f'{i}. {tarefa}')
        print()

    elif tarefa == 'desfazer' or tarefa == 'Desfazer' or tarefa == 'DESFAZER':
        if lista_tarefas:
            tarefa = lista_tarefas.pop()
            tarefas_desfeitas.append(tarefa)
            print (f'Tarefa: "{tarefa}" desfeita.')
            print()
        else:
            print ('Nenhuma tarefa para desfazer.')
            print()

    elif tarefa == 'refazer' or tarefa == 'Refazer' or tarefa == 'REFAZER':
        if tarefas_desfeitas:
            tarefa = tarefas_desfeitas.pop()
            lista_tarefas.append(tarefa)
            print (f'Tarefa: "{tarefa}" refeita.')
            print()
        else:
            print ('Nehuma tarefa para refazer')
            print()

    elif tarefa == 'sair' or tarefa == 'Sair' or tarefa == 'SAIR':
        break

    else:
        lista_tarefas.append(tarefa)
        print()
