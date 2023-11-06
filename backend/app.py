from flask import Flask, render_template, Response, request
# define app
app = Flask(__name__, static_url_path='',
            static_folder='../frontend/build',
            template_folder='../frontend/build')


@app.route('/')
def index():
    return render_template("index.html")
