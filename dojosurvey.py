from flask import Flask, render_template,request,redirect, session

app = Flask(__name__)
app.secret_key = "Hidden"

@app.route('/')
def dojoSurvey():
	return render_template('index.html')

@app.route('/process', methods=['POST'])
def resultForm():
	session['formname'] = request.form['name']
	return redirect('/')

app.run(debug=True)