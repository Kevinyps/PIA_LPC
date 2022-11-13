import argparse
import logging
from programas.webscrap import imagenes
from programas.codificador import codificadorimg
from ImgMeta import metadata_img
from puertos import analisisPuertos
from programas.analizarUrl import analizarUrl
from programas.DecodificadorImagen import decodificadorimg

logging.basicConfig(filename='PIA.log', level=logging.INFO, 
					format='%(levelname)s:%(asctime)s:%(message)s')

ayudarinfo = 	("Script diseñado para tener distintas herramientas de seguridad"
				"\n WebScraping para extraccion de imagenes utiliza -w"
				"\n Codificacion en base64 de imagenes utiliza -ci"
				"\n Codificacion en base64 de imagenes utiliza -di"
				"\n Recopilar metadatos de imagenes utiliza -IM"
				"\n Mapear puertos abiertos de servidor local utiliza -p"
				"\n Análisis de urls con VirusTotal utilice los parámetros -a y -tv.")

analizar = argparse.ArgumentParser(ayudarinfo)
analizar.add_argument('-w', '--webscraping', type=str, 
						help="Te ayuda a extraer imagenes de url's")
analizar.add_argument('-ci', '--codifimag', type= str,
						help="Lograr codificar imagenes extraidas")
analizar.add_argument('-di', '--decodifimag', type= str,
						help="Lograr decodificar imagenes codificadas")
analizar.add_argument('-IM', '--imagmet', type= str,
						help="Ayuda a obtener metadatos de imagenes")
analizar.add_argument('-p', '--mapeopuerto', type= str,
						help="Herramienta para mapeo de puertos")
analizar.add_argument('-au', '--analizaURL', type= str,
						help="Herramienta para mapeo de puertos")
analizar.add_argument('-tv', '--txtvirus', type=str,
                    	help="Nombre del archivo con las urls")

argumentos = analizar.parse_args()

if argumentos.webscraping is not None:
	imagenes(argumentos.webscraping)

elif argumentos.codifimag is not None:
	codificadorimg(argumentos.codifimag)

elif argumentos.decodifimag is not None:
	decodificadorimg(argumentos.decodifimag)

elif argumentos.imagmet is not None:
	metadata_img(argumentos.imagmet)

elif argumentos.mapeopuerto is not None:
	analisisPuertos(argumentos.mapeopuerto)

elif argumentos.analizaURL is not None:
	analizarUrl(argumentos.txtvirus, argumentos.analizaURL)