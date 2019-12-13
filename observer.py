class Subject:
    def __init__(self, name, desc="Description"):
        self.name = name
        self.desc = desc
        self.data = None
        self.subscribers = set()

    def update(self, _update):
        for _subscriber in self.subscribers:
            _subscriber.getNotified(_update)
        
    def register(self, _subscriber):
        self.subscribers.add(_subscriber)

    def unregister(self, _subscriber):
        self.subscribers.discard(_subscriber)
        

class Subscriber:

    def __init__(self, name):
        self.name = name
        
    def getNotified(self, _update):
        pass

    
class Publisher:

    def __init__(self, name):
        self.name = name
        self.subjects = dict()

    def publish(self, _subject, _update):
        _subject.update(_update)
