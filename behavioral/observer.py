import time


class YouTubeChannel(object):

    def __init__(self, channel_name):
        self.subscribers = []
        self.channel_name = channel_name

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

    def upload_video(self, video_name):
        now = time.strftime("%Y%m%d-%H%M%S")
        msg = f"[{now}] ({self.channel_name}) {video_name} has just uploaded"
        self.notify_all_subcribers(msg)

    def live_streaming(self):
        now = time.strftime("%Y%m%d-%H%M%S")
        msg = f"[{now}] ({self.channel_name}) Live streaming is going on!"
        self.notify_all_subcribers(msg)


class YouTubeUser(object):

    def __init__(self, name):
        self.name = name
        self.notifications = []

    def subscribe(self, channel):
        channel.add_subscriber(self)


def main():
    crashcourse = YouTubeChannel("CrashCourse")
    national_geographic = YouTubeChannel("NationalGeographic")

    john = YouTubeUser("john")
    mary = YouTubeUser("mary")

    john.subscribe(crashcourse)
    mary.subscribe(crashcourse)

    john.subscribe(national_geographic)

    crashcourse.upload_video("CS101-HelloWorld")
    national_geographic.live_streaming()

    # check notifications
    for person in [john, mary]:
        print(person.notifications)


if __name__ == "__main__":
    main()
