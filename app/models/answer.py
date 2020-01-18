from db import db
import datetime

class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    answer1 = db.Column(db.Boolean, nullable=False, default=True)
    answer2 = db.Column(db.Boolean, nullable=False, default=True)
    answer3 = db.Column(db.Boolean, nullable=False, default=True)
    comment = db.Column(db.Text, nullable=True)

    @classmethod
    def insert_answer(cls, answer1, answer2, answer3, comment):
        print("in answer")
        new_answer = Answer(answer1=bool(answer1), answer2=bool(answer2), answer3=bool(answer3), comment=comment)
        db.session.add(new_answer)
        db.session.commit()
        return new_answer
