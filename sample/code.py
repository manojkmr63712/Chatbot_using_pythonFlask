import random
from flask import Flask, request, render_template
import requests

app = Flask(__name__)
dataout = ''

@app.route("/")
def home():
    return render_template("index.html")
@app.route("/get")
def get_bot_response():
    symptom = request.args.get('msg')
    nameIn = ['what is your name', 'whats your name', 'whats your name?', 'what is your name?']
    greetIn = ['hello', 'hi','hii', 'hi there', 'hello there']
    bith = ['what is your date of birth', 'what is your date of birth', 'what is your DOB', 'what is your DOB?']
    botmasterIn = ['who is your botmaster', 'who is your botmaster?', 'who is your father', 'who is your mother']
    greetOut = ['hi there', 'hello', 'hi my name is mady', 'hello there']
    nameOut = ['Iam called mady', 'My name is Mady', 'Im called mady']
    botmasterOut = ['My master is notebook data', 'Notebook data is my master']
    symlower = symptom.lower()
    if symlower == '':
        dataout = 'Thanks for the chat. Nice meeting you'
    elif symlower in nameIn:
        dataout = (random.choice(nameOut))
    elif symlower in greetIn:
        dataout = (random.choice(greetOut))
    elif symlower in botmasterIn:
        dataout = (random.choice(botmasterOut))
    elif symlower in bith:
        dataout = 'I was activated in the 2016'
    return (dataout)

if __name__ == '__main__':
    app.run(debug=True)