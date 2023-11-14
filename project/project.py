from flask import Flask, render_template, request
from textblob import TextBlob

passwords = {}

project = Flask(__name__)

def main():
    project.run(debug=True)

def analyze_sentiment(text):
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity

    if sentiment > 0:
        return "Positive"
    elif sentiment == 0:
        return "Neutral"
    else:
        return "Negative"

def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1)

def add_password(account, password):

    passwords[account] = password

    return f"Password added for: {account}"

def view_password(account):
    if account in passwords:
        return f"Password for {account} : {passwords[account]}"
    else:
        return f"Password not found for: {account}"

@project.route('/')
def index():
    return render_template('index.html')

@project.route('/nlp')
def nlp():
    return render_template('nlp.html')

@project.route('/factorial')
def factor():
    return render_template('factorial.html')

@project.route('/password')
def password():
    return render_template('password.html')

@project.route('/nlplink', methods=['POST'])
def nlplink():
    if request.method == 'POST':
        temp = request.form['text_nlp']
        sentiment = analyze_sentiment(temp)
        return render_template('result.html',texttemp = "My sense of the sentence you wrote is", temp = sentiment)

@project.route('/calculatelink', methods=['POST'])
def calculatelink():
    if request.method == 'POST':
        number = int(request.form['number'])
        fact = factorial(number)
        return render_template('result.html', texttemp=f"factorial of {number} is:", temp=fact)

@project.route('/Passwordlink', methods=['POST'])
def Passwordlink():
    if request.method == 'POST':
        account = request.form['un_in']
        password = request.form['pas_in']
        account_R = request.form['un_out']
        if account and password:
            texttemp = add_password(account, password)
            return render_template('result.html', texttemp = texttemp)
        if account_R:
            texttemp = view_password(account_R)
            return render_template('result.html', texttemp=texttemp)

if __name__ == "__main__":
    main()
