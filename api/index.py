from . import dbHelper as db

from flask import Flask
from markupsafe import escape
from flask import render_template as rt

import json

app = Flask(__name__)

@app.route('/')
def home():
    return rt('index.html', qs=db.getData())#json.dumps(db.getData())

@app.route('/quiz')
def quiz():
    return json.dumps(db.getData())