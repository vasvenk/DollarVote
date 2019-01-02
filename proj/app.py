from flask import Flask, render_template
import proj.utils.dbUtils as db

app = Flask(__name__)


@app.route('/home', methods=['GET'])
def home():
    return render_template('hello.html')
