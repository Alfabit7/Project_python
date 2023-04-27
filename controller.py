import view


def start():
    while True:
        menu = view.ShowMenu()
        if menu == 7:
            return "Exit from programm"
