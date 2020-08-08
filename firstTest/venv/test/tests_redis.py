# -*- coding = utf-8 -*-
# @Time :
# @ Author : Yeeero
# @File : tests_redis.by
# @Software : PyCharm

import redis


def main():
    client = redis.Redis(host='127.0.0.1')
    print(client)
    client.set("name", "啊哈哈", ex=300)
    result = client.get('name').decode()
    # print(result)
    # print(client.hgetall('key1'))
    # print(client.mget('name','username'))
    # print(client.keys())
    print(client.zrange('page_rank', 0, -1, withscores=True))


if __name__ == '__main__':
    main()