import inf_system as infs
import view


def writing_down():
    name = view.get_name()
    information = view.general_information()
    action = view. what_to_do()
    print(information)
    for i in range(len(action)):
        if action[i] == 'Новый контакт':
            if name[i][0] not in infs.inf_book:
                infs.create_new_list(name[i], infs.inf_book)
            infs.create_new_note(name[i], infs.inf_book, information[i])
        elif action[i] == 'Актуализация информации':
            infs.update_note(name[i], infs.inf_book, information[i])
        elif action[i] == 'Удалить из базы':
            infs.delete_note(name[i], infs.inf_book)
    return infs.inf_book
