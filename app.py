from flask import Flask

# setting up
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Welcome, busyqa! This is a simple Flask app.'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port=8000)


