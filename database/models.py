from mongoengine import *
import datetime


class Article(Document):
    """
    A MongoEngine document
    """
    title = StringField(required=True)
    body = StringField(required=True)
    author = StringField(required=True)
    published = DateTimeField(default=datetime.datetime.now)
