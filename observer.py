class Subject:
    def __init__(self, name, desc="Description"):
        self.name = name
        self.desc = desc
        self.data = None
        self.subscribers = set()

    def __del__(self):
        pass

    def data_update(self, _update):
        pass

    def update(self, _update):

        self.data_update(_update)

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
        self.subjects = set()

    def addSubject(self, _subject):
        self.subjects.add(_subject)  

    def createSubject(self, _subName):
        _subject = Subject(_subName)
        self.subjects.add(_subject)
        return _subject

    def deleteSubject(self, _subject):
        self.discard(_subject)

    def publish(self, _subject, _update):
        if (_subject in self.subjects):
            _subject.update(_update)
        else:
            print("[Access Denied], you are not authorized to send updates in this group")
