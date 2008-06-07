from google.appengine.ext import db
from vendor import web
from models import *

urls = (
  '/', 'index',
  '/list', 'list'
)

render = web.template.render('templates', base='base')

class index:
    def GET(self):
        return render.index()
    def POST(self):
        i = web.input()
        person = Person()
        person.name = i.name
        person.put()
        return web.seeother('/list')

class list:
    def GET(self):
        people = db.GqlQuery("SELECT * FROM Person ORDER BY created DESC LIMIT 10")
        return render.list(people)

app = web.application(urls, globals())
main = app.cgirun()
