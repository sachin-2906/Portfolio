from flask import Flask, send_from_directory

app = Flask(__name__)

# Serve the main portfolio page
@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

# Serve any other file (json, images, resume, etc.)
@app.route('/<path:path>')
def static_files(path):
    return send_from_directory('.', path)

if __name__ == '__main__':
    print("✅ Portfolio running at: http://127.0.0.1:8000/")
    app.run(port=8000, debug=True)
