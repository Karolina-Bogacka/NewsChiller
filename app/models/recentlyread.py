from db import db
import filter
from sqlalchemy.sql.expression import func
import datetime

class Recently(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.Text, nullable = False)
    body = db.Column(db.Text, nullable = False)
    link = db.Column(db.Text, nullable = False)
    guid = db.Column(db.String(255), nullable = False)
    distress = db.Column(db.Integer, nullable = False)
    category = db.Column(db.String(255), nullable = False)
    #source_id = db.Column(db.Integer, db.ForeignKey('source.id'), nullable = False)
    #source = db.relationship('Source', backref = db.backref('recently', lazy = True))
    date_added = db.Column(db.DateTime, default = datetime.datetime.utcnow)
    date_published = db.Column(db.DateTime)
    #__table_args__ = (
    #    db.UniqueConstraint('source_id', 'guid', name='uc_source_guid'),
    #)

    @classmethod
    def insert_recent(cls, recently):
        article = Recently(title = recently.title,
                body = recently.body,
                link = recently.link,
                guid = recently.id,
                distress = recently.distress,
                category = recently.category,
                date_published = recently.date_published)
        db.session.add(article)
        db.session.commit()

    @classmethod
    def delete_last(cls):
        count = db.session.query(func.count(Recently.title)).scalar()
        if count>10:
            obj = Recently.query.filter_by(func.min(Recently.date_added)).one()
            session.delete(obj)
            session.commit()
