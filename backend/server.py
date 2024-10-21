from flask import Flask, render_template
import markdown

# Specify the path to your templates folder
app = Flask(__name__, template_folder='../frontend/', static_folder='../frontend/static/')

@app.route('/')
def index():
    """Render home page."""

    # Read the markdown file
    with open('../notes/main.md', 'r', encoding="utf-8") as file:
        notes_content = file.read()
    
    notes_html = markdown.markdown(notes_content, extensions=['fenced_code'])

    return render_template('index.html', notes=notes_html)  # Render templates as usual

if __name__ == '__main__':
    app.run(debug=True, port=2005)
