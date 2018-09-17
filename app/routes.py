from app import app, db
from flask import render_template, url_for, redirect, flash, request
from app.forms import LoginForm, RegisterForm, ProfileForm, UserForm
from app.models import User, Role
from flask_login import current_user, login_user, logout_user, login_required


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', page='home')


@app.route('/who')
def who():
    return render_template('who.html', page='who')


@app.route('/what')
def what():
    return render_template('what.html', page='what')


@app.route('/news')
def news():
    return render_template('news.html', page='news')


@app.route('/where')
def where():
    return render_template('where.html', page='where')


@app.route('/contact')
def contact():
    return render_template('contact.html', page='contact')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Credentials are incorrect')
            return redirect(url_for('login'))

        # user is authenticated
        login_user(user, remember=form.remember_me.data)
        flash('You are now logged in.')
        return redirect(url_for('index'))

    return render_template('login.html', form=form, page='login')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = RegisterForm()

    if form.validate_on_submit():
        role = Role.query.filter_by(name='User').first()
        user = User(first_name=form.first_name.data, last_name=form.last_name.data,
                    company_name=form.company_name.data, bio=form.bio.data, email=form.email.data, role_id=role.id)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you have successfully registered.')
        return redirect(url_for('login'))
    return render_template('register.html', form=form, page='register')


@app.route('/profile')
@login_required
def profile():
    role = Role.query.get(current_user.role_id)

    return render_template('profile.html', role=role.name)


@app.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = ProfileForm()

    if form.validate_on_submit():
        current_user.first_name = form.first_name.data
        current_user.last_name = form.last_name.data
        current_user.bio = form.bio.data
        current_user.company_name = form.company_name.data
        db.session.commit()
        flash('Your changes have been saved.')
        return redirect(url_for('profile'))
    elif request.method == 'GET':
        form.first_name.data = current_user.first_name
        form.last_name.data = current_user.last_name
        form.bio.data = current_user.bio
        form.company_name.data = current_user.company_name

    print(form.errors)
    return render_template('edit_profile.html', form=form, page='edit_profile')


@app.route('/admin')
@login_required
def admin():
    users = User.query.all()
    role = Role.query.get(current_user.role_id)

    return render_template("admin.html", users=users, page='admin', role=role.name)


@app.route('/edit_users/<id>', methods=['GET', 'POST'])
@login_required
def edit_users(id):
    user = User.query.get(id)
    role = Role.query.get(user.role_id)

    form = UserForm(role_id=user.role_id)

    if form.validate_on_submit():
        user.first_name = form.first_name.data
        user.last_name = form.last_name.data
        user.company_name = form.company_name.data
        user.role_id = form.role_id.data
        print(form.role_id.data)
        print(form.role_id.default)
        print(form.role_id.choices)
        db.session.commit()
        flash('Your changes have been saved.')
        return redirect(url_for('admin'))
    elif request.method == 'GET':
        form.first_name.data = user.first_name
        form.last_name.data = user.last_name
        form.company_name.data = user.company_name

    return render_template("edit_user.html", form=form, page='edit_user', role=role.name)


@app.route('/logout')
def logout():
    logout_user()

    return redirect(url_for('index'))
