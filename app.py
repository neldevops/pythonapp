from flask import Flask

# setting up#
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1><b>Welcome, This is a Containerized Flask app. By Nelson Nwajie </b></h1>'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port=8000)


