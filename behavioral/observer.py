import time
from abc import ABC, abstractmethod


class YouTubeChannel(ABC):

    def __init__(self):
        self.subscribers = []

    def add_subscriber(self, subscriber):
        self.subscribers.append(subscriber)

    def delete_subscriber(self, subscriber):
        if subscriber in self.subscribers:
            self.subscribers.remove(subscriber)

    def notify_all_subcribers(self, notification):
        for subscriber in self.subscribers:
            self.notify_subscriber(subscriber, notification)

    def notify_subscriber(self, subscriber, notification):
        subscriber.notifications.append(notification)

    @abstractmethod
    def upload_video(self, video_name):
        pass

    @abstractmethod
    def live_streaming(self):
        pass


class CrashCourse(YouTubeChannel):

    def __init__(self, channel):
        super().__init__()
        self.channel = channel

    def upload_video(self, video_name):
        now = time.strftime("%Y%m%d-%H%M%S")
        msg = f"[{now}] ({self.channel}) {video_name} has just uploaded"
        self.notify_all_subcribers(msg)

    def live_streaming(self):
        now = time.strftime("%Y%m%d-%H%M%S")
        msg = f"[{now}] ({self.channel}) Live streaming is going on!"
        self.notify_all_subcribers(msg)


class YouTubeUser(object):

    def __init__(self, name):
        self.name = name
        self.notifications = []

    def subscribe(self, channel):
        channel.add_subscriber(self)


def main():
    crashcourse = CrashCourse("crashcourse")
    john = YouTubeUser("john")
    mary = YouTubeUser("mary")

    john.subscribe(crashcourse)
    mary.subscribe(crashcourse)

    crashcourse.upload_video("CS101-HelloWorld")

    for person in [john, mary]:
        print(person.notifications)


if __name__ == "__main__":
    main()
