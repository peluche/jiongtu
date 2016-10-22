from flask import Flask, send_from_directory, redirect, jsonify

app = Flask(__name__, static_url_path='')
images = [[[5, 5, 0, 0, 0]], [[5, 5, 255, 255, 0]]]

@app.route("/")
def index():
    return redirect('/index.html')

@app.route('/<path:path>')
def send_js(path):
    return send_from_directory('static', path)

@app.route("/i")
def image():
    return jsonify(images=images)

def add_image(pixels):
    images.append(pixels)

def start():
    app.run(debug=True)

if __name__ == '__main__':
    start()
    
