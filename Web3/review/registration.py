from mongoengine import Document, StringField, ListField, IntField

class Users(Document):
    firstname = StringField()
    lastname = StringField()
    email = StringField()
    yob = StringField()
    gender = StringField()
    city = StringField()

