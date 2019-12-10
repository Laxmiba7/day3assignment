from django.urls import path

from .views import homePageView,date,timestamp

urlpatterns = [
    path('', homePageView),
    path('date/',date),
    path('timestamp/',timestamp)
]