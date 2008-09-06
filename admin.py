from vendor import web

urls = (
  '.*', 'stub'
)

class stub:
    def GET(self):
        return "beta"

app = web.application(urls, globals())
main = app.cgirun()
