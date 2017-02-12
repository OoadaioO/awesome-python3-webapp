#!/bin/user/env python3
# -*- coding: utf-8 -*-

__author__="阿呆"

import orm,asyncio
from models import User, Blog, Comment

loop = asyncio.get_event_loop()

async def test():
    await orm.create_pool(loop=loop,user='www-data', password='www-data', db='awesome')
    u = await User.find_all('email = ?',['test@example.com'])
    if u is not None:
        print('user already exist:\n%s' % u)
        
        await u[0].remove()
    u = User(name='Test', email='test@example.com', password='1234567890', image='about:blank')
    await u.save()

loop.run_until_complete(test())
loop.close()
