from flask import Flask , request

app = Flask(__name__)

totsubmit = 0

@app.route('/')
def index():
	return \
		'<form action="/submit" method="POST" enctype="multipart/form-data">\
			<input type="file" name="input"><br>\
			<input type="submit">\
		</form>'

@app.route('/submit',methods=["POST"])
def gaosub():
	f = request.files.get('input')
	f.save('/home/z/subfile/test')
	return 'ok'


if __name__=='__main__':
	app.run(host='0.0.0.0')
