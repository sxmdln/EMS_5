from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Event
from .forms import EventCreateForm

class EventListView(ListView):
    model = Event
    template_name = "events_list.html"

class EventDetailView(DetailView):
    model = Event
    template_name = "event_detail.html"
    context_object_name = "event"

class MyEventListView(LoginRequiredMixin, ListView):
    model = Event
    template_name = "my_events_list.html"

    def get_queryset(self):
        return Event.objects.filter(creator = self.request.user)

class MyEventCreateView(LoginRequiredMixin, CreateView):    
    form_class = EventCreateForm
    template_name = "event_create.html"   
    success_url = reverse_lazy("my_events_list")

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)


class EventUpdateView(LoginRequiredMixin, UpdateView):
    model = Event
    form_class = EventCreateForm
    template_name = "update.html"
    success_url = reverse_lazy("my_events_list")

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)

class EventDeleteView(LoginRequiredMixin, DeleteView):
    model = Event
    template_name = "delete.html"
    success_url = reverse_lazy("my_events_list")
