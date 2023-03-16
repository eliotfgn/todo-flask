from flask import Flask

app: Flask = Flask(__name__)


@app.get()
def index():
    return "Hello world"
