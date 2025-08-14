from flask import Flask, render_template, redirect, url_for, g, render_template_string
import json
import datetime

# Create a Flask web server application
app = Flask(__name__)

# --- Resume Data ---
# The resume data is now loaded within the resume() function to ensure
# the latest version is served on each request.

@app.before_request
def before_request():
    """Load resume data before each request."""
    with open('resume_data.json', 'r', encoding='utf-8') as f:
        g.resume_data = json.load(f)

@app.route('/')
def index():
    """Redirects the root URL to the resume page."""
    return redirect(url_for('resume'))

@app.route('/resume')
def resume():
    """Serves the resume page with data from the Python script."""
    return render_template('resume_builder.html', resume=g.resume_data)

@app.route('/cover-letter')
def cover_letter():
    """Serves the cover letter page with data from the JSON file."""
    current_date = datetime.datetime.now().strftime("%B %d, %Y")
    
    # Render the cover letter body paragraphs
    rendered_body = [render_template_string(p, resume=g.resume_data, cover_letter=g.resume_data['cover_letter']) for p in g.resume_data['cover_letter']['body']]
    
    return render_template('cover_letter_builder.html', resume=g.resume_data, cover_letter=g.resume_data['cover_letter'], date=current_date, rendered_body=rendered_body)

if __name__ == '__main__':
    # Runs the app in debug mode, which automatically reloads
    # when you save changes to your files.
    app.run(debug=True)