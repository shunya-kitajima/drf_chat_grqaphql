from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from graphene_subscriptions.consumers import GraphqlSubscriptionConsumer

application = ProtocolTypeRouter({
    "websocket": URLRouter({
        path("graphgl/", GraphqlSubscriptionConsumer),
    }),
})
