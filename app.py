from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route("/", methods=['POST'])
def user_register():
    return request.json


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=6543)
