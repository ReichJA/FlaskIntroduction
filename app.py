from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
import datetime 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///time-clock.db'
db = SQLAlchemy(app)

class Project_Work(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    project = db.Column(db.String(200), unique=False, nullable=False)   #Project ID
    content = db.Column(db.String(200), unique=False, nullable=False)   #what have I been working on?
    date_start = db.Column(db.DateTime, unique=False, nullable=False)   #when did I start my work?
    date_end = db.Column(db.DateTime, unique=False, nullable=False)     #when did I finish my work?
    time = db.Column(db.Float, unique=False, nullable=False)            #how long did it take?

    def __repr__(self):
        return '<Task %r>' % self.id

class Time_Clock(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    date = db.Column(db.Date, unique=False, nullable=False)
    working_type = db.Column(db.Integer, unique=False, nullable=False)
    
    time_diff = db.Column(db.Float, unique=False, nullable=False)
    overtime = db.Column(db.Float, unique=False, nullable=False)

    def __repr__(self):
        return '<id %r>' % self.id

@app.route('/')
def index():
    tasks = Project_Work.query
    return render_template('index.html', tasks=tasks)


@app.route('/form', methods=['POST', 'GET'])
def form():
    if request.method == 'POST':
        project = request.form['project']
        content = request.form['content']

        start = datetime.datetime.strptime(request.form['date_start'], '%Y-%m-%d %H:%M:%S')
        end = datetime.datetime.strptime(request.form['date_end'], '%Y-%m-%d %H:%M:%S')

        new_task = Project_Work(project=project, content=content, date_start = start, date_end = end, time = 8)

        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue adding your task'

    else:
        tasks = Project_Work.query
        return render_template('form.html', tasks=tasks)

    tasks = Project_Work.query
    return render_template('form.html', tasks=tasks)


@app.route('/delete/<int:id>')
def delete(id):
    task_to_delete = Project_Work.query.get_or_404(id)

    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return 'There was a problem deleting that task'

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    task = Project_Work.query.get_or_404(id)

    if request.method == 'POST':
        task.content = request.form['content']

        try:
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue updating your task'

    else:
        return render_template('update.html', task=task)


if __name__ == "__main__":
    app.run(debug=True)
