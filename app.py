from flask import Flask, render_template, redirect, url_for

# Create a Flask web server application
app = Flask(__name__)

# --- Resume Data ---
# Moving all resume content here makes it easy to update without touching HTML.
resume_data = {
    "name": "John Cornelius",
    "title": "Staff Technical Program Manager • Automation & Digital Operations • Process Excellence",
    "contact": {
        "location": "Harpers Ferry, WV",
        "email": "corn82@icloud.com",
        "phone": "(304) 268-4985",
        "linkedin": "https://linkedin.com/in/johncornelius",
        "github": "https://github.com/corn8200"
    },
    "summary": "Experienced technical program manager with 20+ years leading complex automation, analytics, and process improvement initiatives across manufacturing, logistics, and aviation. Proven success in deploying SCADA, Power Platform, and AI-driven tools to reduce downtime, streamline operations, and drive measurable business outcomes. Skilled in Lean Six Sigma, Agile, and cross-functional team leadership to deliver digital transformation in high-stakes, fast-moving environments. Trusted to manage multimillion-dollar programs with clarity, urgency, and results.",
    "skills": [
        "Lean Six Sigma (Bronze Belt)", "Program Management (JIRA, MS Project, Confluence)",
        "Agile / SAFe / MBSE / Risk-Based Planning", "Automation Strategy & Roadmap Execution",
        "Power Automate, Power Apps, SharePoint", "Process Optimization & Root Cause Analysis",
        "Industrial Automation & SCADA Systems", "Data Visualization (Power BI, Excel, SQL)",
        "Digital Transformation & KPI Dashboards", "Cross-Functional Stakeholder Alignment",
        "Change Management & Process Reengineering", "24/7 Operations & DuPont Scheduling",
        "Fleet, Logistics & Supply Chain Management"
    ],
    "experience": [
        {
            "title": "Technical Program Manager",
            "company": "Allmine Paving (A Tamko Company)",
            "location": "WV",
            "dates": "Jan 2022 – Present",
            "duties": [
                "Directed cross-functional technical teams for 24/7 industrial operations, including supply chain, automation systems, and plant performance analytics.",
                "Led digital infrastructure initiatives including mobile dashboarding and SCADA integration, reducing downtime by 12% and operator lag by 25%.",
                "Managed stakeholder communication across vendor, transportation, and procurement channels to ensure risk-mitigated delivery and budget adherence.",
                "Applied Lean Six Sigma and Agile principles to implement system upgrades and eliminate bottlenecks across operations and asset scheduling workflows."
            ]
        },
        {
            "title": "Technical Program Manager",
            "company": "U.S. Army (160th SOAR)",
            "location": None,
            "dates": "2009 – 2021",
            "duties": [
                "Managed full lifecycle of autonomous aviation and digital systems programs, with end-to-end delivery of advanced training and automation tools.",
                "Led 100+ personnel and oversaw $48M in assets while managing P&L-equivalent responsibilities across training, logistics, and technical operations.",
                "Modernized training and operations by digitizing workflows and implementing telemetry analytics, reducing admin lag by 40%.",
                "Implemented Agile and system modeling practices to improve pilot readiness throughput by 22% across distributed locations.",
                "Planned and coordinated logistics, equipment moves, and remote system testing for 50+ aircraft with zero safety incidents.",
                "Briefed senior stakeholders on risk, schedule, and progress metrics to drive decision-making across interagency teams."
            ]
        }
    ],
    "education": [
        {"degree": "Master of Science (M.S.), Unmanned Systems – Human Factors", "school": "Embry-Riddle Aeronautical University", "details": "4.0 GPA"},
        {"degree": "Bachelor of Science (B.S.), Aeronautics", "school": "Embry-Riddle Aeronautical University", "details": None}
    ],
    "certifications": [
        {"name": "Project Management Professional (PMP)", "issuer": "Simplilearn, Issued Aug 2021"},
        {"name": "Agile Scrum Master", "issuer": "Simplilearn, Issued Sep 2021"},
        {"name": "Risk Management Professional", "issuer": "Simplilearn, Issued Sep 2021"},
        {"name": "Customer Centric Digital Transformation", "issuer": "Simplilearn, Issued Nov 2021"},
        {"name": "Lean Six Sigma Green Belt", "issuer": "Simplilearn, Issued Oct 2021"},
        {"name": "Lean Six Sigma Bronze (Advanced Statistics)", "issuer": "Lean Methods Group, Issued Dec 2023"}
    ]
}

@app.route('/')
def index():
    """Redirects the root URL to the resume page."""
    return redirect(url_for('resume'))

@app.route('/resume')
def resume():
    """Serves the resume page with data from the Python script."""
    return render_template('resume_builder.html', resume=resume_data)

if __name__ == '__main__':
    # Runs the app in debug mode, which automatically reloads
    # when you save changes to your files.
    app.run(debug=True)
