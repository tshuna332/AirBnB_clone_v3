#!/usr/bin/python3
"""index.py to connect to API"""
from api.v1.views import app_views

@app_views.route('/stats', strict_slashes=False)
def hbnbStats():
    """hbnbStats"""
    return '{"status": "OK"}'

if __name__ == "__main__":
    pass
