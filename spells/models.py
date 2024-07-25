from django.db import models

class Spell(models.Model):
     LEVEL_CHOICES = [(i, str(i)) for i in range(10)]  
     name = models.CharField(max_length=100)
     description = models.TextField()
     level = models.IntegerField(choices=LEVEL_CHOICES)

     def __str__(self):
        return self.name