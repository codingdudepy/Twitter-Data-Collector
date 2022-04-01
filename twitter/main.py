###DATE 3.19.22###
###CODER codingdudepy###
### FUNCTION: TWITTER DATA COLLECTOR ###



#Do not use this code to provide purposes such as selling or illegal activities such as doxxing
######    AS STATED IN MIT LICENSE     ######



#Following code has been last modified at:  12: 41 PM (Pacific Time)


#Encounters
### None so far ###

#Initlizaing packages 
from crypt import methods
import flask
import tweepy
from flask import Flask, render_template, request, send_from_directory, url_for, redirect
from markupsafe import Markup
import requests
import os
import gunicorn
import smtplib, ssl
import twitter
from flask_mail import Mail, Message
#Defining App
app = Flask(__name__)


@app.route('/twitter', methods = ['POST', 'GET'])
def repo():
    if request.method == 'POST':
        twitter = request.form['namew']

        return redirect(f"/users/{twitter}")

#Defining repo function for returning data
@app.route('/users/<twitter>')
def users(twitter):
    bearer_token = "xxxxxx"

    client = tweepy.Client(bearer_token)
    
 
    response = client.search_recent_tweets(twitter, max_results='20')
    tweetsww = []
    for tweet in response.data:
        tweetsww.append(tweet.text)
        tweetsww.append("\n")
    result_list = '\n'.join(tweetsww)

    return render_template("twitter.html", splits = (f'{result_list}')
)

#Defining application route
@app.route("/application", methods=['POST', 'GET'])
def application():
    if request.method == 'POST':
        name = request.form["name"]
        github = request.form["github"]
        age = request.form["age"]
        location = request.form["location"]
        email = request.form["email"]
        explain = request.form["explain"]
        return redirect(f"/final/{name}/{github}/{age}/{location}/{email}/{explain}")


#Defining redirect when application is subbmitted value as submit
@app.route("/final/<name>/<github>/<age>/<location>/<email>/<explain>", methods=['GET','POST'])
def final(name, github, age, location, email, explain):
    mail= Mail(app)

    app.config['MAIL_SERVER']='smtp.gmail.com'
    app.config['MAIL_PORT'] = 465
    app.config['MAIL_USERNAME'] = 'prodatacollectors@gmail.com'
    app.config['MAIL_PASSWORD'] = ''
    app.config['MAIL_USE_TLS'] = False
    app.config['MAIL_USE_SSL'] = True
    b = Markup(f"Name: {name}\r\nGithub: {github}\r\nAge: {age}\r\nlocation: {location}\r\nemail: {email}\r\nexplanation: {explain}")
    msg = Message(f'Application {name}', sender = 'prodatacollectors@gmail.com', recipients = [email])
    msg.body = b
    mail.send(msg)
    return render_template("final.html")


#Route for home 
@app.route("/")
def home():
    return render_template("index.html")
    
#Route for apply linked on index.html page
@app.route("/apply")
def apply():
    return render_template("apply.html")


#Running app
if __name__ == "__main__":
    app.run(debug=True)
