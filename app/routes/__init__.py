from flask import abort, redirect, request, render_template
from app import app
from db import db
import main_feed
import filter_dir.filter
from sqlalchemy import or_
from models.article import Article
from models.answer import Answer
from models.source import Source

def search(text):
    new_query = Article.query
    new_query = new_query.filter(or_(Article.title.contains(text), Article.body.contains(text), Article.tags.contains(text)))
    new_query = new_query.filter(Article.unread == True)
    new_query = new_query.filter(filter_dir.filter.set_filter >= Article.distress)
    new_query = new_query.order_by(Article.date_added.desc())
    article_list = new_query.all()
    q = Source.query
    q = q.order_by(Source.title)
    sources = q.all()
    return article_list, sources

@app.route('/', methods=['GET'])
def index():
    new_query = Article.query
    new_query = new_query.filter(Article.unread == True)
    new_query = new_query.filter(filter_dir.filter.set_filter >= Article.distress)
    new_query = new_query.order_by(Article.date_added.desc())
    article_list = new_query.all()
    q = Source.query
    q = q.order_by(Source.title)
    sources = q.all()
    return render_template('index.html', articles = article_list, sources = sources)

@app.route('/', methods=['POST'])
def post_index():
    if request.form['form'] == 'Add feed':
        url = request.form['feed']
        parsed = main_feed.parsing_method(url)
        source = main_feed.source_get(parsed)
        s = Source.insert_feed(url, source)
        if s:
            articles = main_feed.articles_get(parsed)
            Article.insert_feed(s.id, articles)
        return redirect('/')
    elif request.form['form'] == 'Set filter':
        filter_dir.filter.set_filter = request.form["filter"]
        return redirect('/')
    elif request.form['form'] == 'Submit':
        Answer.insert_answer(request.form['answer1'],
        request.form['answer2'], request.form['answer3'], request.form['comment'])
        return redirect('/')
    elif request.form['form'] == 'Search':
        article_list, sources = search(request.form['search'])
        return render_template('index.html', articles = article_list, sources = sources)
    else:
        return redirect('/')


@app.route('/read/<int:article_id>', methods=['GET'])
def get_read(article_id):
    article = Article.query.get(article_id)
    article.unread = False
    db.session.commit()
    return redirect(article.link)
