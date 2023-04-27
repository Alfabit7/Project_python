import notion


def ShowMenu():
    print('\n 1- Добавить заметку \n 2- Показать все заметки\n 3- Редактировать заметку\n 4- Удалить заметку\n 5- Выход из меню\n')
    # Проверяем, что пользователь ввел число из диапазона меню от1 до 5
    while True:
        menu = input('\nВведите пункт меню ')
        try:
            menu = int(menu)
        except ValueError:
            print('\nВведите пункт меню цифрами! Буквы вводить запрещено!')
            continue
        if 0 < menu < 6:
            break
        else:
            print('\nВ меню отсутствует данный пункт. Введите значения из диапазона от 1 до 5')

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
