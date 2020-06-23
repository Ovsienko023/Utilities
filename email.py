import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# VterminaleBot@gmail.com

addr_from = "vterminalebot@gmail.com"                 # Адресат
addr_to   = "ovsienko023@gmail.com"                   # Получатель
password  = "my password"                             # Пароль

msg = MIMEMultipart()                               # Создаем сообщение
msg['From']    = addr_from                          # Адресат
msg['To']      = addr_to                            # Получатель
msg['Subject'] = 'Тема сообщения'                   # Тема сообщения

body = "Текст сообщения"
msg.attach(MIMEText(body, 'plain'))                 # Добавляем в сообщение текст

server = smtplib.SMTP_SSL('imap.gmail.com', 465)    # Создаем объект SMTP
#server.starttls()                                  # Начинаем шифрованный обмен по TLS
server.login(addr_from, password)                   # Получаем доступ
server.send_message(msg)                            # Отправляем сообщение
server.quit()  
