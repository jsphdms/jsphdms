from flask import Flask, render_template
app = Flask(__name__)

posts = [
            {
                'author': 'Joseph Adams',
                'title': 'Here is a title',
                'content': 'This is the content of the post',
                'date_posted': '2019-07-30'
                },
            {
                'author': 'Joe Bloggs',
                'title': 'Another title',
                'content': 'This is some more content',
                'date_posted': '2019-07-31'
                }
        ]

@app.route('/')
def home():
    return render_template('home.html', posts = posts)

@app.route('/post')
def post():
    return render_template('post.html')

if __name__ == '__main__':
	app.run(debug=True)
