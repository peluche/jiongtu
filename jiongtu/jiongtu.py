from flask import Flask, send_from_directory, redirect, jsonify

def start(images):
    app = Flask(__name__, static_url_path='')
    
    @app.route("/")
    def index():
        return redirect('/index.html')
    
    @app.route('/<path:path>')
    def send_js(path):
        return send_from_directory('static', path)
    
    @app.route("/i")
    def image():
        return jsonify(images=images)
    
    app.run(debug=True)

if __name__ == '__main__':
    from random import randrange
    start([[(randrange(100), randrange(100), 0, 0, 0)] for _ in range(1000)])
