from flask import render_template, flash, redirect, url_for
from app import myapp
from app.forms import LoginForm, LinkForm, SignUpForm

@myapp.route("/", methods=['GET', 'POST'])
@myapp.route("/index",  methods=['GET', 'POST'])
def  index():
	form = LinkForm()
	user = {'name':'mohammad'}
	return render_template('index.html',user=user,form=form)



@myapp.route('/login',  methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		flash('login requested for user {}, remember_me={}'.format(
			form.username.data,form.remember_me.data))
		return redirect(url_for('index'))
	return render_template('login.html',form=form)



@myapp.route('/signup',  methods=['GET', 'POST'])
def signup():
	form = SignUpForm()
	return render_template('signup.html', form=form)


