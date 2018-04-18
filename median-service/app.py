#!flask/bin/python
from flask import Flask, jsonify, request, abort, make_response
import datetime
from helpers import median
from flask_httpauth import HTTPBasicAuth

__author__ = "Abhimanyu Nagurkar"
__copyright__ = "Copyright (C) Nginx Inc. All rights reserved."
__license__ = ""
__maintainer__ = "Abhimanyu Nagurkar"
__email__ = "abhimanyu.nagurkar@nginx.com"

app = Flask(__name__, static_url_path = "")


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify( { 'error': 'Not found' } ), 404)

# TODO maintaining the list in memory, can be extended to a database
list=[]


"""Accepts integer through data as params and stores in the list with time stamp"""

@app.route('/app/api/v1.0/put', methods=['POST'])
def put():
    if not request.json or not 'param' in request.json:
        return jsonify({'message': 'input expected'}), 400
    value = request.json['param']
    if not isinstance(value, (int, long)):
        return jsonify({'message': 'integer input expected'}), 400
    v = {
        'value': request.json['param'],
        'timestamp': datetime.datetime.now(),
    }
    list.append(v)
    return jsonify({'value': value}), 201


"""Calculates median of all the values added on last minute"""

@app.route('/app/api/v1.0/median', methods=['GET'])
def get_median():
    filtered = filter(lambda x: (datetime.datetime.now() - x['timestamp']).total_seconds() / 60 < 1, list)
    values = [o['value'] for o in filtered]
    return jsonify({'median': median(values)}), 201


if __name__ == '__main__':
    app.run(debug=True)
