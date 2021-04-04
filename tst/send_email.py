import random
import smtplib, ssl
import string
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "adhyaromemes@gmail.com"  # Enter your address
# receiver_email = "tchiring08@gmail.com"  # Enter receiver address
password = "sonyericsson12345"
subject = "Important! Password Reset!"
context = ssl.create_default_context()


def random_pass():
    letters = string.ascii_lowercase
    random_new_pass = ''.join(random.choice(letters) for i in range(8))
    return random_new_pass


def send_mail(receiver_email):
    new_pass = random_pass()
    message = """\
    From: {}
    Subject: Important! Password Reset!

    Greeting from Video Steganography. You have requested for a password reset.

    Your new Password is : {}

    Please change this password after logging in.
    """.format(sender_email, new_pass)

    # message = """From: From Person <from@fromdomain.com>
    # To: To Person <to@todomain.com>
    # Subject: SMTP e-mail test
    #
    # This is a test e-mail message.
    # """

    # message = MIMEMultipart("alternative")
    # message["From"] = sender_email
    # message["To"] = receiver_email
    # message["Subject"] = subject
    # message.attach(MIMEText(body, "plain"))

    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)

# if __name__ == '__main__':
#     random_pass()
