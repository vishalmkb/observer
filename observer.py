class Subscriber:
    def __init__(self, name):
        self.name = name
    def getNotified(self, message):
        print('{} got message "{}"'.format(self.name, message))
        
class Publisher:
    def __init__(self):
        self.subscribers = set()
    def register(self, who):
        self.subscribers.add(who)
    def unregister(self, who):
        self.subscribers.discard(who)
    def update(self, message):
        for subscriber in self.subscribers:
            subscriber.getNotified(message)


