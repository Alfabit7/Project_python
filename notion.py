#  Словарь myNote Хранит заметки пользователя
import datetime
# myNote = {id: [date, title, msg, editDate}]}
myNote = dict()


date = None
currentDate = None
id = None

# Функция получения текущей даты ивремени и фомрирования ID сосотоящего из даты


def requestDatetime():
    date = datetime.datetime.now()
    currentDate = date.strftime("%d-%b-%Y (%H:%M:%S)")
    id = date.strftime("%d%m%Y%H%M%S%f")
    dateAndId = [id, currentDate]
    return dateAndId

# функция добавления заметок


def addNote():
    dateID = requestDatetime()
    addTitle = input("Введите название заметки: ")
    addMsg = input("Введите заметку: ")
    myNote[dateID[0]] = [dateID[1], addTitle, addMsg]
    # myNote[id]=[]
    print(
        f'\nЗаметка c id {dateID[0]} добавлена {currentDate}')

# функция отображения всех заметок


def ShowAllNotion():
    if len(myNote) == 0:
        print('\n Заметок нет')
    else:
        print(myNote.items())

# функция редактирования заметки


def EditNotion():
    if len(myNote) > 0:
        dateID = requestDatetime()
        userID = input(
            '\n Введите ID заметки, которую хотите отредактировать: ')
        if userID in myNote:
            userTitle = input(
                '\n Введите/(отредактируйте) заголовок заметки: ')
            userMsg = input(
                '\n Введите/(отредактируйте) сообщение заметки: ')

            myNote[userID][1] = userTitle
            myNote[userID][2] = userMsg
            # добавляем\ else - меняем дату редактирования заметки
            if len(myNote[userID]) == 3:
                myNote[userID].append(dateID[1])
            else:
                myNote[userID][3] = dateID[1]
            print(
                f'\nЗаметка c id {userID} отредактированна {dateID[1]} ')
        else:
            print(
                f'\n Заметки с ID {userID} в списке нет проверьте правильность ввода ID')
    else:
        print(
            'Список заметок пуст редактировать нечего')

# функция удаления заметок


def DeleteNotion():
    userKeys = input(
        '\nВведите ID заметки, которую хотите удалить: ')
    myNote.pop(userKeys)
    print('\n Заметка удалена')
