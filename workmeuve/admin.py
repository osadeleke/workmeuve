from django.contrib import admin
from .models import User, Bus, Ticket, Driver

admin.site.register(User)
admin.site.register(Driver)
admin.site.register(Ticket)
admin.site.register(Bus)