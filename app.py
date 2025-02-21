from flask import Flask


todo = Flask(__name__)


@todo.route('/')
def index():
    return "welcome to home page"


@todo.route('/about')
def about():
    return "Hello about page"


@todo.route('/contact')
def contact():
    return "Hello contact page"


@todo.route('/python-course')
def python_course():
    return "Hello python course page"


# I need host, port
if __name__ == '__main__':
    todo.run(
        host='127.0.0.1',
        port=5005,
        debug=True
    )
