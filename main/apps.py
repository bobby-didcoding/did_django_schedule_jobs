from django.apps import AppConfig


class MainConfig(AppConfig):
    name = 'main'

    def ready(self):
    	from jobs import updater
    	updater.start()
