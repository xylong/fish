import config

SECRET_KEY = config.os.environ.get('SECRET_KEY')

DEBUG = config.os.environ.get('DEBUG')

PRE_PAGE = config.os.environ.get('PRE_PAGE')
BEANS_UPLOAD_ONE_BOOK=config.os.environ.get('BEANS_UPLOAD_ONE_BOOK')
