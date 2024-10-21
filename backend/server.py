from flask import Flask, render_template

# Specify the path to your templates folder
app = Flask(__name__, template_folder='../frontend/', static_folder='../frontend/static/')

@app.route('/')
def index():
    """Render home page."""
    return render_template('index.html')  # Render templates as usual

if __name__ == '__main__':
    app.run(debug=True, port=2005)
