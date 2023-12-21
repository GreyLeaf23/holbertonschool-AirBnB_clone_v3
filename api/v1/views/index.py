#!/usr/bin/python3
"""Index view for api.v1.views"""
from api.v1.views import app_views
from flask import jsonify


# Task 4 - Create a route that returns a JSON
@app_views.route('/status', strict_slashes=False)
def status():
    """Return status"""
    return jsonify({"status": "OK"})
# Task 4 - End
