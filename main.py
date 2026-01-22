from flask import Flask, render_template

app = Flask(__name__)

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/ball')
def ball():
    return render_template('ball.html')

app.run(host='localhost', port=4000)
