
from flask import Flask, request, render_template, redirect, url_for, session
from FlaskRoom import *

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def paintapp():
	if request.method == 'POST':
		w = request.form['width']
		d = request.form['depth']
		h = request.form['height']
		room = FlaskRooms(float(w),float(d),float(h))
		return render_template("my-form-outputer.html", room=room)
	else:
		return render_template("my-form-inputer.html")

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=80) 