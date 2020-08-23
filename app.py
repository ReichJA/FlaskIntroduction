from flask import Flask, render_template, url_for, request, redirect

from date_func import calc_datetime_difference, date_format, date_to_string

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

from database_setup import Base, Project_Work, Projects, Working_Type

import datetime

app = Flask(__name__)

# Connect to Database and create database session
engine = create_engine('sqlite:///time-clock2.db')

session_factory =scoped_session(sessionmaker(autocommit=False, bind=engine))
Session = scoped_session(session_factory)

db = Session()

@app.route('/', methods=['GET', 'POST'])
def index():
    db.query('project_work')
    print(db)

    if request.method == 'POST':

        project = request.form['project']
        content = request.form['content']
        
        start = datetime.datetime.strptime(request.form['date_start'], date_format())
        end = datetime.datetime.strptime(request.form['date_end'], date_format())

        diff = calc_datetime_difference(start, end)
        # date0 = date_to_string(start)
        # date1 = date_to_string(end)

        new_task = Project_Work(project=project, content=content, date_start = request.form['date_start'], \
            date_end = request.form['date_end'], time = diff)

        try:
            db.add(new_task)
            db.commit()
            db.remove()

            return redirect('/')

        except:
            return 'There was an issue adding your task'
     
    else:

        tasks = db.query(Project_Work).all()
        return render_template("index.html", tasks=tasks)
    


@app.route('/form')
def form():

    print(db)
    projects = db.query('projects')
    working_types = db.query('working_type')

    return render_template('form.html', projects = projects, working_types = working_types)


@app.route('/delete/<int:id>')
def delete(id):
    print(db)

    task_to_delete = db.query(Project_Work).filter_by(id=id).first()
    try:
        db.delete(task_to_delete)
        db.commit()
        db.remove()

        return redirect('/')
    except:
        return 'There was a problem deleting that task'

#Following function updates existings entries in the database by using the entry-id.

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    
    projects = db.query('Projects').all()
    working_types = db.query(Working_Type).all()
    
    task = db.query(Project_Work).filter_by(id=id).first()

    if request.method == 'POST':
        project = request.form['project']
        content = request.form['content']

        db.update(Project_Work).where(id=id).\
            value(project=project, content=content)

        db.commit()
        
        return redirect('/')

    else:
        return render_template('update.html', task=task, projects = projects, working_types = working_types)


if __name__ == "__main__":
    app.run(debug=True)
