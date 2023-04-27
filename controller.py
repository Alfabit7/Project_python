import view
import notion


# def start():
#     while True:
#         menu = view.ShowMenu()
#         if menu == 1:
#             notion.addNote()
#         elif menu == 2:
#             break

def start():
    while True:
        menu = view.ShowMenu()
        if menu == 5:
            return "Exit to programm"
