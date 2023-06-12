class YoutubeChannel:
    def __init__(self, name):
        self.name = name
        self.subscribers = []

    def subscribe(self, subscriber):
        self.subscribers.append(subscriber)

    def notify(self, event):
        for subscriber in self.subscribers:
            subscriber.sendNotification(self.name, event)


from abc import ABC, abstractmethod


class YoutubeSubscriber(ABC):
    @abstractmethod
    def sendNotification(self, channelName, event):
        pass


class YoutubeUser(YoutubeSubscriber):
    def __init__(self, name):
        self.name = name

    def sendNotification(self, channelName, event):
        print(f"{self.name} received notification from {channelName}: {event}")


channel = YoutubeChannel("T.K. from Tokyo")

channel.subscribe(YoutubeUser("Alice"))
channel.subscribe(YoutubeUser("Bob"))

channel.notify("A new video has been uploaded!")
