from django.contrib import admin
from .models import Instrument, Course, Lesson, UserProgress

admin.site.register(Instrument)
admin.site.register(Course)
admin.site.register(Lesson)
admin.site.register(UserProgress)