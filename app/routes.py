from flask import render_template
from app import myapp
from app.forms import LoginForm

@myapp.route("/")
@myapp.route("/index")
def  index():
	user={'name':'mohammad'}
	return render_template('index.html',user=user)


@myapp.route('/login',  methods=['GET', 'POST'])
def login():
	form=LoginForm()
	return render_template('login.html',form=form)
