# Student Portfolio

A Flask web app for students to store and showcase their projects, event participation, certificates, and achievements.

## Features
- Home page with student's name, photo, and bio
- Sections for Projects, Events, Certificates, and Achievements
- Add entries via simple forms
- Responsive Bootstrap design
- Temporary data storage in Python dictionaries
- Export profile as a public (read-only) page

## Setup Instructions

1. **Clone the repository**
   ```bash
   git clone <repo-url>
   cd student_portfolio
   ```

2. **Create a virtual environment (optional but recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the app**
   ```bash
   flask run
   ```
   The app will be available at [http://127.0.0.1:5000](http://127.0.0.1:5000)

## Folder Structure
```
student_portfolio/
├── app.py
├── templates/
│   ├── index.html
│   ├── profile.html
│   ├── add_project.html
│   └── ...
├── static/
│   ├── css/
│   └── images/
├── requirements.txt
└── README.md
```

## Notes
- Data is stored in memory (Python dictionaries). For persistence, extend to use SQLite or another database.
- For form handling, Flask-WTF is recommended (already included in requirements). 