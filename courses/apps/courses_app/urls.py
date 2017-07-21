from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^add$', views.add),
    url(r'^confirm_remove$', views.confirm_remove),
    url(r'^remove$', views.remove),
    url(r'^index$', views.index),
    url(r'^$', views.index),
]
