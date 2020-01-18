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
        img_link = None
        img_credit = None
        tags = []
        if 'media_content' in ready and ready['media_content'][0]['medium'] == 'image':
            img_link = ready['media_content'][0]['url']
            if 'media_credit' in ready and 'content' in ready['media_credit'][0]:
                img_credit = ready['media_credit'][0]['content']
        if 'tags' in ready:
            for t in ready['tags']:
                tags.append(t['term'].lower())
        tags = ' '.join(word for word in tags)
        article_list.append({
        'id': ready['id'],
        'link': ready['link'],
        'title': ready['title'],
        'summary': ready['summary'],
        'published': ready['published_parsed'],
        'img_link': img_link,
        'img_credit': img_credit,
        'tags': tags
        })
    return article_list
