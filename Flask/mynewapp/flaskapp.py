from app import app

from flask import Flask
from flask import render_template
#instance of flask class in app
app = Flask(__name__)

#decorator - to start the web app / here
@app.route('/')
@app.route('/index')
def main():
    return render_template('index.html')

@app.route('/showmap' methods=['GET'])
def showmap():
    #render_template needs bootstrap
    return render_template('showmap.html')

if __name__ == '__main__':
    app.run()
