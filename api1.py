
import flask
from flask import request, jsonify, render_template

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/hello', methods=['GET'])
def test():
    return {'status' : 'OK'}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)