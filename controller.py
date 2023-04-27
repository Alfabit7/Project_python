import view


def start():
    while True:
        menu = view.ShowMenu()
        if menu == 6:
            return "Exit from programm"
