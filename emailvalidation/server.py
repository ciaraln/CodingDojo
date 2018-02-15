from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
import re 
emailregex = re.compile(r'^[a-zA-Z0-9.+-]+@[_a-zA-Z0-9.+-]+.[a-zA-Z]+$')

app = Flask(__name__)
app.secret_key = 'supertopsecretsquire'
mysql = MySQLConnector(app,'emails')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/email', methods=['POST'])
def createEmail():
	email= request.form['email']
	if not emailregex.match(email):
		flash('Not a valid email, check again!')
	if emailregex.match(email):
		checkQuery = mysql.query_db('SELECT * FROM emails WHERE email_address = "{}"'.format(email))
		if len(checkQuery) > 0:
			flash('This email already exists.')
		else:
			email_query = ('INSERT INTO emails (email_address, created_at, updated_at) VALUES ("{}", NOW(), NOW())'.format(email))
			mysql.query_db(email_query)
			query = "SELECT * FROM emails"
			emails = mysql.query_db(query)
			flash("The email_address you entered ({}) is VALID email address! Thank You!".format(email))
			return render_template('success.html', all_emails= emails)

app.run(debug=True)