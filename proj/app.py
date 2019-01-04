from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')


@app.route('/home', methods=['GET'])
def home():
    return render_template('hello.html')
