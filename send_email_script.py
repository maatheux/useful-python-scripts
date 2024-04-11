import win32com.client as win32
import datetime
from email.message import EmailMessage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication
from os.path import basename
import smtplib
from get_day import GetDay
from update_email_image import update_image


today = GetDay()

hourNow = datetime.datetime.now()

if hourNow.strftime("%p") == 'AM':
    mornOrAfternoon = 'Bom dia'
else:
    mornOrAfternoon = 'Boa tarde'

def send_email():
    update_image()

    msg = MIMEMultipart('related')
    msg["Subject"] = f'' # titulo email
    msg["To"] = 'fulano@hotmail.com, siclano@hotmail.com'
    msg["From"] = 'beltrano@hotmail.com'

    msg_alternative = MIMEMultipart('alternative')
    msg.attach(msg_alternative)

    msg_text = MIMEText(f"<p>Olá, pessoal. {mornOrAfternoon}!</p><p>Segue o relatório de <b>Acompanhamento</b> atualizado.</p><br><br><img src=""cid:MyId1"" alt='Imagem nao encontrada'><br><p>Responsável Atualização: Clever</p><img src=""cid:MyId2"" alt='Imagem nao encontrada'><br>", 'html')
    msg_alternative.attach(msg_text)

    table_img = open(r'imgs\imagem.png', 'rb') # path
    msg_img = MIMEImage(table_img.read())
    table_img.close()
    msg_img.add_header('Content-ID', '<MyId1>')
    msg.attach(msg_img)

    signature_img = open(r'imgs\signature.PNG', 'rb')
    msg_img = MIMEImage(signature_img.read())
    signature_img.close()
    msg_img.add_header('Content-ID', '<MyId2>')
    msg.attach(msg_img)

    excel_file = r'003_Acompanhamento\Relatorio.xlsm'

    file_atach = open(excel_file, "rb")
    part = MIMEApplication(file_atach.read(), Name=basename(excel_file))
    file_atach.close()
    
    part['Content-Disposition'] = 'atachament; filename="%s"' % basename(excel_file)
    msg.attach(part)

    host = "hostname"
    port = 587
    
    server = smtplib.SMTP(host,port)
    server.send_message(msg)
    server.quit()

if __name__ == '__main__':
    send_email()
