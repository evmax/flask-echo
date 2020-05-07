from flask import jsonify
from flask import request

from echo.app import app


@app.route('/post', methods=['POST'])
def post():
    app.logger.info("New post request")
    app.logger.debug(request.data)
    return jsonify({'ok': 'true'}), 200


@app.route('/get', methods=['GET'])
def get():
    app.logger.info("New get request")
    app.logger.debug(request.data)
    return jsonify({'ok': 'true'}), 200
