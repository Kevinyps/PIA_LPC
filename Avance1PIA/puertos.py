import subprocess
import logging


def analisisPuertos(ip):
    logging.info('Búsqueda de puertos iniciada')
    try:
        # Abrimos los txt en donde están las veces que vamos a repetir el proceso
        fo = open(ip, 'r')
        foo = open("registroPuertos.txt", 'w')
        # Repetimos el proceso por cada ip
        for ip in fo:
            direccion = ip
            # Llamamos a nuestra función de powershell
            comando = "powershell -ExecutionPolicy ByPass -File EscanerPuertos.ps1 -direccion_ip " + str(direccion)
            # Guardamos la salida del proceso
            try:
                procesoPowerShell = subprocess.check_output(comando)
                foo.write(procesoPowerShell.decode())
                foo.write("\n\n")
            except Exception as e:
                foo.write("Puerto: " + str(ip) + "\n")
                foo.write(str(e))
                foo.write("\n\n")
                logging.warning('Error en búsqueda de puertos')
        # Guardamos lo escrito en nuestro txt
        logging.info('Búsqueda de puertos terminada')
        fo.close()
        foo.close()
    except:
        logging.warning('Error en path ingresado del txt con el numero de veces a repetir proceso')