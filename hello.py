from flask import Flask
import decorator_functions

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World! Hashib</p>"


@app.route("/<name>")
def say_hello(name):
    return f"<h1>Hello, {name}</h1>"


print(app)
if (__name__ == "__main__"):
    app.run(debug=True)
