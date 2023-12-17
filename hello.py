from flask import Flask
import decorator_functions

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World! Hashib</p>"


print(app)
if (__name__ == "__main__"):
    app.run()
