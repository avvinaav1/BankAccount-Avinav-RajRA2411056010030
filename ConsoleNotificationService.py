from NotificationService import NotificationService


class ConsoleNotificationService(NotificationService):

    def send(self, message):
        print(f"Sending: {message}")
