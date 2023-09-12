import abc 

class TopicInterface(abc.ABC):
    @abc.abstractmethod
    def action( message):
        pass
