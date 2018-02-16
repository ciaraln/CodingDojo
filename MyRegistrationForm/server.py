from flask import Flask, render_template, request, redirect, session, flash
from mysqlconnection import MySQLConnector
import re
import md5
emailregex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9.+_-]+\.[a-zA-Z]+$')
nameregex = re.compile(r'^[a-zA-Z]+$')
app = Flask(__name__)  
app.secret_key = 'supertopsecret'
mysql = MySQLConnector(app, 'registrationformpython')   #put the name of your mysql file in the 2nd parameter. 

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def fieldcheck():
	goto = '/'
	if request.form['formtype'] == 'register':
		if len(request.form['email']) < 1:
			flash('Email field cannot be empty.')
		elif not emailregex.match(request.form['email']):
			flash('Invalid Email address')
		elif len(request.form['first_name']) < 1:
			flash('First Name field cannot be empty.')
		elif not nameregex.match(request.form['first_name']):
			flash('First Name must be alphabetical characters only.')
		elif len(request.form['last_name']) < 1:
			flash('Last Name field cannot be empty.')
		elif not nameregex.match(request.form['last_name']):
			flash('Last Name must be alphabetical characters only.')
		elif len(request.form['password']) < 9:
			flash('Password must be more than 8 Characters!')
		elif len(request.form['passwordcheck']) < 9:
			flash('Password must be more than 8 Characters!')
		elif request.form['password'] != request.form['passwordcheck']:
			flash('Password does not match password confirmation!')
		else:
			password = md5.new(request.form['password']).hexdigest()
			first_name = request.form['first_name']
			last_name = request.form['last_name']
			email = request.form['email']
			user_query = ('INSERT INTO users (first_name, last_name, password, email, created_at, updated_at) VALUES ("{}", "{}", "{}", "{}", NOW(), NOW())'.format(first_name, last_name, password, email))
			mysql.query_db(user_query)
			return render_template('success.html')
		return redirect(goto)
	elif request.form['formtype'] == 'login':
		if len (request.form['email']) < 1:
			flash("Email field cannot be empty.")
		elif not emailregex.match(request.form['email']):
			flash('Invalid Email address')
		elif len(request.form['password']) < 1:
			flash("Password field cannot be empty.")
		else:
			email = request.form['email']
			password = md5.new(request.form['password']).hexdigest()
			db_password = mysql.query_db("SELECT password FROM users WHERE email = '{}'".format(email))
			db_email = mysql.query_db("SELECT email FROM users WHERE email = '{}'".format(email))
			if email == db_email[0]['email'] and password == db_password[0]['password']:
				return render_template('logged_in.html')
			else:
				flash('Your email and passwrd does not match. Please try again.')
		return redirect(goto)
app.run(debug=True)