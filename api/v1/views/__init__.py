#!/usr/bin/python3
"""Blueprint for app_views"""
from flask import Blueprint

# Task 4 - Create Blueprint
app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

from . import *
# Task 4 - End
