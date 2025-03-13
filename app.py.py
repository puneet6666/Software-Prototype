from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, this is the To-Do List app!"

if __name__ == "__main__":
    app.run(debug=True, port=3000)
