import os


class Config:

    QUOTE_API_BASE_URL = 'http://quotes.stormconsultancy.co.uk/random.json'
    SECRET_KEY = 'kwepo12345'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:7710@localhost/blogs'

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOADED_PHOTOS_DEST = 'app/static/photos'

    #  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'kelvinwepo7710@gmail.com'
    MAIL_PASSWORD = '33193060'

    # simple mde  configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True


class ProdConfig(Config):
    uri = os.getenv('DATABASE_URL')
    if uri and uri.startswith('postgres://'):
        uri = uri.replace('postgres://', 'postgresql://', 1)
        
    SQLALCHEMY_DATABASE_URI = uri


class DevConfig(Config):
    # SQLALCHEMY__URI = 'postgresql+psycopg2://postgres:password@localhost/blogs'
    SQLALCHEMY_DATABASE_URI = (
        'postgresql://xbytshqrcnejxz:073bbb312ba84b40bcc07df260858ddbf3bfa9b7b9a73d529b59b067cbeb4ccb@ec2-52-207-74-100.compute-1.amazonaws.com:5432/ddhs9q1bi4ab55')
    DEBUG = True


config_options = {
    'development': DevConfig,
    'production': ProdConfig,
}

