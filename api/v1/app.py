#!/usr/bin/python3
"""the main entrance to the api"""

from flask import Flask, jsonify
from models import storage
from api.v1.views import app_views
from os import getenv


app = Flask(__name__)
app.register_blueprint(app_views)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True


@app.teardown_appcontext
def teardown_db(execption):
    """Closes the database"""
    storage.close()


if __name__ == "__main__":
    app.run(
        host=getenv('HBNB_API_HOST', '0.0.0.0'),
        port=int(getenv('HBNB_API_PORT', '5000')),
        threaded=True
    )