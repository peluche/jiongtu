from flask import Flask, send_from_directory, redirect, jsonify
from itertools import chain

def start(images, options=None):
    if options == None: options = {}
    if 'width' not in options:
        options['width'] = max(chain.from_iterable(images), key=lambda x: x[0])[0] + 1
    if 'height' not in options:
        options['height'] = max(chain.from_iterable(images), key=lambda x: x[1])[1] + 1
    if 'port' not in options:
        options['port'] = None
    if 'zoom' not in options:
        options['zoom'] = 1

        
    app = Flask(__name__, static_url_path='')
    
    @app.route("/")
    def index():
        return redirect('/index.html')
    
    @app.route("/i")
    def image():
        return jsonify(images=images, options=options)
    
    app.run(port=options['port'])

if __name__ == '__main__':
    from random import randrange
    start([[(randrange(20), randrange(20), 0, 0, 0)] for _ in range(1000)])
