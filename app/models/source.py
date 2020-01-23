from db import db
import datetime

class Source(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text, nullable=False)
    subtitle = db.Column(db.Text, nullable=False)
    link = db.Column(db.Text, nullable=False)
    feed = db.Column(db.Text, nullable=False)
    date_added = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    @classmethod
    def insert_feed(cls, feed, source):
        link = source['link']
        title = source['title']
        subtitle = source['subtitle']
        new_source = None
        if Source.query.filter(Source.link==source['link']) :
            new_source = Source(feed=feed, link=link, title=title, subtitle=subtitle)
            db.session.add(new_source)
            db.session.commit()
        count = db.session.query(func.count(Source.title)).scalar()
        if count>10:
            db.session.query(func.min(Source.date_added)).delete()
            db.session.commit()
        return new_source
