from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World!"

@app.route('/dojo')
def dojo():
    print("dojo")
    return "Dojo!"

@app.route('/say/<word>')
def say(word):
    return "Hi " + word + "!"

@app.route('/repeat/<int:num>/<word>')
def repeat(num, word):
    return f"{word}\n" * (num)

@app.route('/<path:path>')
def catch_all(path):
    return "Sorry! No response. Try again."

if __name__ == "__main__":
    app.run(debug=True)