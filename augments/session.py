from flask import Flask , session
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)

tot = 0

@app.route('/set')
def defau():
	global tot
	tot += 1
	session['usn'] = str(tot)
	return 'setted'

@app.route('/cat')
def see():
	return session.get('usn')

@app.route('/del')
def delet():
	session.clear()
	return 'cleared'

if __name__=='__main__':
	app.run(host='0.0.0.0')
