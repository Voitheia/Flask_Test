from flask import Flask
app = Flask(__name__)

#root route, basically the homepage
#having two routes means that flask will put the same html on both of those pages
@app.route('/')
@app.route('/home')
def home():
    return '<h1>this is the home page</h1><p>theres no place like 127.0.0.1 :)))))))</p>'

#about page route
@app.route('/about')
def about():
    return '<h1>this is the about page</h1><p>this page is about things</p>'


#allows us to run the web server with python so we don't have to type stuff in the terminal
#also turns on debug mode so that we can make changes while the web server is running
if __name__ == '__main__':
    app.run(debug=True)
#an alternative to doing this is in the terminal running the following commands:
# $env:FLASK_APP = "<.py name>" (in this case Flask_Test.py)
# $env:FLASK_DEBUG = 1 (turns debug mode on)