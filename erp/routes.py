
from flask import render_template, redirect, request, session, url_for
from erp import app, db, bcrypt
from erp.models import User
from flask_login import login_user, current_user, logout_user, login_required


@app.before_request
def make_session_permanent():
    session.permanent = False

@app.route('/', methods = ['GET', 'POST'])
@app.route('/home', methods = ['GET', 'POST'])
def home():
	if request.method == 'POST':
		uname = request.form.get('uname')
		psw = request.form.get('psw')
		remember = request.form.get('remember')
		if remember == 'on':
			remember = True
		print('\n\n\n\n\n',remember,'\n\n\n\n\n')
		hashed_password = bcrypt.generate_password_hash(psw).decode('utf-8')
		user = User(password=hashed_password, username =uname)
		db.session.add(user)
		db.session.commit()
		login_user(user, remember = remember)
		return redirect(url_for('student'))

	else:
		return render_template('home.html',title='Home')

@app.route('/student')
@login_required
def student():
	return render_template('student.html')


@app.route('/attendance')
@login_required
def attendance():
	return render_template('attendance.html')

@app.route('/marks')
@login_required
def marks():
	return render_template('marks.html')


@app.route('/subjects')
@login_required
def subjects():
	return render_template('subjects.html')


@app.route('/fees')
@login_required
def fees():
	return render_template('fees.html')


@app.route('/circular')
@login_required
def circular():
	return render_template('circular.html')
