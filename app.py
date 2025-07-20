from flask import Flask, render_template, redirect, url_for, request
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, DateField, FileField, SubmitField, URLField
from wtforms.validators import DataRequired, Optional
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dev'
app.config['UPLOAD_FOLDER'] = 'static/images/'

# In-memory data storage
profile = {
    'name': 'LevelUpMe',
    'photo': 'https://images.unsplash.com/photo-1584697964273-6fbfba8d7b61?ixlib=rb-4.0.3&auto=format&fit=crop&w=1350&q=80',
    'bio': 'A passionate student eager to learn and grow.'
}
projects = []
events = []
certificates = []
achievements = []

# Forms
class ProjectForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    link = URLField('Project Link or Image URL', validators=[Optional()])
    submit = SubmitField('Add Project')

class EventForm(FlaskForm):
    name = StringField('Event Name', validators=[DataRequired()])
    role = StringField('Role', validators=[DataRequired()])
    date = DateField('Date', validators=[DataRequired()])
    submit = SubmitField('Add Event')

class CertificateForm(FlaskForm):
    title = StringField('Certificate Title', validators=[DataRequired()])
    date = DateField('Date', validators=[DataRequired()])
    image = FileField('Upload Image or Provide Link', validators=[Optional()])
    link = URLField('Certificate Link', validators=[Optional()])
    submit = SubmitField('Add Certificate')

class AchievementForm(FlaskForm):
    description = TextAreaField('Description', validators=[DataRequired()])
    date = DateField('Date', validators=[DataRequired()])
    submit = SubmitField('Add Achievement')

# Routes
@app.route('/')
def index():
    return render_template('index.html', profile=profile, projects=projects, events=events, certificates=certificates, achievements=achievements)

@app.route('/profile')
def profile_page():
    return render_template('profile.html', profile=profile)

@app.route('/add_project', methods=['GET', 'POST'])
def add_project():
    form = ProjectForm()
    if form.validate_on_submit():
        projects.append({
            'title': form.title.data,
            'description': form.description.data,
            'link': form.link.data
        })
        return redirect(url_for('index'))
    return render_template('add_project.html', form=form)

@app.route('/add_event', methods=['GET', 'POST'])
def add_event():
    form = EventForm()
    if form.validate_on_submit():
        events.append({
            'name': form.name.data,
            'role': form.role.data,
            'date': form.date.data
        })
        return redirect(url_for('index'))
    return render_template('add_event.html', form=form)

@app.route('/add_certificate', methods=['GET', 'POST'])
def add_certificate():
    form = CertificateForm()
    if form.validate_on_submit():
        filename = None
        if form.image.data:
            file = form.image.data
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        certificates.append({
            'title': form.title.data,
            'date': form.date.data,
            'image': filename,
            'link': form.link.data
        })
        return redirect(url_for('index'))
    return render_template('add_certificate.html', form=form)

@app.route('/add_achievement', methods=['GET', 'POST'])
def add_achievement():
    form = AchievementForm()
    if form.validate_on_submit():
        achievements.append({
            'description': form.description.data,
            'date': form.date.data
        })
        return redirect(url_for('index'))
    return render_template('add_achievement.html', form=form)

@app.route('/export')
def export():
    return render_template('export.html', profile=profile, projects=projects, events=events, certificates=certificates, achievements=achievements)

if __name__ == '__main__':
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])
    app.run(debug=True) 