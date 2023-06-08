# Using flask to make an api
# import necessary libraries and functions
from flask import Flask, jsonify, request, send_file
from random import randrange
import io

# creating a Flask app
app = Flask(__name__)


# on the terminal type: curl http://127.0.0.curl :5001/
# returns hello world when we use GET.
# returns the data that we send when we use POST.
@app.route('/', methods=['GET', 'POST', 'DELETE'])
def user():
    if request.method == 'GET':
        return 'engineer'
    if request.method == 'POST':
        """modify/update the information for <user_id>"""
        # you can use <user_id>, which is a str but could
        # changed to be int or whatever you want, along
        # with your lxml knowledge to make the required
        # changes
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
