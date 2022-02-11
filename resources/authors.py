from flask import Response, request
from database.models import Article
from flask_restful import Resource


class AuthorAPI(Resource):
    def get(self, author):
        articles = Article.objects(author=author).order_by('-published').to_json()
        return Response(articles, mimetype="application/json", status=200)


class AuthorsAPI(Resource):
    def get(self):
        articles = Article.objects().only('author')
        authors = list(set([x.author for x in articles]))
        return authors, 200
