import smtplib

to = input("enter the email address of the receiver:")
message = input("enter the message:")

def sendEmail(to,message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('spywork01@gmail.com','deepasunnyspy')
    server.sendmail('spywork01@gmail.com',to, message)
    server.close()

# Remove the recursive call
sendEmail()
