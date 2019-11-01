import smtplib

email = 'goodshepherdiot@gamil.com'  # your email
password = 'P@ssword#1'  # your email account password
sent_to_email = 'rhysjames351@gmail.com'  # recipient
message = 'No, this isn"t in the message.'  # messag in the body of email

server = smtplib.SMTP('smtp.gmail.com', 587)  # connect to teh server
server.starttls()  # use TLS (transport layer security)
server.login(email, password)
server.sendmail(email,send_to_email, message)
server.quit(fg)