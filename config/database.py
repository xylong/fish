from app.lib.helper import env

SQLALCHEMY_DATABASE_URI = 'mysql+cymysql://root:{root}@localhost:{port}/{dbname}'.format(root=env('DB_USERNAME'),
                                                                                         port=env('DB_PORT'),
                                                                                         dbname=env('DB_DATABASE'))
