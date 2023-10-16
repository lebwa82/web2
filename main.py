from tornado import web, ioloop
import tornado
import asyncio
import redis

redis_client = redis.Redis(host = "localhost", db = 0)
DAY_SECONDS = 60*60*24

def increment():
    global redis_client
    count = redis_client.get("count_requests")
    if not count:
        print("ttl expired")
        redis_client.set(name = "count_requests", value = 0, ex = DAY_SECONDS)
    else:
        print("ttl = ", redis_client.ttl("count_requests"))

    redis_client.incr('count_requests')
    count = redis_client.get("count_requests")
    return count

class CountRequests(tornado.web.RequestHandler):
    async def get(self):
        count = increment()
        self.write(str(count))

class GetFile(tornado.web.RequestHandler):
    async def get(self):
        increment()
        self.render("hw1.html")


if __name__ == "__main__":
    redis_client.set(name = "count_requests", value = 0, ex = DAY_SECONDS)

    app = tornado.web.Application([
        (r"/hw", GetFile),
        (r"/count", CountRequests)
    ])

    print('enter port')
    port  = int(input())
    app.listen(port)
    tornado.ioloop.IOLoop.current().start()