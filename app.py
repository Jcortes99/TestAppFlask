from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:intecol.123@localhost/students'

db=SQLAlchemy(app)

class Student(db.Model):
    __tablename__='students'
    id=db.Column(db.Integer, primary_key=True)
    fname=db.Column(db.String(200))
    lname=db.Column(db.String(200))
    pet=db.Column(db.String(200))

    def __init__(self, fname, lname, pet):
        self.fname=fname
        self.lname=lname
        self.pet=pet

class Professor(db.Model):
    __tablename__='professors'
    id=db.Column(db.Integer, primary_key=True)
    fname=db.Column(db.String(200))
    lname=db.Column(db.String(200))
    assigment=db.Column(db.String(200))


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['GET','POST'])
def submit():
    if request.method == 'POST':
        fname= request.form['fname']
        lname= request.form['lname']
        pet=request.form['pets']

        student=Student(fname,lname,pet)
        db.session.add(student)
        db.session.commit()

        studentResult=db.session.query(Student).filter(Student.id==1)

        for result in studentResult:
            print(result.fname)
    return render_template('success.html', data=fname)

ctx = app.app_context()
ctx.push()
if __name__=='__main__':
    app.run(debug=True)