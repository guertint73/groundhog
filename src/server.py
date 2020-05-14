from flask import Flask, Response
import json

'''Flask Setup'''
app = Flask(__name__)


@app.route('/')
def hello_world():
    msg = {'msg': 'Hello Jared'}
    response = Response(response=json.dumps(msg),
                        status=200,
                        mimetype='application/json')
    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0')