from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Scott'}
    posts = [
        {
            'author': {'username': 'Steve C.'},
            'body': 'Part number has been entered.'
        },
        {
            'author': {'username': 'Scott'},
            'body': 'MFG/QA Complete'
        }
    ]
    return render_template('index.html', title='SAP Material Code', user=user, posts=posts)

@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me = {}'.format(form.username.data, form.remember_me.data), 'success')
        return redirect(url_for('index'))
    return render_template('login.html', title='Login', form=form)
