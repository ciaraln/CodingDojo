from flask import Flask, render_template,request,redirect, session

app = Flask(__name__)
app.secret_key = "Hidden"

@app.route('/')

def dojosurvey():
	return render_template('index.html')

@app.route('/dojosurvey', methods=['POST'])
def resultForm():
	session['yourfullname'] = request.form['yourfullname']
	session['DojoLocation'] = request.form['DojoLocation']
	session['FavoriteLanguage'] = request.form['FavoriteLanguage']
	session['comment'] = request.form['comment']
	return render_template('dojosurvey.html')

app.run(debug=True)