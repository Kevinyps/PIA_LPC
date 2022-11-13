import optparse
from PIL import Image
from PIL.ExifTags import TAGS
import logging

def metadata_img(img):
    logging.info('Búsqueda de metadatos iniciada')
    try:
        info= Image.open(img)
        data = info.getexif()
        metadatos = dict()

        
        for tag, valores in data.items(): 
            code = TAGS.get(tag, tag)
            metadatos[code] = valores
        print ("...")
        print ("\t\t METADATOS DE %s" %img)
        print ("...")
        if metadatos:
            for meta_info in metadatos:
                print ("[x] ", meta_info , ":" , metadatos[meta_info])
                f = open('metadatos.txt', 'w')
                f.write("[x] ", meta_info , ":" , metadatos[meta_info])
                f.close
                logging.info('Búsqueda de metadatos terminada')
        else:
            print ("[x] Los Metadatos No existen!")
            f = open('metadatos.txt', 'w')
            f.write("[x] Los Metadatos No existen!")
            f.close
            logging.warning('Error en búsqueda de metadatos')
    except:
        logging.warning('Error en path ingresado para obtencion de datos de imagen')

def main():

    parser = optparse.OptionParser("./prog -I <Ruta de la imagen>")
    parser.add_option("-I", dest="Name_IMG", help="Escribe el nombre de la IMG", type="string")

    (options, args) = parser.parse_args()

    img = options.Name_IMG

    if img == None:
        print ("[x] La IMG no existe")
        parser.print_help()
        exit(0)
    else:
        metadata_img(img)

if __name__ == "__main__":
    main()