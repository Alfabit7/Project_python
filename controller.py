import view


def start():
    while True:
        menu = view.ShowMenu()
        if menu == 5:
            return "Exit to programm"
