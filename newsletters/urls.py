from django.urls import path
from .views import newsletter_signup, newsletter_unsubscribe

app_name = "newsletters"

urlpatterns = [
    path('', newsletter_signup, name="home"),
    path('unsubscribe/', newsletter_unsubscribe, name="unsubscribe")
]
