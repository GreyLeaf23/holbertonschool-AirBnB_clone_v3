#!/usr/bin/python3
"""Starts a Flask web application"""
from flask import Flask
from models import storage
from api.v1.views import app_views
import os

# Task 4 - Create an instance of Flask
app = Flask(__name__)
app.register_blueprint(app_views)  # Register Blueprint with Flask app


@app.teardown_appcontext
def teardown_db(exception):
    """Closes the database again at the end of the request."""
    storage.close()


if __name__ == "__main__":
    host = os.getenv('HBNB_API_HOST', '0.0.0.0')
    port = os.getenv('HBNB_API_PORT', '5000')
    app.run(host=host, port=port, threaded=True)
# Task 4 - End
