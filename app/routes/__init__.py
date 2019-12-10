from flask import abort, redirect, request, render_template
from app import app
from db import db
import main_feed
import filter
from models.article import Article
from models.source import Source
from models.recentlyread import Recently

@app.route('/', methods=['GET'])
def index():
    new_query = Article.query
    new_query = new_query.filter(Article.unread == True)
    new_query = new_query.filter(filter.set_filter <= Article.distress)
    new_query = new_query.order_by(Article.date_added.desc())
    article_list = new_query.all()
    print([i.distress for i in article_list])
    return render_template('index.html', articles = article_list)

@app.route('/read/<int:article_id>', methods=['GET'])
def get_read(article_id):
    article = Article.query.get(article_id)
    article.unread = False
    db.session.commit()
    Recently.insert_recent(article)
    Recently.delete_last()
    return redirect(article.link)

@app.route('/article/<int:article_id>', methods=['GET'])
def get_article(article_id):
    article = Article.query.get(article_id)
    article.unread = False
    db.session.commit()
    Recently.insert_recent(article)
    Recently.delete_last()
    return redirect(article.link)

@app.route('/sources', methods=['GET'])
def get_source():
    q = Source.query
    q = q.order_by(Source.title)
    sources = q.all()
    return render_template('sources.html', sources = sources)

@app.route('/sources', methods=['POST'])
def post_source():
    url = request.form['feed']
    parsed = main_feed.parsing_method(url)
    source = main_feed.source_get(parsed)
    s = Source.insert_feed(url, source)
    articles = main_feed.articles_get(parsed)
    Article.insert_feed(s.id, articles)
    return redirect('/sources')

@app.route('/filters', methods=['GET'])
def filtered():
    return render_template('filters.html')

@app.route("/filters", methods=["POST"])
def test():
    filter.set_filter = request.form["filter"]
    print("set_filter")
    print(request.form["filter"])
    return redirect('/filters')

@app.route("/article_list", methods=['GET'])
def article_list():
    new_query = Article.query
    new_query = new_query.filter(Article.unread == True)
    new_query = new_query.filter(filter.set_filter <= Article.distress)
    new_query = new_query.order_by(Article.date_added.desc())
    article_list = new_query.all()
    return article_list

@app.route("/source_list", methods=['GET'])
def source_list():
    new_query = Source.query
    source_list = new_query.all()
    return source_list

@app.route("/recently_read", methods=['GET'])
def recently_list():
    new_query = Recently.query
    recently_list = new_query.all()
    return recently_list

@app.route("/recently_read", methods=['POST'])
def recently_list_post():
    Recently.insert_recent()
    return recently_list

@app.route("/to_read", methods=['GET'])
def toread_list():
    new_query = ToRead.query
    toread_list = new_query.all()
    return toread_list

@app.route("/to_read", methods=['POST'])
def toread_list_post():
    ToRead.insert_read(add)
    return recently_list

@app.route("/to_read", methods=['DELETE'])
def toread_list_delete():
    ToRead.delete_read(title)
    return recently_list
