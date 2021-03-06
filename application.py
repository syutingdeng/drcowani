"""
This script runs the anime application using a development server.
"""

from os import environ
from anime import app

if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        #PORT = int(environ.get('SERVER_PORT', '5000'))
        PORT = 5000
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)
