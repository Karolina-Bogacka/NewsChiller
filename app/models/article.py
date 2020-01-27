from db import db
import filter_dir.filter
from filter_dir.filter import classify
import filter_dir.filter_bert
from filter_dir.filter_bert import classify_bert
import filter_dir.binary_filter
import datetime
from sqlalchemy.sql.expression import func

class Article(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.Text, nullable = False)
    body = db.Column(db.Text, nullable = False)
    link = db.Column(db.Text, nullable = False)
    guid = db.Column(db.String(255), nullable = False)
    unread = db.Column(db.Boolean, default = True, nullable = False)
    distress = db.Column(db.Integer, default = 0, nullable = False)
    img_link = db.Column(db.Text, nullable = True)
    img_credit = db.Column(db.Text, nullable = True)
    tags = db.Column(db.Text, nullable = True)
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
        for position in feed_articles:
            distress = filter_dir.binary_filter.classify_bert([position['title']])
            article_list.append({
                'title': position['title'],
                'body': position['summary'],
                'link': position['link'],
                'guid': position['id'],
                'distress': int(distress),
                'source_id': source_id,
                'date_published': position['published'],
                'img_link': position['img_link'],
                'img_credit': position['img_credit'],
                'tags': position['tags']
            })
        db.engine.execute(insert, article_list)
        count = db.session.query(func.count(Article.title)).scalar()
        if count>100:
            db.session.query(func.min(Article.date_added)).one().delete()
            db.session.commit()
