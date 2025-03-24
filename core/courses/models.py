from django.db import models
from django.contrib.auth.models import User

class Instrument(models.Model):
    name = models.CharField(max_length=100)  # Например, "Гитара", "Барабаны"

    def __str__(self):
        return self.name

class Course(models.Model):
    title = models.CharField(max_length=200)
    instrument = models.ForeignKey(Instrument, on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return self.title

class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    order = models.IntegerField()  # Порядок урока в курсе
    presentation = models.FileField(upload_to='presentations/')  # PDF или PowerPoint
    video_url = models.URLField(blank=True)  # Ссылка на YouTube-видео (если есть)

    def __str__(self):
        return self.title

class UserProgress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
    completed_at = models.DateTimeField(auto_now_add=True)