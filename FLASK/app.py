from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/Index')
def index():
    return '<h1>FLASK REST API </h1>'

@app.route('/about')
def about():
    return '<h2>LEARN QUICK</h2>'

@app.route('/contact')
def contact():
    return '<h3>CONTACT US</h3>'


@app.route('/users/<name>')
def users(name):
    return '<h3> HELLO {}</h3>'.format(name) 


if __name__ == '__main__':
    app.run(debug=True)
