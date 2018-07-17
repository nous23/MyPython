import smtplib

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

sender = 'cchen23@outlook.com'
password = 'wentworthy23'
receiver = '459877442@qq.com'

subject = 'test'

msg = MIMEMultipart()
msg['From'] = sender
msg['To'] = receiver
msg['Subject'] = subject

email_body = 'Hello World'
msg.attach(MIMEText(email_body, 'plain'))

email_content = msg.as_string()

server = smtplib.SMTP('smtp-mail.outlook.com:587')

server.starttls()
server.login(sender, password)
server.sendmail(sender, password, email_content)
server.quit()