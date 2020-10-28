import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#Função chamada para enviar email via SMTP
def smtpsend(texto):
    #cria um objeto com o corpo do texto do gmail
    msg = MIMEMultipart()
    # Necessários os arquivos com email e senha do remetente e outro com a denúncia
    f = open('login.txt','r')
    f1 = open('senha.txt','r')
    msg['From'] = f.readline()
    mypass = f1.readline()
    corpo = texto
    f.close()
    f1.close()

    msg['Subject'] = 'Denúncia de ciclista em pernambuco via databikePE'
    msg['To'] = 'lags@cesar.school'
    #função para juntar o corpo do texto no resto do objeto
    msg.attach(MIMEText(corpo, 'plain'))
    
    smtp = smtplib.SMTP('smtp.gmail.com', 587)
    smtp.starttls()
    #autentificação do email
    smtp.login(msg['From'], mypass)
    #envio de email
    smtp.sendmail(msg['From'], msg['To'], msg.as_string())
    
    smtp.quit()
    
    print("\nEmail foi enviado para ",msg['To']," com sucesso!\n")
    
    