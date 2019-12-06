from flask import abort, redirect, request, render_template
from app import app
from db import db
import main_feed
import filter
from models.article import Article
from models.source import Source

@app.route('/', methods=['GET'])
def index():
    new_query = Article.query
    new_query = new_query.filter(Article.unread == True)
    new_query = new_query.filter(filter.set_filter <= Article.distress)
    new_query = new_query.order_by(Article.date_added.desc())
    article_list = new_query.all()
    return render_template('index.html', articles = article_list)

@app.route('/read/<int:article_id>', methods=['GET'])
def get_read(article_id):
    article = Article.query.get(article_id)
    article.unread = False
    db.session.commit()
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
