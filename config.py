import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    # Sercret key
    SECRET_KEY = os.getenv('SECRET_KEY', default='you-will-never-guess')

    # Database
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', default='sqlite:///' + os.path.join(basedir, 'app.db'))
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Email error notificacion conf
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = ['jtamayoh@gmail.com']
