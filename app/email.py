from . import mail
from flask_mail import Message
from flask import render_template

def create_mail(subject,template,to,**kwargs):

    message = Message(subject,sender="zubkayare@gmail.com",recipients = [to])
    message.body = render_template(template + ".txt", **kwargs)
    mail.send(message)
