from django.urls import path

from .views import (EventListView, EventDetailView, MyEventListView, MyEventCreateView,EventUpdateView, EventDeleteView)

urlpatterns = [
    path('', EventListView.as_view(), name= "events_list"),
    path('new/', MyEventCreateView.as_view(), name= "event_create"),
    path('my-events/', MyEventListView.as_view(), name= "my_events_list"),
    path('<int:pk>/', EventDetailView.as_view(),
    name ="event_detail"),
    path('edit/<int:pk>', EventUpdateView.as_view(),name = "update"),
    path('delete/<int:pk>', EventDeleteView.as_view(),name = "delete"),
    
]
