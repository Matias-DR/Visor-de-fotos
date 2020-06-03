from PySimpleGUI import *
from items import *


def menu():
    ventana = Window('Visor', elementos('menu'),
                     margins=(1, 1),
                     resizable=True,
                     text_justification='center',
                     background_color='#242424',
                     finalize=True)

# def visor():
#  ventana=Window('Visor', elementos('visor'),
#                 size=(253, 473),
#                 margins=(1, 1),
#                 location=(380, 30),
#                 resizable=True,
#                 text_justification='center',
#                 background_color='#242424',
#                 return_keyboard_events=True,
#                 finalize=True
#                )

    while True:
        evento, valor = ventana.read()
        if evento in (None, 'Salir'):
            break
    ventana.close()


menu()
