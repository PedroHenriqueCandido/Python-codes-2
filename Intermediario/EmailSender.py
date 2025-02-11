import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def enviar_email(subject, body, to_email):
    from_email = 'seu_email@gmail.com'  # Substitua pelo seu e-mail
    password = 'sua_senha_de_app'  # Substitua pela senha gerada pelo app (no caso de 2FA)


    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject


    msg.attach(MIMEText(body, 'plain'))

    try:
     
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()  
        server.login(from_email, password)
        text = msg.as_string()

        # Enviar o e-mail
        server.sendmail(from_email, to_email, text)
        server.quit()  

        print(f'E-mail enviado com sucesso para {to_email}')

    except Exception as e:
        print(f'Ocorreu um erro ao enviar o e-mail: {e}')


enviar_email(
    subject='Teste de Envio de E-mail',
    body='Olá! Este é um e-mail enviado automaticamente.',
    to_email='destinatario@example.com'  # Substitua pelo e-mail do destinatário
)
