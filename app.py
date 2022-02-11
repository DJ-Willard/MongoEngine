import os
from flask import Flask, redirect, url_for, request, render_template
from flask_restful import Api
from mongoengine import connect
from resources import ArticleAPI, ArticlesAPI, AuthorAPI, AuthorsAPI


app = Flask(__name__)
api = Api(app)
connect(host=f"mongodb://localhost:5000/articles")

api.add_resource(ArticlesAPI, '/api/articles')
api.add_resource(ArticleAPI, '/api/article/<id>')

api.add_resource(AuthorsAPI, '/api/authors')
api.add_resource(AuthorAPI, '/api/author/<author>')


@app.route('/', defaults={'article': None, 'author': None})
@app.route('/<article>', defaults={'author': None})
@app.route('/author/<author>', defaults={'article': None})
def index(article, author):
    return render_template('index.html', admin=False, article=article, author=author)


@app.route('/admin')
def admin():
  return render_template('index.html', admin=True)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=5001)
