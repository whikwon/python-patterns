from abc import ABC, abstractmethod


class IOS(object):

    def __init__(self, mail_manager, calendar_manager):
        self.mail_manager = mail_manager
        self.calendar_manager = calendar_manager

    def send_email(self):
        self.mail_manager.send_email()

    def add_appointment(self):
        self.calendar_manager.add_appointment()


class MailManager(ABC):

    @abstractmethod
    def send_email(self):
        pass


class GMail(MailManager):

    def send_email(self):
        print("Sent e-mail to your manager by GMail.")


class NaverMail(MailManager):

    def send_email(self):
        print("Sent e-mail to your manager by NaverMail.")


class CalendarManager(ABC):

    @abstractmethod
    def add_appointment(self):
        pass


class GoogleCalendar(CalendarManager):

    def add_appointment(self):
        print("Added appointment to your google calendar.")


class NaverCalendar(CalendarManager):

    def add_appointment(self):
        print("Added appointment to your naver calendar.")


def main():
    mail_manager = GMail()
    calendar_manager = GoogleCalendar()

    os = IOS(mail_manager, calendar_manager)
    os.send_email()
    os.add_appointment()


if __name__ == "__main__":
    main()
