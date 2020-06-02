from random import *

def botonRandom():
	nro=randrange(7)
	if nro==0:
		return 'media/botones/f01.png'
	elif nro==1:
		return 'media/botones/f11.png'
	elif nro==2:
		return 'media/botones/f02.png'
	elif nro==3:
		return 'media/botones/f22.png'
	elif nro==4:
		return 'media/botones/f03.png'
	elif nro==5:
		return 'media/botones/f33.png'
	elif nro==6:
		return 'media/botones/f04.png'
	elif nro==7:
		return 'media/botones/f44.png'

def fotoRandom():
	nro=randrange(4)
	if nro==0:
		return 'media/vapor/vapor0.png'
	if nro==1:
		return 'media/vapor/vapor1.png'
	if nro==2:
		return 'media/vapor/vapor2.png'
	if nro==3:
		return 'media/vapor/vapor3.png'
	if nro==4:
		return 'media/vapor/vapor4.png'