from flask import Flask, render_template


todo = Flask(__name__)


@todo.route('/')
def index():
    return render_template('index.html')


@todo.route('/about')
def about():
    return render_template('about.html')


@todo.route('/contact')
def contact():
    return render_template('contact.html')


@todo.route('/python-course')
def python_course():
    return render_template('python_course.html')


# I need host, port
if __name__ == '__main__':
    todo.run(
        host='127.0.0.1',
        port=5005,
        debug=True
    )
