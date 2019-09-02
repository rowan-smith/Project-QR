import os


class Config(object):
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # THREADS_PER_PAGE = 2
    THREADS_PER_PAGE = 8

    WTF_CSRF_ENABLED = True

    CSRF_SESSION_KEY = os.getenv('CSRF_SESSION_KEY')

    # Secret key for signing cookies
    if os.environ.get('SECRET_KEY'):
        SECRET_KEY = os.environ.get('SECRET_KEY')
    else:
        SECRET_KEY = 'anYr7h=tj9x&MLr!SeW$s(4UHp&h8'

    @staticmethod
    def init_app(app):
        pass


class ProductionConfig(Config):
    # Database Settings
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///QR-Users.db'


class DevelopmentConfig(Config):

    # Database Settings
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///dev.db'

    # Debug Settings
    DEBUG = True

    # Testing Settings
    TESTING = True

    # DEV
    DEVELOPMENT = True
