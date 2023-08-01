import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders


def main():
    email_user = input("what is your gmail address? \n ")
    email_password = input("what is the password for that email address? \n  ")
    email_rcver = input("what email address do you want to send to? \n ")

    # subject = input("Subject of the email : \n ")

    # email_user = 'goldenshark0702@gmail.com'
    # email_password = 'goldenshark1!G'
    # email_rcver = 'goldenshark0805@gmail.com'

    subject = 'Welcome !'

    msg = MIMEMultipart()
    msg['From'] = email_user
    msg['To'] = email_rcver
    msg['Subject'] = subject

    # body = input("write down body of the email : \n ")
    body = 'Hi. Plz contact me. Regards.'
    msg.attach(MIMEText(body, 'plain'))

    # filename = input("Enter filepath of the file you want to upload : \n ")
    # filename = 'test.pdf'
    # attachment = open(filename, 'rb')

    # part = MIMEBase('application', 'octet-stream')
    # part.set_payload(attachment.read())
    # encoders.encode_base64(part)
    # part.add_header('content-disposition', "attachment; filename= "+filename)

    # msg.attach(part)
    # text = msg.as_string()

    # server = smtplib.SMTP('smtp.gmail.com', 587)
    # server.starttls()
    # server.login(email_user, email_password)

    # server.sendmail(email_user, email_rcver, text)
    server.quit()

    print("Sent!")


if __name__ == "__main__":
    main()
