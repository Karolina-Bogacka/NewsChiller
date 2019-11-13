import feedparser

def source_get(parsed):
    ready_feed = parsed['feed']
    return {
    'link': ready_feed['link'],
    'title': ready_feed['title'],
    'subtitle': ready_feed['subtitle'],
    }

def parsing_method(url):
    return feedparser.parse(url)

def articles_get(parsed):
    article_list = []
    ready_entries = parsed['entries']
    for ready in ready_entries:
        article_list.append({
        'id': ready['id'],
        'link': ready['link'],
        'title': ready['title'],
        'summary': ready['summary'],
        'published': ready['published_parsed'],
        })
    return article_list
