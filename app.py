from flask import Flask
from flask import render_template, redirect


app = Flask(__name__)


@app.route('/')
def index():  
    return redirect('resume')


@app.route('/resume')
def resume():
    return render_template('resume.html')


@app.route('/links')
def links():
    return render_template('links.html')


if __name__ == '__main__':
    app.run(debug=True)