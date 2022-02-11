from flask import Response, request
from database.models import Article
from flask_restful import Resource


class ArticleAPI(Resource):
    def get(self, id):
        article = Article.objects.get(id=id).to_json()
        return Response(article, mimetype="application/json", status=200)

    def put(self, id):
        body = request.get_json()
        Article.objects.get(id=id).update(**body)
        return {'id': str(id), 'status': 'updated'}, 200

    def delete(self, id):
        Article.objects.get(id=id).delete()
        return {'id': str(id), 'status': 'deleted'}, 200
