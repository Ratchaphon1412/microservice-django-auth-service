from ..interface.topicinterface import TopicInterface


class Listener:
    def run(topic,message):
        
        if topic == "test":
            TopicUserCreate.action(message)
        elif topic == "user_update":
            TopicUserUpdate.action(message)
        else:
            pass


class TopicUserCreate(TopicInterface):
    def action( message):
        print("User Create")

class TopicUserUpdate(TopicInterface):
    def action( message):
        print("User Update")