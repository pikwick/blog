import marshmallow as mm

class User():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return '<User(name={self.name!r}, age={self.age!r})>'.format(self=self)

class UserSchema(mm.Schema):
    name = mm.fields.List(mm.fields.String)
    age = mm.fields.Int()

    @mm.post_load
    def make_blabla(self, data):
        return User(**data)




