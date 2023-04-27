#  Словарь myNote Хранит заметки пользователя
myNote = dict()


def addNote():
    addTitle = input("Введите название заметки: ")
    addMsg = input("Введите заметку: ")
    myNote[addTitle] = addMsg
    print('\n Заметка добавлена')


def ShowAllNotion():
    if len(myNote) == 0:
        print('\n Заметок нет')
    else:
        print(myNote.items())


def EditNotion():
    userKeys = input(
        '\n Введите заголовок заметки, которую хотите отредактировать: ')
    userMsg = input(
        '\n Введите текст редактирования заметки: ')
    myNote[userKeys] = userMsg
    print('\n Заметка отредактированна')


def DeleteNotion():
    userKeys = input(
        '\n Введите заголовок заметки, которую хотите удалить: ')
    myNote.pop(userKeys)
    print('\n Заметка удалена')
