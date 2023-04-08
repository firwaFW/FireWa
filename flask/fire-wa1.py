
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

@app.route('/')

def Home():
	return render_template('index.html')


@app.route('/About Course')
def About_Course():
    
	return render_template('About Course.html')

@app.route('/Python Course')
def PythonCourse():
    
	return render_template('PythonCourse.html')
 
if __name__ == '__main__':
    app.run(debug=True, port=8006)
    
if __name__ == '__main__':

	app.run(debug=True)
