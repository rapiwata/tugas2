from django.db import models

TYPE_CHOICES = [
    ('Tugas Harian', 'Tugas Harian'),
    ('Tugas Akhir', 'Tugas Akhir'),
    ("Ujian", "Ujian"),
]

class Assignment(models.Model):
    name = models.CharField(max_length=50)
    subject = models.CharField(max_length=20)
    date = models.DateTimeField(auto_now_add=True)
    progress = models.IntegerField()
    description = models.TextField()



