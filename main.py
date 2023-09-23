from tornado import web, ioloop
import tornado
import asyncio

count = 0
class CountRequests(tornado.web.RequestHandler):
    async def get(self):
        global count
        count += 1
        print(count)
        self.write(str(count))

class GetFile(tornado.web.RequestHandler):
    async def get(self):
        global count
        count += 1
        self.render("hw1.html")


if __name__ == "__main__":
    app = tornado.web.Application([
        (r"/hw", GetFile),
        (r"/count", CountRequests)
    ])
    app.listen('8888')
    tornado.ioloop.IOLoop.current().start()