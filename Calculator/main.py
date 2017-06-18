from flask import Flask, render_template, url_for, redirect, request
from werkzeug.utils import secure_filename
import os
import psycopg2

app = Flask(__name__)


@app.route('/')
def index():
    '''
    It shows the calculator.
    '''
    return render_template('calculator.html')

def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()