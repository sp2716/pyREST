from flask import Flask, jsonify, request, send_file
from random import randrange
import io

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST', 'DELETE'])
def user():
    if request.method == 'GET':
        return 'engineer'
    if request.method == 'POST':
        data = request.form  # a multidict containing POST data
        return jsonify(isError=False,
                       message="Success",
                       statusCode=200,
                       data=data), 200

@app.route('/favicon.ico', methods=['GET'])
def favicon():
    if request.method == 'GET':
        filename = 'favicon.ico'
        return send_file(filename, mimetype='image/jpg')

@app.route('/form', methods=['GET', 'POST', 'DELETE'])
def form():
	if request.method == 'GET':
		return 'form goes here...'

# driver function
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
