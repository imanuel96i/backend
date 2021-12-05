from django.conf.urls import url

from . import views



urlpatterns = [
    url(r'^registro/', views.UserCreateAPIView.as_view()),
]