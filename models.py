from google.appengine.ext import db

class Page(db.Model):
    slug      = db.StringProperty()
    title     = db.StringProperty()
    body      = db.TextProperty()
    body_html = db.TextProperty()
    created   = db.DateTimeProperty(auto_now_add=True)
    updated   = db.DateTimeProperty()
