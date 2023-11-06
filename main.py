from tornado import web, ioloop, websocket
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

class EchoWebSocket(tornado.websocket.WebSocketHandler):
    def check_origin(self, origin):
        return True
    def open(self):
        print("WebSocket opened")

    def on_message(self, message):
        self.write_message(u"You said: " + message)

    def on_close(self):
        print("WebSocket closed")


if __name__ == "__main__":
    app = tornado.web.Application([
        (r"/hw", GetFile),
        (r"/count", CountRequests),
        (r"/websocket", EchoWebSocket),
    ])
    app.listen('8888')
    tornado.ioloop.IOLoop.current().start()