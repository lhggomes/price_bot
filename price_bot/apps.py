from django.apps import AppConfig


class RoomConfig(AppConfig):
    name = 'price_bot'

    def ready(self):
        from . import updater
        updater.start()
