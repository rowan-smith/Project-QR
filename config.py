import os

SECRET_KEY_PASSWORD = "CHANGE_ME_PLZ"


class Config(object):
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    THREADS_PER_PAGE = 8

    DEBUG = False
    DEVELOPMENT = False
    TESTING = False

    # CSRF Settings
    WTF_CSRF_ENABLED = True
    CSRF_ENABLED = True
    CSRF_SESSION_KEY = os.getenv(SECRET_KEY_PASSWORD)

    # Secret key for signing cookies
    if os.environ.get('SECRET_KEY'):
        SECRET_KEY = os.environ.get('SECRET_KEY')
    else:
        SECRET_KEY = SECRET_KEY_PASSWORD

    @staticmethod
    def init_app(app):
        pass


class ProductionConfig(Config):
    # Database Settings
    SQLALCHEMY_DATABASE_URI = 'sqlite:///QR-Users.db'


class DevelopmentConfig(Config):
    # Database Settings
    SQLALCHEMY_DATABASE_URI = 'sqlite:///dev.db'

    # Debug Settings
    DEBUG = True

    # Testing Settings
    TESTING = True

    # DEV
    DEVELOPMENT = True
