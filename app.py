from flask import Flask, render_template
from articles import Article

app = Flask(__name__)

articles = Article.all()


@app.route("/")
def blog():
    return render_template('blog.html', articles=articles)


@app.route('/blog/<slug>')
def hello_world(slug: str):
    article = articles[slug]
    return render_template('article.html', article=article)


if __name__ == '__main__':
    app.run(port=4000, debug=True)
