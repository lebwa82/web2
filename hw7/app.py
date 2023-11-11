import os
import json
from tornado.ioloop import IOLoop
from tornado.web import RequestHandler, Application
from py_vapid import Vapid
from pywebpush import webpush
import pybase64
import base64
from base64 import urlsafe_b64encode
subscriptions = []

def base64UrlEncode(data: bytes) -> str:
    """Base64Url Encode data."""
    return base64.urlsafe_b64encode(data).rstrip(b'=').decode('utf-8')

class PushHandler(RequestHandler):
    def post(self):
        global subscription
        subscription = json.loads(self.request.body)
        subscriptions.append(subscription)
        self.set_status(201)
        self.finish("Subscription registered.")
        print(f'subscriptions = {subscriptions}')

class PushCertHandler(RequestHandler):
    def get(self):
        global certs
        certs = Vapid()
        certs.generate_keys()
        from cryptography.hazmat.primitives import serialization
        pub_key = base64UrlEncode(certs.public_key.public_bytes(
            serialization.Encoding.X962,
            serialization.PublicFormat.UncompressedPoint
        ))

        self.write(pub_key)

class SendPushHandler(RequestHandler):
    def post(self):
        global subscriptions
        print(f'subscriptions = {subscriptions}')
        print('sending push')
        for subscription in subscriptions:
            print('push')
            webpush(
                subscription_info=subscription,
                data="Неужели дошло?!",
                vapid_private_key=certs,
                vapid_claims={"sub": "mailto:test@example.com"}
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
        (r'/push-cert', PushCertHandler)
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8000)
    print("Server started on port 8000")
    IOLoop.current().start()