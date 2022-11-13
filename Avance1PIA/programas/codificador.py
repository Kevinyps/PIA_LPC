import base64
import logging


def codificadorimg(link):
	logging.info('Codificacion de imagen iniciada')
	try:
		with open(link, "rb") as image2string:
			converted_string = base64.b64encode(image2string.read())
		#print(converted_string)

		with open('imagen_codificada.txt' , "wb") as file:
			file.write(converted_string)
		logging.info('Codificacion de imagen finalizada')

	except:
		logging.warning('Error en path ingresado de la imagen')