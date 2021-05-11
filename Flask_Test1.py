from flask import Flask, render_template, url_for
app = Flask(__name__)

#this posts variable is a list of dictionaries, used as dummy data for blog posts
#basically just a replacement for a database call
posts = [
    {
        'author': 'author1',
        'title': 'title1',
        'content': 'first lul',
        'date_posted': '5/10/21'
    },
    {
        'author': 'author2',
        'title': 'title2',
        'content': '2nd eeeeeeeee',
        'date_posted': '5/11/21'
    }
]

#this variable passes the page titles to flask in the render_template call
titles = [
    'Home', 'About'
]

#root route, basically the homepage
#having two routes means that flask will put the same html on both of those pages
#by using the render_template, we are able to pass an html document to flask for it to put on the web server
#by passing posts=posts to render_template, we can give the template the data from the posts variable
@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html.j2', posts=posts, title=titles[0])

#about page route
@app.route('/about')
def about():
    return render_template('about.html.j2', title=titles[1])


#allows us to run the web server with python so we don't have to type stuff in the terminal
#also turns on debug mode so that we can make changes while the web server is running
if __name__ == '__main__':
    app.run(debug=True)
#an alternative to doing this is in the terminal running the following commands:
# $env:FLASK_APP = "<.py name>" (in this case Flask_Test.py)
# $env:FLASK_DEBUG = 1 (turns debug mode on)