import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__, static_folder='static')

userinfo = {'name': 'Alan Turing',
    'shortIntro': 'Aspiring Skynet Developer and Professional Programmer',
    'longIntro': 'Alan Turing is from Kansas City, Missouri. He obtained his PhD at Yale. He currently works as a Software Developer. He is a driven individual who plans to one day work as a for his dream company: "Epic Games", and work on his favorite game, "Fortnite"'
 }
@app.route('/')
def index():
    return render_template('index.html', title="MLH Fellow", url=os.getenv("URL"), name=userinfo['name'],
    shortIntro=userinfo['shortIntro'], longIntro = userinfo['longIntro'])
