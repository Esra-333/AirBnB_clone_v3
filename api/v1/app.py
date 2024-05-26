#!/usr/bin/python3
"""
API for AirBnB_clone_v3
"""
from flask import Flask
import os
from models import storage
from api.v1.views import app_views

app = Flask(__name__)

# Register the blueprint app_views to the Flask instance app
app.register_blueprint(app_views)

# Declare a method to handle @app.teardown_appcontext that calls storage.close()
@app.teardown_appcontext
def teardown_db(exception):
    storage.close()

if __name__ == "__main__":
    host = os.getenv('HBNB_API_HOST', '0.0.0.0')
    port = int(os.getenv('HBNB_API_PORT', 5000))
    app.run(host=host, port=port, threaded=True)

