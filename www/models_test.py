import unittest

import www.orm as orm
from www.models import User, Blog, Comment


def test():
    yield from orm.create_pool(user='www-data', password='www-data', db='awesome')
    u = User(name='Test', email='test@example.com', password='1234567890', image='about:blank')
    yield from u.save()

for x in test():
    pass