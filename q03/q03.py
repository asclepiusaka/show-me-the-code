#!/usr/bin/env python3

import redis
#open redis-server first, if all the set is default, then
db = redis.StrictRedis()
with open("record.txt","r") as f:
    for line in f.readlines():
        db.lpush("code",line.strip("\n"))
db.save()

'''
to check the result, open redis-cli, type:
lrange code 0 200
'''