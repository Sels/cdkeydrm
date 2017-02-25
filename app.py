import os
import sys
import psycopg2
import urlparse
import requests

from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods=['GET'])
def ok():
    return "ok", 200

@app.route('/validate', methods=['GET'])
def validate():

    urlparse.uses_netloc.append("postgres")
    url = urlparse.urlparse(os.environ["DATABASE_URL"])

    conn = psycopg2.connect(
        database=url.path[1:],
        user=url.username,
        password=url.password,
        host=url.hostname,
        port=url.port
        )
    
    cur = conn.cursor()
    cur.execute("Select 'test-test-test-test';")
    r = cur.fetchone()
    log(r)
    if request.args.get("cdkey") == r[1]:
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
