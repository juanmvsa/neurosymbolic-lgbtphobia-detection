from flask import Flask, render_template, Response, request
# define app
app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>hello world</h1>'
    # return render_template('index.html')
