from db import db
import filter
from sqlalchemy.sql.expression import func
import datetime
from models.article import Article

class ToRead(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.Text, nullable = False)
    body = db.Column(db.Text, nullable = False)
    link = db.Column(db.Text, nullable = False)
    guid = db.Column(db.String(255), nullable = False)
    distress = db.Column(db.Integer, default = 0, nullable = False)
    category = db.Column(db.String(255), nullable = False)
    date_added = db.Column(db.DateTime, default = datetime.datetime.utcnow)
    date_published = db.Column(db.DateTime)

    @classmethod
    def insert_read(cls, add):
        article_query = Article.query
        article_query = article_query.filter(Article.id == add['id'])
        object = article_query.all()
        for i in object:
            print(i.title)
        print(add)
        object = object[-1]
        article = ToRead(title = object.title,
                body = object.body,
                link = object.link,
                guid = object.id,
                distress = object.distress,
                category = object.category,
                date_published = object.date_published)
        print(article.title)
        db.session.add(article)
        db.session.commit()

    @classmethod
    def delete_read(cls, title):
        obj = ToRead.query.filter_by(ToRead.title == title).one()
        session.delete(obj)
        session.commit()
