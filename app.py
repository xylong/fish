from app import create_app

__author__ = 'xyl'

app = create_app()

if __name__ == '__main__':
    app.run(debug=app.config['DEBUG'])
