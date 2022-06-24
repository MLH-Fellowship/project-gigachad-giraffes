from flask import Flask, redirect, render_template, request, flash
from flask_gravatar import Gravatar
from dotenv import load_dotenv
from playhouse.shortcuts import model_to_dict
from peewee import *
import datetime
import os
import requests



load_dotenv()

app = Flask(__name__, static_folder='static')

mydb = MySQLDatabase(os.getenv("MYSQL_DATABASE"), 
    user=os.getenv("MYSQL_USER"), 
    password = os.getenv("MYSQL_PASSWORD"),
    host = os.getenv("MYSQL_HOST"),
    port = 3306 )

class TimelinePost(Model):
    name = CharField()
    email = CharField()
    content = TextField()
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = mydb

mydb.connect()
mydb.create_tables([TimelinePost])

gravatar = Gravatar(app,
                    size=900,
                    rating='g',
                    default='retro',
                    force_default=False,
                    force_lower=False,
                    use_ssl=False,
                    base_url=None)


userinfo = {'name': 'Tanzir Hasan',
    'shortIntro': 'Aspiring Software Developer and Cryptography Enthusiast',
    'longIntro': ['''I\'m Tanzir! I\'m currently going to NYU and getting my degree in Computer Science with a minor in Mathematics. I like learning about how math is applied to computer science and I\'m particularly interested in computer graphics and physics simulations.
    I have worked in multiple aspects of software engineering from backend systems to mobile applications to implementing algorithms.''', 
    '''\nI program a lot on my own and I really enjoy it, I'm currently working on a audio equalizer in C++. My favorite programming languages are Python and C++, but Haskell and Kotlin are a close second.
     I am currently an MLH Fellow and interning at Boeing. My biggest professional goal is to create a self contained homomorphic system''',
    '''\n\nAside from programming, I have a crippling addiction to books, particularly Fantasy. I go through books very quickly and I'm currently reading a 
    book called The Poppy War, you should check it out! Aside from that I read books on programming from time to time, I'm currently reading through Automota and Computability by Dexter C. Kozen on a recommendation from my math addicted friend.'''],
    'work': [{'jobTitle': 'Software Engineer @ MLH', 'desc': "I created the backend of the LMS", "year": "1999", 'link':'./static/img/logo.jpg'},
        {'jobTitle': 'Software Engineer @ Meta', 'desc': "I created facebook mobile application", "year": "2004-2022", 'link':'./static/img/logo.jpg'}],
    'skills': ['./static/img/skillicons/c-.png','./static/img/skillicons/css-3.png', './static/img/skillicons/html-5.png',
    './static/img/skillicons/js.png','./static/img/skillicons/python.png'],
    'education': [{'type': 'PhD of Computer Science', 'from': 'Columbia University', 'when': '1984-1989', 'desc': 'I studied stuff', 'link': './static/img/logo.jpg'}],
    'email': '123fakemail@gmail.com',
    'hobbies':  [{'name': 'Basketball', 'caption': 'My Favorite Sport!', 'img': './static/img/hobbies_gallery/basketball.jpeg', 'active': 'active'},
     {'name': 'Fishing', 'caption': 'My favorite way to relax!', 'img': './static/img/hobbies_gallery/fishing.jpg', 'active': ''}, 
    {'name': 'Paddleboarding', 'caption': 'My favorite watersport!', 'img': './static/img/hobbies_gallery/paddleboarding.jpg', 'active': ''}],
    'project_rows': [[{'name': 'Mario', 'tag': 'Loving Recreation of Mario', 'tools': 'Unity, C#', 'link': 'github.com', 'img': './static/img/logo.jpg'},
    {'name': 'Mario', 'tag': 'Loving Recreation of Mario', 'tools': 'Unity, C#', 'link': 'github.com', 'img': './static/img/logo.jpg'},
    {'name': 'Mario', 'tag': 'Loving Recreation of Mario', 'tools': 'Unity, C#', 'link': 'github.com', 'img': './static/img/logo.jpg'}
    ],[{'name': 'Mario', 'tag': 'Loving Recreation of Mario', 'tools': 'Unity, C#', 'link': 'github.com', 'img': './static/img/logo.jpg'},
    {'name': 'Mario', 'tag': 'Loving Recreation of Mario', 'tools': 'Unity, C#', 'link': 'github.com', 'img': './static/img/logo.jpg'},
    {'name': 'Mario', 'tag': 'Loving Recreation of Mario', 'tools': 'Unity, C#', 'link': 'github.com', 'img': './static/img/logo.jpg'}
    ]],
    'facebook': 'facebook.com',
    'github': 'github.com',
    'instagram': 'instagram.com',
    'linkedin':'linkedin.com' ,
    'twitter':'twitter.com'
 }

def openweathermap(city_name):
    api_key = str(os.getenv("APIKEY")) #Openweathermap api key is easy to obtain
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + f'appid={api_key}' + "&q=" + city_name
    response = requests.get(complete_url)
    #requests json information from the API
    x = response.json()
    x=x['weather']
    x= x[0]
    return x['description']

@app.route('/')
def index():
    return render_template('index.html', title='Tanzir Hasan', url=os.getenv('URL'), name=userinfo['name'],
    shortIntro=userinfo['shortIntro'], longIntro = userinfo['longIntro'], work = userinfo['work'], skills = userinfo['skills'],
    education = userinfo['education'], email=userinfo['email'], facebook = userinfo['facebook'], instagram = userinfo['instagram'],
    github=userinfo['github'], linkedin=userinfo['linkedin'], twitter = userinfo['twitter'], profilepic='./static/img/profile.jpg',
    weather=openweathermap('Seattle'))

@app.route('/hobbies')
def hobbies():
    return render_template('hobbies.html', 
    title="Hobbies", 
    url=os.getenv("URL"),
    hobbies = userinfo["hobbies"],
    email=userinfo['email'], 
    facebook = userinfo['facebook'], 
    instagram = userinfo['instagram'],
    github=userinfo['github'], 
    linkedin=userinfo['linkedin'], 
    twitter = userinfo['twitter']
    )

@app.route('/projects')
def projects():
    return render_template('projects.html', 
    title="Projects", 
    url=os.getenv("URL"),
    project_rows = userinfo['project_rows'],
    email=userinfo['email'], 
    facebook = userinfo['facebook'], 
    instagram = userinfo['instagram'],
    github=userinfo['github'], 
    linkedin=userinfo['linkedin'], 
    twitter = userinfo['twitter']
    )

@app.route('/api/timeline_post', methods=['POST'])
def post_time_line_post():
    name = request.form['name']
    email = request.form['email']
    content = request.form['content']
    timeline_post = TimelinePost.create(name=name, email=email, content=content)
    if timeline_post.id > 10:
        TimelinePost.delete_by_id(timeline_post.id-10)
    return redirect(request.referrer)

@app.route('/api/timeline_post', methods=['GET'])

def get_time_line_post():
    return {
        'timeline_posts': [
            model_to_dict(p)
            for p in 
            TimelinePost.select().where(TimelinePost.id > 0).order_by(TimelinePost.created_at.desc())
        ]
    }

@app.route('/api/timeline_post', methods=['DELETE'])

def delete_time_line_post():
    for i in range(int(request.form['start']), int(request.form['end'])+1):
        TimelinePost.delete_by_id(i)
    return 'Emptied'

@app.route('/timeline')

def timeline():
    return render_template('timeline.html',
    posts = get_time_line_post(),
    title="Timeline", 
    url=os.getenv("URL"),
    project_rows = userinfo['project_rows'],
    email=userinfo['email'], 
    facebook = userinfo['facebook'], 
    instagram = userinfo['instagram'],
    github=userinfo['github'], 
    linkedin=userinfo['linkedin'], 
    twitter = userinfo['twitter'])