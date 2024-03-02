from flask import Blueprint, render_template, session, flash, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from datetime import datetime

from app import db
from app.models import User

site = Blueprint('site', __name__, template_folder='templates')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=5, max=32)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=5, max=32)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')


@site.route('/')
def index():
    return render_template('index.html', current_year=datetime.now().year)

@site.route('/dashboard')
def dashboard():
    return render_template('dashboard.html', current_year=datetime.now().year)

@site.route('/logout')
def logout():
    session.pop('username', None)

    flash('You have been logged out.', category='info')
    return redirect(url_for('site.index'))

@site.route('/register', methods=('GET', 'POST'))
def register():
    reg_form = RegistrationForm()
    login_form = LoginForm()

    if reg_form.validate_on_submit():
        username = reg_form.username.data
        email = reg_form.email.data
        password = reg_form.password.data
        confirm_password = reg_form.confirm_password.data

        if len(username) < 5 or len(username) > 32:
            flash('Username must be between 5 and 32 characters.', category='danger')
        elif len(password) < 5 or len(password) > 32:
            flash('Password must be between 5 and 32 characters.', category='danger')
        elif password != confirm_password:
            flash('Passwords do not match.', category='danger')
        elif User.query.filter_by(username=username).first() is not None:
            flash('Username already taken.', category='danger')
        else:
            new_user = User(username=username, email=email, password=password)
            db.session.add(new_user)
            db.session.commit()

            session['username'] = username
            flash(f'You registered as {username}.', category='success')
            return redirect(url_for('site.dashboard'))
            
    elif login_form.validate_on_submit():
        username = login_form.username.data
        password = login_form.password.data

        user = User.query.filter_by(username=username).first()

        if user and user.password == password:
            flash(f'You logged in as {username}.', category='success')
            session['username'] = username
            return redirect(url_for('site.index'))
        else:
            flash('Incorrect username or password.', category='danger')

    return render_template('register.html', reg_form=reg_form, login_form=login_form, current_year=datetime.now().year)
