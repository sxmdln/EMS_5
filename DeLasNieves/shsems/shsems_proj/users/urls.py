from django.urls import path, include

from users.views import ParticipantCreateView

urlpatterns = [
    path('users/', include("django.contrib.auth.urls")),
    path('signup/', ParticipantCreateView.as_view()),
    path('events/', include("events.urls")),
    path('home/', include("home.urls")),
]
