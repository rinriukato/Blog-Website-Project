from flask import Flask, render_template
import requests

app = Flask(__name__)
BLOG_ENDPOINTS = "https://api.npoint.io/de6a1553488cfe6c7dc1"


@app.route('/')
def home():
    response = requests.get(url=BLOG_ENDPOINTS)
    all_posts = response.json()
    return render_template('index.html', posts=all_posts)


@app.route('/<page_name>')
def get_blog(page_name):
    return render_template(page_name)


@app.route('/post/<int:index>')
def get_blog_entry(index):
    response = requests.get(url=BLOG_ENDPOINTS)
    all_posts = response.json()

    this_post = None
    for post in all_posts:
        if post['id'] == index:
            this_post = post

    return render_template('post.html', post=this_post)


if __name__ == "__main__":
    app.run(debug=True)
