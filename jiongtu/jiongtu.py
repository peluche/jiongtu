from flask import Flask, send_from_directory, redirect, jsonify
from itertools import chain

def start(images, width=None, height=None, port=None):
    if width == None: width = max(chain.from_iterable(images), key=lambda x: x[0])[0]
    if height == None: height = max(chain.from_iterable(images), key=lambda x: x[1])[1]
    app = Flask(__name__, static_url_path='')
    
    @app.route("/")
    def index():
        return redirect('/index.html')
    
    @app.route("/i")
    def image():
        return jsonify(images=images, width=width, height=height)
    
    app.run(port=port)

if __name__ == '__main__':
    from random import randrange
    start([[(randrange(20), randrange(20), 0, 0, 0)] for _ in range(1000)])
