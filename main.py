from flask import Flask , request

app = Flask(__name__)

totsubmit = 0

@app.route('/')
def index():
	return \
		'<form action="/submit" method="POST">\
			code<br>\
			<textarea name="code" rows="15" cols="80"></textarea><br>\
			datain<br>\
			<textarea name="datain" rows="10" cols="80"></textarea><br>\
			<button>submit</button>\
		</form>'

@app.route('/submit',methods=["POST"])
def gaosub():
	rq = request
	global totsubmit
	totsubmit+=1
	
	idcpp = str(totsubmit) + ".cpp"
	fcpp = open(idcpp,mode="w")
	fcpp.write(rq.form.get("code"))
	
	idin = str(totsubmit) + ".in"
	fin = open(idin,mode="w")
	fin.write(rq.form.get("datain"))
	
	idans = str(totsubmit) + ".ans"
	fans = open(idans,mode="w")
	fans.write('take your time<br>(plz wait & refresh)')
	
	print(rq.method)
	print(rq.form.get("code"))
	return "<a href='/result/" + str(totsubmit) + "'>watch result</a><br>\
		<a href='/'>back</a>"

@app.route('/result/<resid>')
def gaores(resid):
	
	idans = str(resid) + ".ans"
	fans = open(idans,mode="r")
	ans = fans.read()
	
	return "<pre>" + ans + "</pre>" + "<br><br>\
		<a href='/'>back</a>"


if __name__=='__main__':
	app.run(host='0.0.0.0')
