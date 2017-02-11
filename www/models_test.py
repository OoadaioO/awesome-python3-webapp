#!/bin/user/env python3
# -*- coding: utf-8 -*-

__author__="阿呆"

import orm,asyncio
from models import User, Blog, Comment

loop = asyncio.get_event_loop()

async def test():
    await orm.create_pool(loop=loop,user='www-data', password='www-data', db='awesome')
    u = User(name='Test', email='test@example.com', password='1234567890', image='about:blank')
    await u.save()

loop.run_until_complete(test())
loop.close()
