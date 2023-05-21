from django.apps import AppConfig


class StudentConfig(AppConfig):
    name = "students"

    def ready(self):
        import students.signals
