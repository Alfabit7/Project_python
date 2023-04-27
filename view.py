import notion


def ShowMenu():
    print('\n 1- Добавить заметку \n 2- Показать все заметки\n 3- Редактировать заметку\n 4- Удалить заметку\n 5- Выход из меню\n')
    menu = int(input('Введите пункт меню '))
    if menu == 1:
        notion.addNote()
    elif menu == 2:
        notion.ShowAllNotion()
    elif menu == 3:
        notion.EditNotion()
    elif menu == 4:
        notion.DeleteNotion()
    elif menu == 5:
        print('exit to menu')
    return menu
