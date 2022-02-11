from flask import Response, request
from database.models import Article
from flask_restful import Resource


class ArticlesAPI(Resource):
    def get(self):
        articles = Article.objects().order_by('-published').to_json()
        return Response(articles, mimetype="application/json", status=200)

    def post(self):
        body = request.get_json()
        article = Article(**body).save()
        id = article.id
        return {'id': str(id)}, 200
