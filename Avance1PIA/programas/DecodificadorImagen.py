import base64
import logging

def decodificadorimg(link):
	logging.info('Decodificacion de imagen iniciada')
	try:
		file = open(link,'rb')
		byte = file.read()
		file.close()

		decodeit = open('imagendecodificada.jpg','wb')
		decodeit.write(base64.b64decode((byte)))
		decodeit.close()
		logging.info('Decodificacion de imagen finalizada')
	except:
		logging.warning('Error en path ingresado de la imagen')