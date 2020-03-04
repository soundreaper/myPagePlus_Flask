from flask import Flask, render_template, url_for, request
import requests

app = Flask(__name__)

key = "ad958ab12b22f3901be8a6cdb93beec3"
okey = "pk.eyJ1Ijoib21hcnNzNjIiLCJhIjoiY2s3YXJsdGh4MG13ODNlcXJhY3l1NnMybiJ9.xmKZ0Yt2_b8evLDsrQcTqQ"


@app.route('/')
def index():
    """Index page of the application"""
    return render_template('index.html')

@app.route('/login')
def login():
    """Page for logging in"""
    return render_template('login.html')

@app.route('/register')
def register():
    """Page for registering"""
    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)