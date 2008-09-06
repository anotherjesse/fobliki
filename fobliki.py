from google.appengine.ext import db
from google.appengine.api import users
from vendor import web
from models import *

urls = (
  '/login', 'login',
  '/logout', 'logout',
  '(.*)', 'page'
)

render = web.template.render('templates', base='base')

class logout:
    def GET(self):
         return web.seeother(users.create_logout_url('/'))

class login:
    def GET(self):
         return web.seeother(users.create_login_url('/'))

class page:
    def GET(self, slug):
        key = db.Key.from_path('Page', slug)
        page = Page.get(key)
        if users.is_current_user_admin():
            if page:
                if web.ctx.query == '':
                    return render.show(page, slug)
            else:
                page = Page()
            return render.edit(page, slug)
        else:
            if page:
                return render.show(page, slug)
            return render.missing(slug)
    def POST(self, slug):
        if not users.is_current_user_admin():
            return web.seeother('/')
        key = db.Key.from_path('Page', slug)
        page = Page.get(key)
        if page == None:
            page = Page(key_name=slug)

        i = web.input()
        page.slug = slug
        page.title = i.title
        page.body = i.body
        page.put()
        return web.seeother(slug)

app = web.application(urls, globals())
main = app.cgirun()
