from google.appengine.ext import db

class Person(db.Model):
    name = db.StringProperty()
    ssn = db.StringProperty()
    created = db.DateTimeProperty(auto_now_add=True)
