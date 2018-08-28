from flask import Flask

__author__ = 'xyl'

app = Flask(__name__)
app.config.from_object('config.app')

# from app.web import book

if __name__ == '__main__':
    app.run(debug=app.config['DEBUG'])
