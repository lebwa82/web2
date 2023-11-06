import os
import json
from tornado.ioloop import IOLoop
from tornado.web import RequestHandler, Application
from py_vapid import Vapid
from pywebpush import webpush

subscriptions = []

class PushHandler(RequestHandler):
    def post(self):
        subscription = json.loads(self.request.body)
        subscriptions.append(subscription)
        self.set_status(201)
        self.finish("Subscription registered.")

class SendPushHandler(RequestHandler):
    def post(self):
        vapid = Vapid.from_file("private_key.pem", "public_key.pem")

        for subscription in subscriptions:
            webpush(
                subscription_info=subscription,
                data="Неужели дошло?!",
                vapid_private_key=vapid,
            )

        self.write("Push notifications sent.")

class GetFile(RequestHandler):
    async def get(self):
        self.render("index.html")

def make_app():
    return Application([
        ("/push", PushHandler),
        ("/send-push", SendPushHandler),
        (r"/", GetFile),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8000)
    print("Server started on port 8000")
    IOLoop.current().start()