# Dynamic Resume & Cover Letter Generator

This is a simple web application built with Python and Flask that serves a dynamic, modern HTML resume and cover letter. The application is designed to separate content from presentation, making it easy to update your information without touching the underlying code.

## Why I Built This

I'm a big believer that a good TPM should stay close to the code. I built this small Flask app for a few reasons:

1.  **To Keep My Skills Sharp:** It's a fun, practical way to stay current with Python, web servers, and modern front-end practices.
2.  **To Treat My Resume Like a Product:** Using Git for version control means I can track changes, experiment with formats, and always have a single source of truth.
3.  **To Solve a Personal Problem:** I wanted a resume that looked great on screen and printed perfectly to a one-page PDF every single time, without fighting with Word templates. This app does exactly that.
4.  **To Separate Content from Presentation:** All resume and cover letter content lives in a clean JSON file (`resume_data.json`), making updates simple without ever needing to touch the HTML templates.

Ultimately, this project is a small reflection of how I like to work: find a problem, and build a clean, simple solution for it.

## Features

*   **Dynamic Resume:** A modern, single-page resume generated from a simple JSON data file.
*   **Streamlined Cover Letter:** A cover letter generator that uses the same data as the resume, ensuring consistency and avoiding contradictions.
*   **Print-Optimized:** Both the resume and cover letter are optimized for printing to a single-page PDF.
*   **Easy to Customize:** Simply edit the `resume_data.json` file to update the content of your resume and cover letter.
*   **Web-Based:** The resume and cover letter are served as web pages, making them easily accessible and shareable.

## Tech Stack

- **Backend:** Python 3, Flask
- **Frontend:** HTML5, CSS3, Jinja2 Templating

## How to Run It

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/corn8200/dynamic-resume-generator.git
    ```
2.  **Navigate to the project directory:**
    ```bash
    cd report
    ```
3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Run the Flask application:**
    ```bash
    python app.py
    ```
5.  **Open your browser to the following URLs:**
    *   **Resume:** `http://127.0.0.1:5000/resume`
    *   **Cover Letter:** `http://127.0.0.1:5000/cover-letter`

## Project Structure

```
.
├── app.py                  # The main Flask application
├── resume_data.json        # Your resume and cover letter data
├── requirements.txt        # Python dependencies
├── static/                 # CSS, images, and other static assets
│   ├── resume_style.css
│   └── ...
└── templates/              # HTML templates
    ├── resume_builder.html
    ├── cover_letter_builder.html
    └── navigation.html
```