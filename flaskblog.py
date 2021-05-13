from flask import Flask, render_template
app = Flask(__name__)

#posts
posts = [
    {
        'author':'Luna Rivera',
        'title':'Blog Post 1',
        'content':'First post content',
        'date_posted':'April 20, 2021'
    },
    {
        'author':'Angel Azucena',
        'title':'Blog Post 2',
        'content':'First post content',
        'date_posted':'May 4, 2021'
    }
]

@app.route("/")
@app.route("/home")
def Home():
    return render_template('home.html', posts = posts)

@app.route("/about")
def About():
    return render_template('about.html',title='About')

if __name__ == '__main__':
    app.run(debug=True)    