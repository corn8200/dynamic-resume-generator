from flask import Flask, render_template

# Create a Flask web server application
app = Flask(__name__)

@app.route('/')
def index():
    """
    A main index page to navigate to your other pages.
    """
    return """
    <h1>Navigation</h1>
    <ul>
        <li><a href="/report">View Trip Report</a></li>
        <li><a href="/resume">View Resume</a></li>
    </ul>
    """

@app.route('/report')
def report():
    """Serves the report.html page from the templates folder."""
    return render_template('report.html')

@app.route('/resume')
def resume():
    """Serves the resume_builder.html page from the templates folder."""
    return render_template('resume_builder.html')

if __name__ == '__main__':
    # Runs the app in debug mode, which automatically reloads
    # when you save changes to your files.
    app.run(debug=True)