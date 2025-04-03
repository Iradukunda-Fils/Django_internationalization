from django.urls import path
from .views import home, Item, index
from django.utils.translation import gettext_lazy as _

urlpatterns = [
    path('',home,name="home"),
    path('item',Item, name="item"),
    path("index", index, name="index")
]
