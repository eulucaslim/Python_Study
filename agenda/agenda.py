from crud import add_contact, show_contats, update_contact, delete_contact

done = False
while not done:
    print('-- AGENDA DE CONTATOS --\n')
    print('1. Adicionar Contatos\n')
    print('2. Exibir Contato\n')
    print('3. Atualizar Contatos\n')
    print('4. Remover Contatos\n')
    print('5. Sair da Agenda\n')
                        
    choice = input('Escolha de 1 a 5: \n')
                        
    if choice == '1':
        add_contact()
                        
    elif choice == '2':
        show_contats()
                        
    elif choice == '3':
        update_contact()
                        
    elif choice == '4':
        delete_contact()
                        
    elif choice == '5':
        print('Encerrando o Programa...')
        done = True
                   
    else:
        print('Opção não correspondente!')                    