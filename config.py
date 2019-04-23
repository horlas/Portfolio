import os


WTF_CSRF_ENABLED = True
SECRET_KEY = os.environ.get('SECRET_KEY')

# Todo : crsf WTF_CSRF_ENABLED = True
# email server

MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 465
MAIL_USE_TLS = False
MAIL_USE_SSL = True
MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')

# administrator list
ADMINS = ['aurelia.gourbere@gmail.com']

