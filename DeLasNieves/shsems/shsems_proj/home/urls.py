from django.urls import path, include
from .views import HomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name="home"),
    path('events/', include("events.urls")),
    # path('user/', include("users.urls")),
]