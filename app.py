import os
import sys
import json

import requests
from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods=['GET'])
def ok():
    return "ok", 200

@app.route('/validate', methods=['GET'])
def validate(cdkey):
    if request.args.get("cdkey") == "test-test-test-test":
        return "ok",200
    return "Im a teapot", 418


@app.route('/', methods=['POST'])
def foo():
    return 200

def log(msg):
    print str(msg)
    sys.stdout.flush()


if __name__ == '__main__':
    app.run(debug=True)
