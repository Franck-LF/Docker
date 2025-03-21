# ---------------------------------
# API for exercise 3
#
#



import flask
from flask import request, jsonify, render_template
import mysql.connector
import json
from typing import List, Dict

app = flask.Flask(__name__)
app.config["DEBUG"] = True



def persons() -> List[Dict]:
    config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'persons'
    }
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM persons')
    results = [{firstname: lastname} for (firstname, lastname) in cursor]
    cursor.close()
    connection.close()
    return results


@app.route('/', methods=['GET'])
def index() -> str:
    return json.dumps({'persons': persons()})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)