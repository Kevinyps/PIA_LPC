import os
import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook
import re
import logging

def imagenes(link): 
    logging.info('Búsqueda de imagenes iniciada')
    try: 
            r = requests.get(link)  
            URL = r.text  
            soup_8= BeautifulSoup(URL, 'html.parser')  
         
            
            link_img=[]
               #como las imagenes que consigue tienen extension png y jpg
            #utilizamos una expresion regular para filtrar solamente los jpg
            x=0
            for item in soup_8.find_all('img',{'src':re.compile('.jpg')}): 
              #como la busqueda de los jpg lo guardaba en una sola variable
              #en item['src'], usamos otra expresión regular para  separarlos y
              #almacenarlos en una lista
                texto_link = re.compile(r'(/[^\s]+\.+\w{3})')
                pos_link = item['src']
                mo = texto_link.search(pos_link)
                link_img.append("http:" + mo.group())
                #print(x)
                x+=1
                for image in link_img:
                    with open("result" + str(x)+ '.jpg', 'wb') as f:
                        res = requests.get(image)
                        f.write(res.content)
                        f.close()
            logging.info('Búsqueda de imagenes finalizada')
    except:
        logging.warning('Error en la URL ingresada')