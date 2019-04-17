import os


# class Config(object):
#
#     SECRET_KEY = 'MqI1t_qc4BwYj7Xr5Y-dJA' # or os.environ.get('SECRET_KEY')

CSRF_ENABLED = True
SECRET_KEY = 'MqI1t_qc4BwYj7Xr5Y-dJA'

# Todo : crsf WTF_CSRF_ENABLED = True
# email server

MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 465
MAIL_USE_TLS = False
MAIL_USE_SSL = True
MAIL_USERNAME = 'testmyfirstband@gmail.com' # or os.environ.get('MAIL_USERNAME')
MAIL_PASSWORD = 'MYfb1902;'  # or os.environ.get('MAIL_PASSWORD')

# administrator list
ADMINS = ['aurelia.gourbere@gmail.com']

