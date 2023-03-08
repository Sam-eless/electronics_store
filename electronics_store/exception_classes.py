class InstantiateCSVError(Exception):
    """Класс-исключение"""
    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else "Файл поврежден"

    def __str__(self):
        return self.message