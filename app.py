from flask import Flask , render_template, request, redirect # type: ignore
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import or_

from datetime import datetime

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///todo.sqlite"
db = SQLAlchemy(app)

class Todo(db.Model):
    sno = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(200), nullable = False)
    desc = db.Column(db.String(1000), nullable = False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"{self.sno} - {self.title}" 



@app.route("/", methods = ['GET', "POST"])
def get_and_add_todo():
    if request.method == 'POST':
        formTitle = request.form['title']
        FormDesc = request.form['desc']

        todo = Todo(title=formTitle, desc=FormDesc)
        db.session.add(todo)
        db.session.commit()

    allTodo = Todo.query.all()
    return render_template('index.html',allTodo=allTodo)
    

@app.route("/about",)
def about():
    
    return render_template('about.html')


@app.route("/search", methods = ['GET', "POST"])
def serach_todo():
    if request.method == 'POST':
        search_query = request.form['search']
        print(search_query)
       
        allTodo = db.session.query(Todo).filter(
                    or_(
                        Todo.title.like(f"%{search_query}%"),
                        Todo.desc.like(f"%{search_query}%")
                    )
                ).all()
        
        return render_template('search.html',allTodo=allTodo)
        
    allTodo = Todo.query.all()
    return render_template('search.html',allTodo=allTodo)
    

@app.route("/update/<int:sno>", methods = ['GET', 'POST'])
def update(sno):
    if request.method == 'POST':
        formTitle = request.form['title']
        FormDesc = request.form['desc']

        todoUpdate = Todo.query.filter_by(sno = sno).first()
        todoUpdate.title = formTitle
        todoUpdate.desc = FormDesc
        db.session.add(todoUpdate)
        db.session.commit()
        return redirect('/')

    todoUpdate = Todo.query.filter_by(sno = sno).first()
    return render_template('update.html',todoUpdate=todoUpdate)


@app.route("/delete/<int:sno>")
def delete(sno):
    todoDelete = Todo.query.filter_by(sno = sno).first()
    db.session.delete(todoDelete)
    db.session.commit()
    return redirect('/')

@app.template_filter('format_datetime')
def format_datetime(value, format='%Y-%m-%d %H:%M:%S'):
    if isinstance(value, str):
        value = datetime.fromisoformat(value)
    return value.strftime(format)


if __name__ == "__main__":
    app.run(host='192.168.195.65', port=5000, debug = True)