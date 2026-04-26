from flask import Flask, render_template, redirect, abort, request
from flask_login import LoginManager, logout_user, login_required
from data import db_session
from data.users import User
from data.jobs import Jobs
from data.category import Category, jobs_to_category_table
from data.department import Department
from form.loginform import LoginForm
from flask_login import login_user, current_user
from form.user import RegisterForm
from form.newjobsform import JobsForm
from form.departamentform import DepartamentForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.get(User, user_id)


@app.route("/")
def index():
    if current_user.is_authenticated:
        db_sess = db_session.create_session()
        jobs = db_sess.query(Jobs).all()
    else:
        jobs = []
    return render_template('index.html', jobs=jobs)


@app.route("/departament_main")
def departament_main():
    if current_user.is_authenticated:
        db_sess = db_session.create_session()
        departaments = db_sess.query(Department).all()
    else:
        departaments = []
    return render_template('index2.html', departaments=departaments)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/register', methods=['GET', 'POST'])
def reqister():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Пароли не совпадают")
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Такой пользователь уже есть")
        user = User(
            name=form.name.data,
            surname=form.surname.data,
            email=form.email.data,
            age=form.age.data,
            position=form.position.data,
            speciality=form.speciality.data,
            address=form.address.data,
        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/')
    return render_template('register.html', title='Регистрация', form=form)


@app.route('/register_job', methods=['GET', 'POST'])
def register_job():
    if current_user.is_authenticated:
        form = JobsForm()
        db_sess = db_session.create_session()
        form.category.choices = [(c.id, c.name) for c in db_sess.query(Category).all()]
        if form.validate_on_submit():
            if db_sess.query(Jobs).filter(Jobs.job == form.job.data).first():
                return render_template('add_jobs.html', form=form, message="Такая работа уже добавлена",
                                       title="Добавление работы")
            job = Jobs(
                job=form.job.data,
                team_leader=form.team_leader.data,
                creator=current_user.id,
                work_size=form.work_size.data,
                collaborators=form.collaborators.data,
                is_finished=form.is_finished.data,
            )
            if form.category.data:
                job.categories = db_sess.query(Category).filter(Category.id.in_(form.category.data)).all()
            db_sess.add(job)
            db_sess.commit()
            return redirect('/')
        return render_template('add_jobs.html', form=form, title="Добавление работы")


@app.route('/register_departament', methods=['GET', 'POST'])
def register_departament():
    if current_user.is_authenticated:
        form = DepartamentForm()
        if form.validate_on_submit():
            db_sess = db_session.create_session()
            if db_sess.query(Department).filter(Department.title == form.title.data).first():
                return render_template('add_departament.html', form=form, message="Такой департамент уже есть",
                                       title="Добавление Департамента")
            department = Department(
                id=form.id.data,
                title=form.title.data,
                creator=current_user.id,
                chief=form.chief.data,
                members=form.members.data,
                email=form.email.data,
            )
            db_sess.add(department)
            db_sess.commit()
            return redirect('/departament_main')
        return render_template('add_departament.html', form=form, title="Добавление Департамента")


@app.route('/jobs/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_jobs(id):
    form = JobsForm()
    db_sess = db_session.create_session()
    all_category = db_sess.query(Category).all()
    form.category.choices = [(c.id, c.name) for c in all_category]
    if request.method == "GET":
        jobs = db_sess.query(Jobs).filter(Jobs.id == id, Jobs.creator == current_user.id).first()
        if jobs:
            form.job.data = jobs.job
            form.team_leader.data = jobs.team_leader
            form.work_size.data = jobs.work_size
            form.collaborators.data = jobs.collaborators
            form.category.data = [c.id for c in jobs.categories]
            form.is_finished.data = jobs.is_finished
        else:
            abort(404)
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        jobs = db_sess.query(Jobs).filter(Jobs.id == id, Jobs.creator == current_user.id).first()
        if jobs:
            jobs.job = form.job.data
            jobs.team_leader = form.team_leader.data
            jobs.work_size = form.work_size.data
            jobs.collaborators = form.collaborators.data
            jobs.categories = db_sess.query(Category).filter(Category.id.in_(form.category.data)).all()
            jobs.is_finished = form.is_finished.data
            db_sess.commit()
            return redirect('/')
        else:
            abort(404)
    return render_template('add_jobs.html',
                           title='Редактирование работы',
                           form=form
                           )


@app.route('/departament/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_departament(id):
    form = DepartamentForm()
    if request.method == "GET":
        db_sess = db_session.create_session()
        dep = db_sess.query(Department).filter(Department.id == id, Department.creator == current_user.id).first()
        if dep:
            form.id.data = dep.id
            form.title.data = dep.title
            form.chief.data = dep.chief
            form.members.data = dep.members
            form.email.data = dep.email
        else:
            abort(404)
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        dep = db_sess.query(Department).filter(Department.id == id, Department.creator == current_user.id).first()
        if dep:
            dep.id = form.id.data
            dep.title = form.title.data
            dep.chief = form.chief.data
            dep.members = form.members.data
            dep.email = form.email.data
            db_sess.commit()
            return redirect('/departament_main')
        else:
            abort(404)
    return render_template('add_departament.html',
                           title='Редактирование Департамента',
                           form=form
                           )


@app.route('/jobs_delete/<int:id>', methods=['GET', 'POST'])
@login_required
def jobs_delete(id):
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).filter(Jobs.id == id, Jobs.creator == current_user.id).first()
    if jobs:
        db_sess.delete(jobs)
        db_sess.commit()
    else:
        abort(404)
    return redirect("/")


@app.route('/departament_delete/<int:id>', methods=['GET', 'POST'])
@login_required
def departament_delete(id):
    db_sess = db_session.create_session()
    dep = db_sess.query(Department).filter(Department.id == id, Department.creator == current_user.id).first()
    if dep:
        db_sess.delete(dep)
        db_sess.commit()
    else:
        abort(404)
    return redirect("/departament_main")


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


if __name__ == "__main__":
    db_session.global_init("db/blogs.db")
    app.run(port=8080, host='127.0.0.1')
