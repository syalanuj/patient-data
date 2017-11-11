from flask import render_template, send_file
from patient_data import app


@app.route('/', methods=['GET'])
def index():
    """
    Serves initial page of the application.
    :return: HTML rendered template of home page
    """

    return send_file('client/dist/index.html')