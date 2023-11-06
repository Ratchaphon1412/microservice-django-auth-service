from ..interface.topicinterface import TopicInterface
from User.models import UserProfiles
import json
class Listener:
    def run(topic,message):
        
        if topic == "payment_customer":
            TopicUserCreate.action(message)
        elif topic == "user_update":
            TopicUserUpdate.action(message)
        else:
            pass


class TopicUserCreate(TopicInterface):
    def action( message):
        message_decode = message.decode('utf-8')
        
        data = json.loads(message_decode)
        print(data)
        print("User Create")
        try :
           user = UserProfiles.objects.get(id=data.get('id'))
           user.customer_omise_id =data.get('customer_omise_id')
           user.save()
        except  Exception as e:
            print(e)
            pass
        
        
        
        

class TopicUserUpdate(TopicInterface):
    def action( message):
        print("User Update")