from db import db
import filter
import datetime

class Article(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.Text, nullable = False)
    body = db.Column(db.Text, nullable = False)
    link = db.Column(db.Text, nullable = False)
    guid = db.Column(db.String(255), nullable = False)
    unread = db.Column(db.Boolean, default = True, nullable = False)
    distress = db.Column(db.Integer, default = 0, nullable = False)
    source_id = db.Column(db.Integer, db.ForeignKey('source.id'), nullable = False)
    source = db.relationship('Source', backref = db.backref('articles', lazy = True))
    date_added = db.Column(db.DateTime, default = datetime.datetime.utcnow)
    date_published = db.Column(db.DateTime)
    __table_args__ = (
        db.UniqueConstraint('source_id', 'guid', name='uc_source_guid'),
    )

    @classmethod
    def insert_feed(cls, source_id, feed_articles):
        insert = Article.__table__.insert().prefix_with('IGNORE')
        article_list = []
        print("filterinsert")
        d = filter.classify("lol")
        print(d)
        print("fuuuuuuck")
        for position in feed_articles:
            distress = filter.classify(position['title'])
            print("distress")
            print(distress)
            article_list.append({
                'title': position['title'],
                'body': position['summary'],
                'link': position['link'],
                'guid': position['id'],
                'distress': distress,
                'source_id': source_id,
                'date_published': position['published'],
            })
        db.engine.execute(insert, article_list)
