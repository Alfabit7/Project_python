#  Словарь myNote Хранит заметки пользователя
import csv
import datetime
# myNote = {id: [id date, title, msg, editDate}]}
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
            if userTitle == '':
                return
            else:
                myNote[userID][1] = userTitle
            if userMsg == '':
                return
            else:
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
            '\n Список заметок пуст, редактировать нечего')


# функция удаления заметок

def DeleteNotion():
    if len(myNote) > 0:

        userID = input(
            '\nВведите ID заметки, которую хотите удалить: ')
        if userID in myNote:
            myNote.pop(userID)
            print(f'\n Заметка с  ID {userID} удалена ')
        else:
            print(
                f'\n Заметки с ID {userID} в списке нет проверьте правильность ввода ID')
    else:
        print(
            '\n Список заметок пуст, удалять нечего')


def SaveBase():
    with open('myNote.csv', 'w', newline='', encoding='UTF-8-sig') as file:
        writer = csv.writer(file, delimiter=';')
        # Записываем заголовок
        writer.writerow(['Number_id', 'Date', 'Title', 'Msg', 'EditDate'])
        # Записываем данные
        for number_id, data in myNote.items():
            writer.writerow([number_id]+data)
