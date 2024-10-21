from flask import Flask, send_from_directory
import os

app = Flask(__name__)

# Define the path to the frontend directory
FRONTEND_PATH = os.path.join(os.path.dirname(__file__), '../frontend')

@app.route('/')
def serve_index():
    # Serve the index.html from the frontend directory
    return send_from_directory(FRONTEND_PATH, 'index.html')

if __name__ == '__main__':

#   manā datorā default ports 5000 bija aizņemts ar citu lapu
    app.run(debug=True, port=2005)
