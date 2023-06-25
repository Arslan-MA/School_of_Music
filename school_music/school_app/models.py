from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=80)
    surname = models.CharField(max_length=80)
    age = models.PositiveIntegerField()

    DIRECTIONS = (
        ('Фортепиано', 'Фортепиано'),
        ('Струнные инструменты', 'Струнные инструменты'),
        ('Духовые и ударные инструменты', 'Духовые и ударные инструменты')
    )

    directions = models.CharField(max_length=100, choices=DIRECTIONS)
    class_number = models.PositiveIntegerField()
    tool = models.CharField(max_length=80)

    def __str__(self):
        return f"{self.surname} - {self.name} - {self.directions} - {self.class_number} - {self.tool}"
