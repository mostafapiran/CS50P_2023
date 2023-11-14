# Multiple web apps (NLP and etc)
#### Video Demo:  <https://youtu.be/sWYBVhyzjLw>
#### Description:

The provided code is a simple web application built using Flask, a popular Python web framework, and it includes functionalities related to natural language processing (NLP), factorial calculation, and password management. Let's break down the code and explain its components.

#### You can experience using this project at the following address:
https://mostafa314.pythonanywhere.com

### 1. Flask Application Setup:

```python
from flask import Flask, render_template, request
from textblob import TextBlob

passwords = {}

project = Flask(__name__)
```

- The code imports necessary modules: `Flask` for web application development, `render_template` for rendering HTML templates, and `request` for handling HTTP requests. Additionally, it imports `TextBlob` from the `textblob` library, which is used for natural language processing.

- A dictionary called `passwords` is initialized to store account-password pairs.

- An instance of the Flask class is created and named `project`.

### 2. Functions:

#### `main()`

```python
def main():
    project.run(debug=True)
```

- The `main()` function is defined to run the Flask application in debug mode when executed directly.

#### `analyze_sentiment(text)`

```python
def analyze_sentiment(text):
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity

    if sentiment > 0:
        return "Positive"
    elif sentiment == 0:
        return "Neutral"
    else:
        return "Negative"
```

- `analyze_sentiment` takes a text input, uses TextBlob to perform sentiment analysis, and returns the sentiment as "Positive," "Neutral," or "Negative."

#### `factorial(num)`

```python
def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1)
```

- `factorial` calculates the factorial of a given number using recursion.

#### `add_password(account, password)`

```python
def add_password(account, password):
    passwords[account] = password
    return f"Password added for: {account}"
```

- `add_password` adds an account-password pair to the `passwords` dictionary and returns a confirmation message.

#### `view_password(account)`

```python
def view_password(account):
    if account in passwords:
        return f"Password for {account} : {passwords[account]}"
    else:
        return f"Password not found for: {account}"
```

- `view_password` retrieves the password for a given account from the `passwords` dictionary and returns a message.

### 3. Flask Routes:

#### `index()`, `nlp()`, `factor()`, `password()`

```python
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
```

- These routes define the behavior when the user accesses specific URLs. They render HTML templates associated with each route.

#### `nlplink()`, `calculatelink()`, `Passwordlink()`

```python
@project.route('/nlplink', methods=['POST'])
def nlplink():
    # ... (see next explanation)

@project.route('/calculatelink', methods=['POST'])
def calculatelink():
    # ... (see next explanation)

@project.route('/Passwordlink', methods=['POST'])
def Passwordlink():
    # ... (see next explanation)
```

- These routes handle the form submissions for NLP, factorial calculation, and password management.

### 4. Form Handling Routes:

#### `nlplink()`

```python
@project.route('/nlplink', methods=['POST'])
def nlplink():
    if request.method == 'POST':
        temp = request.form['text_nlp']
        sentiment = analyze_sentiment(temp)
        return render_template('result.html', texttemp="My sense of the sentence you wrote is", temp=sentiment)
```

- Handles the form submission for NLP. Retrieves the input text from the form, performs sentiment analysis, and renders a result page.

#### `calculatelink()`

```python
@project.route('/calculatelink', methods=['POST'])
def calculatelink():
    if request.method == 'POST':
        number = int(request.form['number'])
        fact = factorial(number)
        return render_template('result.html', texttemp=f"factorial of {number} is:", temp=fact)
```

- Handles the form submission for factorial calculation. Retrieves the input number, calculates its factorial, and renders a result page.

#### `Passwordlink()`

```python
@project.route('/Passwordlink', methods=['POST'])
def Passwordlink():
    if request.method == 'POST':
        account = request.form['un_in']
        password = request.form['pas_in']
        account_R = request.form['un_out']
        if account and password:
            texttemp = add_password(account, password)
            return render_template('result.html', texttemp=texttemp)
        if account_R:
            texttemp = view_password(account_R)
            return render_template('result.html', texttemp=texttemp)
```

- Handles the form submission for password management. Retrieves input account, password, and account for retrieval. Calls `add_password` or `view_password` accordingly and renders a result page.

### 5. Application Execution:

```python
if __name__ == "__main__":
    main()
```

- The application is executed if the script is run directly.

### Conclusion:

This Flask application integrates natural language processing, factorial calculation, and password management functionalities through different routes. Users can access specific pages, input data through forms, and receive results based on the implemented functionalities. The HTML templates associated with each route provide the user interface for interacting with the application.
