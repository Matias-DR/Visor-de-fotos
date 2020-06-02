from PySimpleGUI import *
from imagenes import *

def elementos(tipo):
	if tipo=='menu':
		return	[
					[
						Image(
								'media/carta/sobre.png',
								pad=(0, 0))
					], 
					[
						Button(
								'Ver fotos',
								size=(15, 0),
								pad=(2, 2),
								border_width=0,
								button_color=('#292929', '#292929'),
								image_filename=botonRandom(),
								image_size=(120, 120)),
						Button(
								'Salir',
								size=(15, 0),
								pad=(2, 2),
								border_width=0,
								button_color=('#292929', '#292929'),
								image_filename=botonRandom(),
								image_size=(120, 120))
					]
				]