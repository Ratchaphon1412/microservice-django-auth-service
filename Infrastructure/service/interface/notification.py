import abc

class Notification(abc.ABC):
    @abc.abstractmethod
    def send(self, message):
        pass