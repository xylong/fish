import config

SECRET_KEY = config.os.environ.get('SECRET_KEY')

DEBUG = config.os.environ.get('DEBUG')

PRE_PAGE = config.os.environ.get('PRE_PAGE')
