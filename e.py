from flask_mail import Mail, Message
from myapp import app
mail = Mail(app)
def send_email(to, subject, template):
    msg = Message(

        subject,
        recipients=[to],
        html=template,
        sender=app.config['MAIL_DEFAULT_SENDER']
    )
    mail.send(msg)