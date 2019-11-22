from django.db import models
from extras.utils import generate_random_string

def poster_upload_path(instance, filename):
    return "posters/{}-{}".format(generate_random_string(10), filename)

class Event(models.Model):
        name = models.CharField("Name of Event",
            max_length = 150, blank = False, null = False)
        description = models.TextField("Description",
            max_length = 2000, blank= True)
        max_slots = models.IntegerField("Max Slots",
            blank = True, null = True)        
        date_from = models.DateField("Start Date")
        date_to = models.DateField("End Date")
        time_from = models.TimeField("Start Time")
        time_to = models.TimeField("End Time")
        creator = models.ForeignKey(to = "users.Participant",
            on_delete= models.CASCADE)
        poster = models.ImageField(upload_to = poster_upload_path, blank = True, 
        null = True, help_text = "Please upload an image with 16x9 resolution.")

        def __str__(self):
            return self.name

        def all_participants(self):
            return [x[0] for x in self.registration_set.values_list("participant__username")]
