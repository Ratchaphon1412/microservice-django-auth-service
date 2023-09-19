from .factory.security import Security
from .factory.email import Email

class Facade:
 
    
    
    def securityService():
        return Security()
    
    
    def notificationService():
        return Email()
    