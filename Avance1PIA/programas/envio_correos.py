import smtplib, os, logging
from email.mime.multipart import MIMEMultipart
from email.mime.text      import MIMEText
from email.mime.multipart import MIMEBase
from email.encoders       import encode_base64

def envioCorreos(dest):
    user = "kevin.yair.pena.salazar@gmail.com"
    pswd = "oipbjdspxhdhaxcm "

    #Para las cabeceras del email
    remitente  = "kevin.yair.pena.salazar@gmail.com"
    destinatario = dest
    asunto = "Log PIA"
    mensaje = "Aqui encontraras adjunto el log del programa"
    archivo = "C:\\Users\Kevin Peña\Desktop\Git PIA\PIA_LPC\Avance1PIA\PIA.log"
    #Host y puerto smtp
    conn = smtplib.SMTP('smtp.gmail.com', 587)

    #Protocolo de cifrado
    conn.starttls()

    #Credenciales
    conn.login(user, pswd)

    header = MIMEMultipart()
    header['Subject'] = asunto
    header['From']    = remitente
    header['To']      = destinatario
    mensaje = MIMEText(mensaje, 'html')
    header.attach(mensaje)

    if(os.path.isfile(archivo)):
        adjunto = MIMEBase('aplication','octet-stream')
        adjunto.set_payload(open(archivo,'rb').read())
        encode_base64(adjunto)
        adjunto.add_header('Content-Disposition','attachment; filename= "%s" ' % os.path.basename(archivo))
        header.attach(adjunto)
    else:
       print('Error en path ingresado')
    #Enviar Gmail
    if conn.sendmail(remitente,destinatario,header.as_string()) == {}:
        logging.info('Envio exitoso')

    #Cierre de conexion
    conn.quit()
