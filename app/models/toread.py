from db import db
import filter
from sqlalchemy.sql.expression import func
import datetime

class ToRead(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.Text, nullable = False)
    body = db.Column(db.Text, nullable = False)
    link = db.Column(db.Text, nullable = False)
    guid = db.Column(db.String(255), nullable = False)
    distress = db.Column(db.Integer, default = 0, nullable = False)
    source_id = db.Column(db.Integer, db.ForeignKey('source.id'), nullable = False)
    source = db.relationship('Source', backref = db.backref('toread', lazy = True))
    date_added = db.Column(db.DateTime, default = datetime.datetime.utcnow)
    date_published = db.Column(db.DateTime)
    __table_args__ = (
        db.UniqueConstraint('source_id', 'guid', name='uc_source_guid'),
    )

    @classmethod
    def insert_read(cls, add):
        article = ToRead(title = add.title,
                body = add.body,
                link = add.link,
                guid = add.id,
                distress = add.distress,
                source_id = add.source_id,
                date_published = recently.date_published)
        db.session.add(article)
        db.session.commit()

    @classmethod
    def delete_read(cls, title):
        obj = ToRead.query.filter_by(ToRead.title == title).one()
        session.delete(obj)
        session.commit()
