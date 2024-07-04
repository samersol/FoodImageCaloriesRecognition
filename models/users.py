from mongoengine import Document, StringField

class UserFood(Document):
    email = StringField(required=True)
    fullName = StringField(required=True)
    password = StringField(required=True)
    goal = StringField(required=True)