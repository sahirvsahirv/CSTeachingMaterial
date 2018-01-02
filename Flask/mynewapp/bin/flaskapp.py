from flask import Flask
#instance of flask class in app
app = Flask(__name__)

#decorator - to start the web app / here
@app.route('/')
def main():
    return u'hello world'

if __name__ == '__main__':
    app.run()
