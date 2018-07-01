

from marshmallow.validate import Validator, ValidationError
import netaddr



class IPv4Validator(Validator):
    """IPv4 Validator"""
    def __call__(self, value):
        try:
            if not netaddr.valid_ipv4(value):
                raise Exception
        except:
            raise ValidationError('Invalid ip {}'.format(value))
        return value


class IPv6Validator(Validator):
    """IPv6 Validator"""
    def __call__(self, value):
        try:
            if not netaddr.valid_ipv6(value):
                raise Exception
        except:
            raise ValidationError('Invalid ip {}'.format(value))
        return value


class ValidatorAny(Validator):
    """Validator ANY of others"""
    def __init__(self, validators):
        self.validators = validators

    def __call__(self, value):
        valid = False
        errors = []
        for v in self.validators:
            try:
                valid = v(value)
                break
            except ValidationError as e:
                errors.append(str(e))
        if not valid:
            raise ValidationError('{} not valid: {}'.format(value, errors))

        return value


class IPv4or6Validator(Validator):
    """IP v4 or v6 Validator"""
    def __call__(self, value):
        return ValidatorAny([IPv4Validator(), IPv6Validator()])(value)

import marshmallow as mm

class User():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return '<User(name={self.name!r}, age={self.age!r})>'.format(self=self)

class UserSchema(mm.Schema):
    name = mm.fields.List(mm.fields.String(validate=IPv4or6Validator()), default=[], missing=[])
    age = mm.fields.Int()

    @mm.post_load
    def make_blabla(self, data):
        return User(**data)



if __name__ == '__main__':
    print 'Hello'

    a = {'age' : 37}
    schema = UserSchema()
    c = schema.validate(a)
    print('c=', c)
    b = schema.dump(a)
    print('b=', b)

    print(a)
