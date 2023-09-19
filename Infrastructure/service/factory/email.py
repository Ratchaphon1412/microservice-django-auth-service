from ..interface.notification import Notification
from django.conf import settings
from django.core.mail import EmailMessage
from django.template.loader import get_template
from django.template import Context



class Email(Notification):
    def __init__(self):
        self.email_host = settings.EMAIL_HOST_USER
    
    def send(self,data):
        try:
            email_template = get_template(data['template']).render({
                'data':data['dataBinding']
                
            })
            mail = EmailMessage(
                subject=data['subject'],
                body=email_template,
                from_email=self.email_host,
                to=data['to']
            )
            mail.content_subtype = "html"
            mail.send()
             
        except Exception as e:
            print(e)
            return False    
        
        